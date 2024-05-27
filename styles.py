import base64


with open("assets/Background1.png", "rb") as background_image_file:
    home_background = base64.b64encode(background_image_file.read()).decode('utf-8')

# Página 3 (Página Home)
navbar_style = {
    'padding': '10px 2rem',
    'background': 'linear-gradient(to right, #000, #555)',
    'display': 'flex',
    'justifyContent': 'space-between',
    'alignItems': 'center',
    'borderBottomLeftRadius': '30px',
    'borderBottomRightRadius': '20px',
    'color':'#fff',
    'border': '2px solid #fff'
}

# Definindo o estilo para o conteúdo principal
main_content_style = {
    'paddingTop': '55px',
    'paddingLeft': '55px',
    'paddingRight': '55px',
    'paddingBottom': '23px',
    'flexGrow': '0',
}

link_style = {
    'color': '#fff',
    'marginBottom': '0.5rem',  # Espaço entre os links
}

button_style = {
    'background': 'transparent',
    'color': '#fff',
    'marginBottom': '0.5rem',  # Espaço entre os links
    'border': 'none'
}

home_page_div_style = {

    'backgroundImage': f'linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url("data:image/jpg;base64,{home_background}")',
    'backgroundSize': 'cover',
    'backgroundPosition': 'center center',
    'backgroundRepeat': 'no-repeat',
    'border':'none',
    'padding':'none',
    'margin':'none'
}



input_insert_page_style={
    'width': '100%',
    'borderRadius': '8px'
}

# Footer com informações de contato
footer_style = {
    'display': 'flex',
    'justifyContent': 'space-between',
    'padding': '2rem 6rem 1rem 2rem ',
    'background': 'linear-gradient(to right, #000, #555)',
    'color': '#fff',
    'flexWrap': 'wrap',
    'alignItems': 'center',  # Certifique-se de que os itens estejam alinhados verticalmente
    'position': 'relative',  # ou 'fixed' se você quiser que o footer fique sempre visível
    'bottom': '0',  # Se position for 'fixed', isso colocará o footer na parte inferior
    'borderTopLeftRadius':'30px',
    'border': '2px solid #fff'
}

column_style = {
    'display': 'flex',
    'flexDirection': 'column',
    'padding': '0 1rem',
    'borderLeft': '0px',
    'alignItems': 'start'
}


bottom_line_style = {
    'width':'94%',
    'backgroundColor': '#fff',
    'borderBottom':'2px solid' ,
    'margin':'20px auto',
    'bottom':'0'
  } 