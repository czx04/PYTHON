# game_layout.py
import plotly.graph_objs as go
from dash import html, dcc

from PYTHON.data import datagame, months

back_btn = html.Div(
    style={"textAlign": "left"},
    children=[
        dcc.Link([
            html.Img(
                src="../assets/IMG/back_icon.png",
                alt="Info",
                className="info-icon",
                width="24",
                height="24",
                style={"cursor": "pointer", "padding": "30px 30px"},
            )
        ], href="/", style={"fontSize": "20px", "color": "blue"}),
    ],
)


def graph_nav(game_path):
    game_data = next((game for game in datagame if game["game"].lower().replace(" ","") == game_path), None)
    if game_data:
        user_counts = [int(game_data["user_up"][month]) for month in months]
    trace = go.Scatter(
        x=months,
        y=user_counts,
        mode='lines+markers',
        name=game_data["game"]
    )
    fig = go.Figure(data=[trace])
    fig.update_layout(
        title='User Growth for Valorant Over Months',
        xaxis_title='Month',
        yaxis_title='Number of Users',
        template='plotly_dark'
    )
    return html.Div(
        className="graph-nav",
        children=[
            html.Div(
                children=[
                    dcc.Graph(figure=fig)
                ],
                style={"padding": "20px"}
            )
        ],
        style={},
    )


navbar = html.Div(
    className="navbar",
    children=[
        back_btn
    ],
    style={}
)


def showgame(game):
    games = game.split('/')[2]
    return html.Div(
        className=f"{game}_div",
        children=[
            navbar,
            graph_nav(games)
        ],
        style={

        }
    )
