from dash import html, dcc, dash_table
from app import *
from styles import *




def index_page():
    return  html.Div([
                html.Div(
                    html.H1('Bem vindo ao Neuro Cloud!', style={'textAlign': 'center', 'color': 'black', 'fontSize': 30}),
                    style={'backgroundColor': 'rgba(255, 255, 255, 0.5)', 'padding': '20px', 'borderRadius': '10px', 'margin': '20px auto'}
                ),
                dcc.Link(
                    html.Button('Login',
                                style={'width': '100%', 'backgroundColor': '#0000FF', 'color': 'white', 'padding': '14px 20px', 'margin': '8px 0', 'border': 'none', 'cursor': 'pointer'}),
                                href='/pagina-1', style={'display': 'flex', 'margin': 'auto', 'justifyContent':'center'}
                    )
               
            ], style={'justifyContent' : 'center'})




def login_page():
    
    body_text = [html.P("Ao solicitar um cadastro, você aceita nossos termos e condições de uso e nossa política de privacidade, que estão em concordância com a LGPD (lei geral de proteção de dados)."), 
                 html.P("Você será redirecionado para uma página, onde poderá solicitar uma conta.")]


    modal = create_modal("modal-confirm-login", "confirm-login", "close-login-modal", "Termos e condições", body_text, " Prosseguir com o cadastro")

    return html.Div([
                html.Div([
                    html.H2("Login", style={'textAlign': 'center', 'color': 'white'}),
                    html.Div([
                        dcc.Input(
                            id='username-input',
                            type='text',
                            placeholder='Usuário',
                            style={'width': '95%', 'padding': '10px', 'margin': '8px 0'}
                        ),
                        dcc.Input(
                            id='password-input',
                            type='password',
                            placeholder='Senha',
                            style={'width': '95%', 'padding': '10px', 'margin': '8px 0'}
                        ),
                        html.Button(
                            'Entrar',
                            id='login-button',
                            n_clicks=0,
                            style={'width': '100%', 'border': '2px solid #fff', 'borderRadius': '10px', 'backgroundColor': '#000', 'color': 'white', 'padding': '14px 20px', 'margin': '8px 0', 'cursor': 'pointer'}
                        ),
                        dbc.Button(
                            'Solicitar um cadastro',
                            id='open-login-modal',
                            n_clicks=0,
                            href='/pagina-1',
                            style={ 'color': 'white', 'cursor': 'pointer', 'border': 'none', 'background': 'transparent', 'textDecoration': 'underline'}
                        )
                    ], style={'maxWidth': '600px', 'margin':'auto'}),
                ], style={'border': '2px solid #fff', 'borderRadius': '12px', 'background': 'linear-gradient(to right, #000, #555)', 'padding': '20px', 'display': 'flex', 'flexDirection': 'column', 'justifyContent': 'center', 'alignItems': 'center', 'width': '100%', 'maxWidth': '350px', 'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.2)', 'marginTop': '50px'}),
                modal
            ], style={'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center', 'height': '100vh', 'fonFamily': 'Arial, sans-serif'})




def create_modal(modal_id, confirm_button_id, close_id, header_text, body_text, button_text):

    return dbc.Modal(
                [   html.Div([
                    dbc.ModalHeader(dbc.ModalTitle(header_text), style={'background': 'linear-gradient(to right, #111, #555)', 'color': '#fff'}),
                    dbc.ModalBody(
                                    body_text,
                                    style={'background': 'linear-gradient(to right, #111, #555)', 'color': '#fff'}
                                ),
                    dbc.ModalFooter(
                        [
                            dbc.Button("Cancelar", id=close_id, className="ms-auto", n_clicks=0, style={'backgroundColor': '#222', 'border': '2px solid #fff'}),
                            dcc.Link(dbc.Button(button_text, id=confirm_button_id, className="ms-2", n_clicks=0, style={'backgroundColor': '#222', 'border': '2px solid #fff'}), href='/')
                        ], style={'background': 'linear-gradient(to right, #111, #555)', 'color': '#000'}
                    ),
                    ], style={'border': '2px solid #fff', 'borderRadius': '8px'})
                ],
                id=modal_id,
                is_open=False,  # Inicialmente fechado
            )





# Função para criar a Navbar
def create_navbar():
    navbar = html.Div([
                dcc.Link( html.H2('NeuroCloud', style={'margin': '0', 'textDecoration': 'none', 'color': '#fff'}), href='/pagina-3', style={'textDecoration': 'none'}),
                html.Div([
                    dcc.Link( dbc.Button('Inserir', style=button_style), href='/pagina-inserir'),
                    dcc.Link( dbc.Button('Processar dados', style=button_style), href='/pagina-grafico'),
                    dcc.Link( dbc.Button('Atualizar', style=button_style), href='/pagina-atualizar'),
                    dcc.Link( dbc.Button('Histórico', style=button_style), href='/pagina-historico'),
                    dcc.Link( dbc.Button('Listar Pacientes', style=button_style), href='/pagina-pacientes'),
                    dbc.Button('Logoff', id='open-logoff-modal', style=button_style)
                ], style={'display': 'flex', 'gap': '20px'})
            ], style=navbar_style)
    

    body_text = [html.P("Você realmente deseja sair?"), 
                 html.P("Um novo login será requerido.")]

    modal = create_modal("modal-confirm-logoff", "confirm-logoff", "close-logoff-modal", "Confirmação de Logoff", body_text, "Confirmar Logoff")

    return html.Div([
            navbar,
            modal
    ])




def create_social_link(href, icon_class, text):
    return html.A(
        dbc.Button(
            [html.I(className=icon_class), f" {text}"],
            color="link",
            style={'color': '#fff', 'textDecoration': 'none'}
        ),
        href=href,
        target="_blank",
        style=link_style
    )




# Função para criar o Footer
def create_footer(encoded_logo = None):
    if encoded_logo is None:
        encoded_logo = "<default_base64_string>"

    social_links = html.Ul(
        children=[
            html.Li(create_social_link('https://www.instagram.com', 'fab fa-instagram','Instagram')),
            html.Li(create_social_link('https://www.facebook.com', 'fab fa-facebook','Facebook')),
            html.Li(create_social_link('https://www.linkedin.com', 'fab fa-linkedin','LinkedIn')),
            html.Li(create_social_link('https://www.twitter.com', 'fab fa-twitter','Twitter')),
        ],
        style={
            'listStyleType': 'none',
            'padding': '0',
            'margin': '0',
        }
    )

    page_links = html.Ul(
        children=[
            html.Li(dcc.Link('Página Inicial', href='/pagina-3', style=link_style)),
            html.Li(dcc.Link('Sobre Nós', href='/sobre', style=link_style)),
            html.Li(dcc.Link('Dúvidas Frequentes', href='/duvidas', style=link_style)),
            html.Li(dcc.Link('Conheça a análise EEG', href='/proposito', style=link_style)),
            html.Li(dcc.Link('Política de privacidade', href='/termos', style=link_style)),
        ],
        style={
            'listStyleType': 'none',
            'padding': '0',
            'margin': '0'
        }
    )

    return  html.Footer([


                html.Div([
                    html.Img(src=f"data:image/jpg;base64,{encoded_logo}", style={'height': '90px', 'width': '114px', 'marginBottom': '10px', 'borderRight': '70px'}),
                    html.P('Plataforma de análise de dados EEG', style={'fontFamily': 'Times' }),
                    html.P('Email: neurocontact@gmail.com'),
                    html.P('LinkedIn: link'),
                ], style=column_style),
                html.Div([
                    html.H6('Contato'),
                    html.Li('Telefone: +55 (45) 4002-8922', style={'listStyleType': 'none', 'marginTop': '16px'}),
                    html.Li('Whatsapp: +55 (45) 9 9988-7766', style={'listStyleType': 'none', 'marginTop': '16px'}),
                    html.Li('Email: neurosupport@gmail.com.br', style={'listStyleType': 'none', 'marginTop': '16px'}),
                ], style=column_style),
                html.Div([
                    html.H6('Redes Sociais', style={'marginLeft': '10px', 'marginTop': '20px'}),
                    social_links
                ], style=column_style),
                html.Div([
                    html.H6('Links Rápidos'),
                    page_links
                ], style=column_style),
                html.Hr(style=bottom_line_style),
                html.P('© 2024 NeuroCloud. Todos os direitos reservados.', style={'textAlign': 'center', 'width': '100%'})
            ], style=footer_style)



# Função para criar a Home Page
def home_page(encoded_logo = None):

    navbar = create_navbar()
    footer = create_footer(encoded_logo)


    plot_card = dbc.Card(
        [
            dbc.CardImg(
                src="/assets/ExamplePlot.png",
                top=True,
                style={"opacity": 1.0},
            ),
            dbc.CardImgOverlay(
               
            ),  
        ],
        style={"width": "26rem", 'height': '80 rem', 'border': '4px solid #fff', 'borderRadius': '10px'},
    )

    neuro_card = dbc.Card(
        [
            dbc.CardImg(src="/assets/CardNeurocloud.png", top=True, style={"opacity": 0.9,  'maxHeight': '175px'}),
            dbc.CardBody(
                [
                    html.H4("EEG", className="card-title"),
                    html.P(
                        "O que é análise de eletroencefalograma?",
                        className="card-text",
                    ),
                    dbc.Button("Conheça a análise EEG", style={'backgroundColor': '#222', 'border': '2px solid #fff'}),
                ], style={'background': 'linear-gradient(to right, #111, #555)', 'color': '#fff'}
            ),
        ],
        style={"width": "18rem", 'border': '4px solid #fff', 'borderRadius': '10px'},
    )


    main_content = html.Div([
        html.H1('Home', style={'textAlign': 'left', 'color': 'white'}),
        html.Br(),

        html.Div([
            html.Div([
                html.P('Nosso objetivo é fornecer ferramentas avançadas e acessíveis para a análise precisa do EEG, ajudando médicos, pesquisadores e profissionais da saúde a entender melhor a atividade cerebral e fornecer tratamentos mais eficazes para uma variedade de condições neurológicas.', style={'text-align': 'justify', 'marginLeft': '20px', 'color': 'white'}),
                html.Br(),
                neuro_card
            ], style={'flex': '2', 'paddingRight': '60px'}),
            html.Div([
                plot_card
            ], style={'flex': '1'})
        ], style={'display': 'flex'}),
    ], style=main_content_style)

    return html.Div([
        html.Div([    
            navbar,
            main_content,
            footer
        ], style={'display': 'flex', 'flexDirection': 'column', 'minHeight': '100vh', 'backgroundColor': 'transparent', 'flexGrow':'1', 'border': 'none'})
    ], style=home_page_div_style)



def insert_page(encoded_logo = None):
    navbar = create_navbar()
    footer = create_footer(encoded_logo)

    main_content = html.Div([
        html.H1('Inserir Dados da consulta', style={'textAlign': 'left', 'color': 'white'}),
        html.Br(),
        html.Div([
            html.Label('Nome do Paciente:', style={'color': 'white'}),
            dcc.Input(id='nome-paciente', type='text', style=input_insert_page_style),
            html.Br(),
            html.Label('Título da Consulta:', style={'color': 'white'}),
            dcc.Input(id='titulo-consulta', type='text', style=input_insert_page_style),
            html.Br(),
            html.Label('Número do Protocolo:', style={'color': 'white'}),
            dcc.Input(id='numero-protocolo', type='text', style=input_insert_page_style),
            html.Br(),
            html.Label('Data:', style={'color': 'white'}),
            dcc.Input(id='data-consulta', type='text', style=input_insert_page_style),
            html.Label('Carregar Arquivo:', style={'color': 'white'}),
            dcc.Upload(id='upload-arquivo', children=html.Div(['Arraste e solte ou ', html.A('Selecione os arqiuvos')]), style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px 0',
                'backgroundColor':'white'
            }),
            html.Br(),
            dbc.Button('Inserir', id='inserir-dados', n_clicks=0, style={'background': '#111', 'border': '1px solid #fff'}),
            dbc.Button('Limpar', id='limpar-campos', n_clicks=0, style={'background': '#111', 'border': '1px solid #fff', 'marginLeft': '7px'}),
            html.Div(id='mensagem-insercao', style={'marginTop': '10px', 'color': 'white'})
        ], style={'maxWidth': '500px', 'maxHeight': '500px', 'margin': 'auto'})
    ], style=main_content_style)

    return html.Div([
        html.Div([
            navbar,
            main_content,
            footer
        ], style={'display': 'flex', 'flexDirection': 'column', 'height': '100vh', 'backgroundColor': 'transparent', 'flexGrow':'1', 'border': 'none'})
    ], style={'display': 'flex', 'flexDirection': 'column', 'height': '100vh'})


def query_page(encoded_logo = None):
    navbar = create_navbar()
    footer = create_footer(encoded_logo)

    list = ['number1','number2', 'number3' ]
    dados = [
    {"id": 1, "nomeConsulta": "falta de atenção", "data": "12/01/2023", "nomePaciente": "Sebastian Bach", "arquivo": "arquivo1.pdf"},
    {"id": 2, "nomeConsulta": "análise autismo", "data": "01/12/2024", "nomePaciente": "André Marques", "arquivo": "arquivo2.pdf"},
    {"id": 3, "nomeConsulta": "análise tdah", "data": "07/04/2023", "nomePaciente": "Albert Einstein", "arquivo": "arquivo3.pdf"}
]

    main_content = html.Div([
                        html.H1('Listar pacientes e consultas cadastradas', style={'textAlign': 'left', 'color': 'white'}),
                        html.Br(),

                        html.Div([

                            html.Div(
                                dash_table.DataTable(
                                    id='table',
                                    columns=[
                                        {"name": "ID", "id": "id"},
                                        {"name": "Titulo da consulta", "id": "nomeConsulta"},
                                        {"name": "data", "id": "data"},
                                        {"name": "Nome", "id": "nomePaciente"},
                                        {"name": "Arquivo", "id": "arquivo", "presentation": "markdown"}
                                    ],
                                    data=dados,
                                    style_cell={'textAlign': 'left', 'padding': '5px', 'color': '#fff', 'backgroundColor': '#000', 'border': '1px solid #fff'},
                                    style_header={
                                        'backgroundColor': '#000',
                                        'fontWeight': 'bold',
                                        'border': '1px solid #fff'
                                    },
                                    style_data={
                                        'border': '1px solid #fff'
                                    },
                                    style_table={'borderRadius': '15px', 'overflow': 'hidden', 'border': '2px solid #fff'},
                                    markdown_options={"html": True}
                                )
                            ),

                            html.Br(),
                            dbc.Button('Inserir', id='listar-consultas', n_clicks=0, style={'background': '#111', 'border': 'none'}),
                            dbc.Button('Limpar', id='lstar-pacientes', n_clicks=0, style={'background': '#111',  'border': 'none', 'marginLeft': '7px'})
                            
                        ], style={'maxWidth': '800px', 'margin': 'auto'})
                    ], style=main_content_style)

    return html.Div([
        html.Div([
            navbar,
            main_content,
            footer
        ], style={'display': 'flex', 'flexDirection': 'column', 'height': '100vh', 'backgroundColor': 'transparent', 'flexGrow':'1', 'border': 'none'})
    ], style={'display': 'flex', 'flexDirection': 'column', 'height': '100vh'})









def graph_external_layout():

    return html.Div()




def graph_page_layout(encoded_logo = None):

    navbar = create_navbar()
    footer = create_footer(encoded_logo)

    main_content =  html.Div([
                    
                        dcc.Upload(
                            id='upload-data',
                            children=html.Button('Upload File'),
                            multiple=False
                        ),
                        

                        html.Div([

                             dcc.Dropdown(
                                id='graph-layout-dropdown',
                                options=[{'label': 'Canais individuais', 'value': '0'},
                                        {'label': 'Canais sobrepostos', 'value': '1'},
                                ],
                                placeholder='Disposição dos canais',
                                value='0',
                                style={'flex': '2', 'justifyContent': 'left', 'width':'225px'}
                            ),

                            
                                html.Label('Filtro passa-baixa:', style={'color':'#fff'}),
                                dcc.Input(id='low-pass-input', value='', type='text', style={'borderRadius': '6px', 'maxHeight': '5vh'})
                           

                        ], style={'display': 'flex', 'alignItems': 'center', 'marginTop': '10px'}),

                    

                        html.Div([

                            dcc.Dropdown(
                                    id='montage-dropdown',
                                    options=[{'label': 'padrão 10-05', 'value': 'standard_1005'},
                                            {'label': 'padrão 10-20', 'value': 'standard_1020'},
                                            {'label': 'padrão 10-20 pós-fixado', 'value': 'standard_postfixed'},
                                            {'label': 'padrão 10-20 prefixado', 'value': 'standard_prefixed'},
                                            {'label': 'padrão easycap M1', 'value': 'easycap-M1'},
                                            {'label': 'padrão easycap M10', 'value': 'easycap-M10'}
                                    ],
                                    placeholder='Selecione uma opção de montagem',
                                    style={'flex': '2', 'justifyContent': 'left', 'width':'300px'}
                            ),

                                html.Label('Filtro passa-alta:', style={'color':'#fff'}),
                                dcc.Input(id='high-pass-input', value='', type='text', style={'borderRadius': '6px', 'maxHeight': '5vh'})
                            

                        ], style={'display': 'flex', 'alignItems': 'center', 'marginTop': '10px'}),


                        html.Div([
                            html.Div([
                                html.Button(
                                    id='ica-button',
                                    children='Plotar ICA',
                                    type='button',
                                    style={ 'font-family': 'Times New Roman'}
                                )
                            ], style={'display': 'flex', 'justifyContent': 'flex-start', } ),
                            
                            html.Div([
                                html.Button('Filtrar frequências', id='submit-filter', n_clicks=0)
                            ], style={'display': 'flex', 'justifyContent': 'flex-end'})

                        ], style={'marginBottom': '10px', 'marginTop': '10px', 'display': 'flex', 'justifyContent': 'space-between', 'flexDirection': 'row'}),        
                       

                        html.Div(
                            id='eeg-graph-div',
                            children=[html.Div( style={'marginTop': '135px'})],
                            
                        ),

                        dcc.Store(id='eeg-store')  # Armazena os dados do EEG
                    ], style={ 'display': 'block', 'padding': '30px', }) #block foi responsável por resolver o problema da largura do gráfico

    return html.Div([
                navbar,
                main_content,
                footer
    ])



def build_graph_layout(ch_names, fig):

    checklist = dcc.Checklist(
        id='channels-checklist',
        options=[{'label': channel, 'value': channel} for channel in ch_names],
        value=[],  # Nenhum canal selecionado por padrão
        labelStyle={'display': 'block', 'marginBottom':'80px'},  # Mostrar cada checkbox em sua própria linha
        style={'flex': '1', 'color':'#fff'}
    )

    return html.Div([
        html.Button(
            id='interpolation-button',
            children='Interpolar canais',
            type='button',
            style={'flex': '2', 'font-family': 'Time New Roman', 'marginRight': '5px'}
        ),

        html.Button(
            id='drop-channels-button',
            children='Excluir canais marcados',
            type='button',
            style={'flex': '2', 'font-family': 'Times New Roman', 'marginBottom': '10px'}
        ),
        
        html.Br(),

        html.Div([
            dcc.Graph(id='eeg-graph', figure=fig, config={'scrollZoom': True}, style={'flex': '3', 'width': '80%'}),
            html.Div(
                [checklist],
                style={'marginTop': '125px', 'marginRight':'20px'}
            ),
        ],
            style={'display': 'flex', 'flexDirection': 'row', 'flexWrap': 'wrap'}
        )
    ], style={'marginTop': '10px'} )


def build_overlaped_graph_layout(ch_names, fig):

    checklist = dcc.Checklist(
        id='channels-checklist',
        options=[{'label': channel, 'value': channel} for channel in ch_names],
        value=[],  # Nenhum canal selecionado por padrão
        labelStyle={'display': 'block', 'marginBottom':'80px'},  # Mostrar cada checkbox em sua própria linha
        style={'flex': '1', 'display':'none'}
    )

    return html.Div([
        
        html.Button(
            id='interpolation-button',
            children='Interpolar canais marcados',
            type='button',
            style={'flex': '2', 'font-family': 'Times New Roman', 'marginRight': '5px'}
        ),

        html.Button(
            id='drop-channels-button',
            children='Excluir canais marcados',
            type='button',
            style={'flex': '2', 'font-family': 'Times New Roman', 'marginBottom': '10px'}
        ),

        html.Div([
            dcc.Graph(id='eeg-graph', figure=fig, config={'scrollZoom': True}, style={'flex': '3', 'width': '85%'}),
                html.Div(
                    [checklist],
                    style={'marginTop': '125px', 'marginRight':'20px'}
                ),
        ],
            style={'display': 'flex', 'flexDirection': 'row', 'flexWrap': 'wrap'}
        )
    ] 
    )
