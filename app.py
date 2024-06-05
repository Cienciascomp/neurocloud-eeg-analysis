import dash
from flask_sqlalchemy import SQLAlchemy
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME])

app.server.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/test_db'
app.server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app.server)

app.config.suppress_callback_exceptions =True

server = app.server