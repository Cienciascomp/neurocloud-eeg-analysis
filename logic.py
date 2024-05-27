import mne
import plotly.graph_objs as go
from plotly.subplots import make_subplots

def create_minimal_raw(eeg_data):

    info = mne.create_info(ch_names=eeg_data['ch_names'], sfreq=eeg_data['sfreq'], ch_types='eeg')

    raw = mne.io.RawArray(eeg_data['data'], info)

    return raw


def correct_channels_names(ch_names):

     for i in range(len(ch_names)):
        if ch_names[i][1].isupper():
            ch_names[i] = ch_names[i][0] + ch_names[i][1].lower() + ch_names[i][2:]


def drop_unwanted_channels(raw,  checklist_values):

    raw.drop_channels(ch_names=[ch_name for ch_name in checklist_values], on_missing='raise')


def build_graph_logic(ch_names, data, times):

    #Cria os subplots. O número de linhas é igual ao número de canais. Uma coluna.
    fig = make_subplots(rows=len(ch_names), cols=1, shared_xaxes=False, vertical_spacing=0.01)

    #Adiciona cada canal como um subplot. Caso não fosse utilizado, os canais ficariam sobrepostos
    for i, channel_name in enumerate(ch_names):
        fig.add_trace(go.Scatter(x=times, y=data[i], mode='lines', name=channel_name), row=i+1, col=1)

    #Atualiza a formatação do texto para cada eixo
    for axis in fig.layout:
        if axis.startswith('yaxis') or axis.startswith('xaxis'):
            fig.update_layout({
                axis: dict( gridcolor='gray', linecolor='gray',
                    tickfont=dict(size=12, color='#fff', family='Courier New, monospace')
                )
            })

    fig.update_layout(height=105*len(ch_names), title_text="EEG Data Plot", showlegend=False, margin=dict(l=30, r=10, t=100, b=15),  plot_bgcolor='#fff', paper_bgcolor='#222') #Edita características da figura usada para gerar o gráfico

    return fig


def build_overlaped_graph_logic(ch_names, data, times):

    fig = go.Figure()
    for i, channel_name in enumerate(ch_names):
        fig.add_trace(go.Scatter(x=times, y=data[i], mode='lines', name=channel_name))
    fig.update_layout(title='EEG Data Plot', height=650,   plot_bgcolor='#222', paper_bgcolor='#222', margin=dict(l=30, r=10, t=100, b=15)) #Edita características da figura usada para gerar o gráfico
    fig.update_xaxes(tickfont=dict(size=12, color='#fff', family='Courier New, monospace'))

    return fig


def build_ica_logic(eeg_data):

    raw = create_minimal_raw(eeg_data)

    raw.filter(1., None)

    ica = mne.preprocessing.ICA(n_components=20 , method='fastica', max_iter=800, random_state=91)

    ica.fit(raw, picks=None, start=None, stop=None, reject_by_annotation=True)

    sources = ica.get_sources(raw)

    ica_data, ica_times = sources.get_data(return_times = True)

    ica_name_list = []

    for i in range(len(eeg_data['ch_names'])):
        if i < 10: 
            ica_name_list.append('ICA00' + str(i))
        else:
            ica_name_list.append('ICA0' + str(i))

    return ica_name_list, ica_data, ica_times


# Lógica de autenticação
def authenticate_user(username, password):
    # Verificar se o nome de usuário e senha correspondem aos credenciais corretos
    return username == 'user' and password == 'senha'




