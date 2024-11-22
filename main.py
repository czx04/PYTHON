import dash
import plotly.graph_objs as go
from dash import dcc, html
from dash.dependencies import Input, Output

from PYTHON.data import datagame, user_counts, total_games, total_dau, average_playtime
# import pages
from PYTHON.pages.game_layout import showgame
from PYTHON.pages.home import homepage_layout
from PYTHON.pages.notfound import notfound

# Khởi tạo ứng dụng Dash
app = dash.Dash(__name__)
app.title = "Dash Multi-Page App"

# UI

app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        html.Div(id="page-content", children=homepage_layout)
    ],
    style={
    }
)


@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname"),
)
def display_page(pathname):
    if pathname == "/" or pathname is None:
        return homepage_layout
    elif pathname.startswith("/games"):
        return showgame(pathname)
    else:
        return notfound(pathname)


if __name__ == '__main__':
    app.run_server(debug=True, port=3040)
