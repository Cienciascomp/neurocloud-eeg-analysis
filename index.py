
from layout import *
from callbacks import *


with open("assets/NeuroCloud.png", "rb") as background_image_file:
    encoded_logo = base64.b64encode(background_image_file.read()).decode('utf-8')


def create_layout():

    with open("assets/neurobackground.png", "rb") as background_image_file:    
        encoded_background_string = base64.b64encode(background_image_file.read()).decode('utf-8')

    return html.Div([
            dcc.Location(id='url', refresh=False),
            html.Div(
                id='page-content', 
                children=[], 
                style={'display' : 'block', 'justifyContent' : 'center',
                    'minHeight': '100vh',
                    'minWidth' : '100vw', 
                    'background': f'linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url("data:image/png;base64,{encoded_background_string}") ',
                    'backgroundSize': 'cover'
                }
            )
        ])


app.layout = create_layout()

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/pagina-1':
        return login_page()
    elif pathname =='/pagina-2':
        return 
    elif pathname == '/pagina-3': 
        return home_page(encoded_logo) #coloca a logo aqui
    elif pathname == '/pagina-pacientes':
        return user_info_page(encoded_logo)
    elif pathname == '/pagina-grafico':
        return graph_page_layout(encoded_logo)
    elif pathname == '/pagina-inserir':
        return insert_page(encoded_logo) #aqui tambem
    else:
        return index_page()

@app.callback(Output('url', 'pathname'),
            [Input('login-button', 'n_clicks')],
            [State('username-input', 'value'),
            State('password-input', 'value')])
def authenticate_and_redirect(n_clicks, username, password):
    if n_clicks:
        if authenticate_user(username, password):
            return '/pagina-3'
        else:
            # Exibir uma mensagem de erro ou fazer outra ação se as credenciais estiverem incorretas
            print("Credenciais incorretas. Tente novamente.")
    # Se as credenciais não estiverem corretas ou o botão ainda não foi clicado, permanecer na mesma página
    return '/pagina-1'


if __name__ == '__main__':
    app.run_server(debug=True)