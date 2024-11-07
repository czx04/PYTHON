# game_layout.py
import plotly.graph_objs as go
from dash import html, dcc
from openpyxl.styles.builtins import title

from PYTHON.data import datagame, months

back_btn = html.Div(
    style={"textAlign": "left","display": "flex"},
    children=[
        html.Div(
            style={
                "width": "25px",
                "height": "1px",
            }
        ),
        dcc.Link([
            html.Img(
                src="../assets/IMG/undo-white.svg",
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
        name=game_data["game"],
        line=dict(color='white', shape='spline', smoothing=1.3),
        fill='tonexty',
        fillcolor='rgba(255, 255, 255, 0.2)',
        marker=dict(size=8)
    )
    fig = go.Figure(data=[trace])
    fig.update_layout(
        height=420,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        template='plotly_dark',
        xaxis=dict(
            showgrid=False,
            automargin=True,
            range=[-0.2, len(months)-1]
        )
    )
    return html.Div(
        className="graph-nav",
        children=[
            html.Div(
                children=[
                    dcc.Graph(figure=fig,config={"displayModeBar": False},style={
                            "height": "100%",
                            "transform": "translateY(-10px)"
                        }),

                ],
                style={"background": "linear-gradient(to right, #0c2442, #2a5687)","height": "365px"}
            )
        ],
        style={

        },
    )


navbar = html.Div(
    className="navbar",
    children=[
        back_btn
    ],
    style={
        "position": "absolute",
        "zIndex": 10
    }
)


def showgame(game):
    games = game.split('/')[2]
    return html.Div(
        className=f"{game}_div",
        children=[
            navbar,
            graph_nav(games),
            html.Div(
                style={
                    "width": "25px",
                    "height": "100px",
                }
            )
        ],
        style={
            "background-color":"#f4f3ee"
        }
    )
