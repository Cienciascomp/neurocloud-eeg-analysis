from app import app
from dash import Input, Output, State, dash
import dash
from dash.exceptions import PreventUpdate
from logic import *
from layout import build_graph_layout, build_overlaped_graph_layout
import base64
import os
import json
import numpy as np
from tempfile import NamedTemporaryFile





@app.callback(
    Output(component_id='eeg-store', component_property='data', allow_duplicate=True),
    Input(component_id='upload-data', component_property='contents'),
    prevent_initial_call=True
)
def store_data(contents):
    #Adentra esse trecho caso contentes não seja nulo
    if contents is not None:
        #Decodifica o conteúdo do arquivo em base 64, pois ele foi carregado na web dessa forma. Escreve um arquivo temporário no buffer.
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        with NamedTemporaryFile(mode='w+b', delete=False, suffix='.edf') as tmp:
            tmp.write(decoded)
            tmp.flush()  # Garantir que todos os dados sejam escritos
            tmp.seek(0)  # Voltar ao início do arquivo para garantir que a leitura seja feita corretamente
            raw = mne.io.read_raw_edf(tmp.name, preload=True)

        #Exclui o arquivo temporário
        os.unlink(tmp.name)

        #Extrai os dados relevantes para a construção do gráfico
        data, times = raw.get_data(return_times=True)
        info = raw.info
        sfreq = info['sfreq']
        sfreq = str(sfreq)
        date = info.pop('meas_date')
        date = date.strftime('%Y-%d-%m %H:%M:%S')
        date_list = [date]

        ch_names = raw.ch_names

        correct_channels_names(ch_names)
        # Agrupando os dados e os times em um dicionário
        eeg_data = {
            'data': data,
            'times': times,
            'ch_names': ch_names,
            'sfreq': sfreq
        }

        # Convertendo qualquer ndarray em eeg_data para listas
        for key, value in eeg_data.items():
            if isinstance(value, np.ndarray):
                eeg_data[key] = value.tolist()  # Converte ndarrays para listas

        data_json = json.dumps(eeg_data)

        return data_json


@app.callback(
    Output(component_id='eeg-graph-div', component_property='children'),
    Input(component_id='eeg-store', component_property='data'),
    Input(component_id='graph-layout-dropdown', component_property='value'),
    Input(component_id='ica-button', component_property='n_clicks'),
    prevent_initial_call = True
)
def draw_graph(serialized_data, is_overlaped, n_clicks_ica):
    if serialized_data is not None:
        # base64_decoded_data = base64.b64decode(compressed_data)
        # decompressed_data = zlib.decompress(base64_decoded_data).decode('utf-8')
        eeg_data = json.loads(serialized_data)

        raw = create_minimal_raw(eeg_data)
        
        ctx = dash.callback_context

        if not ctx.triggered:
            raise PreventUpdate

        trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if trigger_id == 'ica-button':
            if n_clicks_ica is not None:
                ch_names, data, times = build_ica_logic(eeg_data)
        else:
            ch_names = eeg_data['ch_names']
            data = eeg_data['data']
            times = eeg_data['times']
        
        if is_overlaped == '0':
            fig = build_graph_logic(ch_names, data, times)
            return build_graph_layout(ch_names, fig)
        else:
            fig = build_overlaped_graph_logic(ch_names, data, times)
            return build_overlaped_graph_layout(ch_names, fig)
        

# Edita o gráfico, interpolando canais, filtrando frequências com passa-baixa ou passa-alta, ou excluindo canais marcados
@app.callback(
    Output(component_id='eeg-store', component_property='data', allow_duplicate=True),
    [Input(component_id='interpolation-button', component_property='n_clicks'),
    Input(component_id='drop-channels-button', component_property='n_clicks'),
    Input(component_id='submit-filter', component_property='n_clicks')],
    [State(component_id='montage-dropdown', component_property='value'),
    State(component_id='channels-checklist', component_property='value'),
    State(component_id='eeg-store', component_property='data'),
    State(component_id='low-pass-input', component_property='value'),
    State(component_id='high-pass-input', component_property='value')],
    prevent_initial_call=True
)
def filter_edit_channels(n_clicks_bads, n_clicks_drop, n_clicks_filter, montage, checklist_values, serialized_data, low_pass_value, high_pass_value):
     
    eeg_data = json.loads(serialized_data)

    raw = create_minimal_raw(eeg_data)

    ctx = dash.callback_context

    if not ctx.triggered:
        raise PreventUpdate

    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if trigger_id == 'interpolation-button':

        if n_clicks_bads is None:
            return serialized_data
        
        for ch_name in eeg_data['ch_names']:
            if ch_name in checklist_values:
                raw.info['bads'].append(ch_name)

        montage_choosen = mne.channels.make_standard_montage(montage)
        raw.set_montage(montage_choosen)
        updated_raw = raw.copy().interpolate_bads(reset_bads=False)
        
    elif trigger_id == 'submit-filter':

        if n_clicks_filter is None:
            return serialized_data
        
        if high_pass_value == '':
            high_pass_value = None
        else:
            high_pass_value = float(high_pass_value)

        if low_pass_value == '':
            low_pass_value = None
        else:
            low_pass_value = float(low_pass_value)

        updated_raw = raw.filter(high_pass_value , low_pass_value)

    elif trigger_id == 'drop-channels-button':

        if n_clicks_drop is None:
            return serialized_data
            
        updated_raw = raw.copy()

        drop_unwanted_channels(updated_raw, checklist_values)

    ch_names = updated_raw.info['ch_names']
    sfreq= updated_raw.info['sfreq']
    data, times = updated_raw.get_data(return_times=True)

    eeg_data = {
        'data': data,
        'times': times,
        'ch_names': ch_names,
        'sfreq': sfreq
    }

    # Convertendo qualquer ndarray em eeg_data para listas
    for key, value in eeg_data.items():
        if isinstance(value, np.ndarray):
            eeg_data[key] = value.tolist()  # Converte ndarrays para listas

    data_json = json.dumps(eeg_data)

    return data_json


@app.callback(
    Output('mensagem-insercao', 'children'),
    [Input('inserir-dados', 'n_clicks')],
    [State('nome-paciente', 'value'), State('titulo-consulta', 'value'), State('numero-protocolo', 'value'), State('upload-arquivo', 'contents')]
)
def inserir_dados(n_clicks, nome_paciente, titulo_consulta, numero_protocolo, upload_arquivo):
    if n_clicks > 0:
        # Aqui você pode adicionar a lógica para inserir os dados no programa
        return 'Dados inseridos com sucesso!'

@app.callback(
    [Output('nome-paciente', 'value'), Output('titulo-consulta', 'value'), Output('numero-protocolo', 'value'), Output('upload-arquivo', 'contents')],
    [Input('limpar-campos', 'n_clicks')]
)
def limpar_campos(n_clicks):
    if n_clicks > 0:
        return '', '', '', None
    return dash.no_update


@app.callback(
    Output(component_id="modal-confirm-logoff",  component_property="is_open"),
    [Input(component_id="open-logoff-modal",  component_property="n_clicks"), Input(component_id="close-logoff-modal",  component_property="n_clicks"), Input(component_id="confirm-logoff",  component_property="n_clicks")],
    [State(component_id="modal-confirm-logoff", component_property="is_open")]
)
def toggle_logoff_modal(n1, n2, n3, is_open):
    if n1 or n2 or n3:
        return not is_open
    return is_open

@app.callback(
    Output(component_id="modal-confirm-login",  component_property="is_open"),
    [Input(component_id="open-login-modal",  component_property="n_clicks"), Input(component_id="close-login-modal",  component_property="n_clicks"), Input(component_id="confirm-login",  component_property="n_clicks")],
    [State(component_id="modal-confirm-login", component_property="is_open")]
)
def toggle_login_modal(n1, n2, n3, is_open):
    if n1 or n2 or n3:
        return not is_open
    return is_open