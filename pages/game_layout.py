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


def cardbody(gamex):
    game_data = next((game for game in datagame if game["game"].lower().replace(" ", "") == gamex), None)
    if game_data:
        total_users = sum(int(game_data["user_up"][month]) for month in months)
    return (
        html.Div(
        className="card-body",
        children=[
            html.Div(
                children=[
                    html.Div(
                        children=[
                            html.Img(
                                src="../assets/IMG/pages/message.svg",
                                alt="uuser",
                                height="48px",
                                width="48px",
                            ),
                            html.H3(
                                f"{total_users}",
                                style={
                                    "font-size": "24px",
                                    "margin": "10px 0px",
                                    "font-family": "Montserrat,Helvetica Neue,Arial,sans-serif",
                                }
                            ),
                            html.H6(
                                "Message",
                                style={
                                    "font-family": "Montserrat,Helvetica Neue,Arial,sans-serif",
                                    "font-size": "16px",
                                    "margin": "10px 0px",
                                }
                            )
                        ],
                        style={

                        }
                    ),
                    html.Div(
                        style={
                            "width": "1px",
                            "height": "60%",
                            "background-color": "#000",
                        }
                    ),
                    html.Div(
                        children=[
                            html.Img(
                                src="../assets/IMG/pages/money.svg",
                                alt="uuser",
                                height="48px",
                                width="48px",
                            ),
                            html.H3(
                                f"$ {total_users}",
                                style={
                                    "font-size": "24px",
                                    "margin": "10px 0px",
                                    "font-family": "Montserrat,Helvetica Neue,Arial,sans-serif",
                                }
                            ),
                            html.H6(
                                "Today Revenue",
                                style={
                                    "font-family": "Montserrat,Helvetica Neue,Arial,sans-serif",
                                    "font-size": "16px",
                                    "margin": "10px 0px",
                                }
                            )
                        ],
                        style={

                        }
                    ),
                    html.Div(
                        style={
                            "width": "1px",
                            "height": "60%",
                            "background-color": "#000",
                        }
                    ),
                    html.Div(
                        children=[
                            html.Img(
                                src="../assets/IMG/pages/users.svg",
                                alt="uuser",
                                height="48px",
                                width="48px",
                            ),
                            html.H3(
                                f"{total_users}",
                                style={
                                    "font-size": "24px",
                                    "margin": "10px 0px",
                                    "font-family": "Montserrat,Helvetica Neue,Arial,sans-serif",
                                }
                            ),
                            html.H6(
                                "User",
                                style={
                                    "font-family": "Montserrat,Helvetica Neue,Arial,sans-serif",
                                    "font-size": "16px",
                                    "margin": "10px 0px",
                                }
                            )
                        ],
                        style={

                        }
                    ),
                    html.Div(
                        style={
                            "width": "1px",
                            "height": "60%",
                            "background-color": "#000",
                        }
                    ),
                    html.Div(
                        children=[
                            html.Img(
                                src="../assets/IMG/pages/request.svg",
                                alt="uuser",
                                height="48px",
                                width="48px",
                            ),
                            html.H3(
                                f"{total_users}",
                                style={
                                    "font-size": "24px",
                                    "margin": "10px 0px",
                                    "font-family": "Montserrat,Helvetica Neue,Arial,sans-serif",
                                }
                            ),
                            html.H6(
                                "Request",
                                style={
                                    "font-family": "Montserrat,Helvetica Neue,Arial,sans-serif",
                                    "font-size": "16px",
                                    "margin": "10px 0px",
                                }
                            )
                        ],
                        style={

                        }
                    ),
                ],
                style={
                    "width": "90%",
                    "height": "170px",
                    "background-color": "#fff",
                    "text-align": "center",
                    "position": "relative",
                    "top": "-60px",
                    "display": "flex",
                    "flex-direction": "row",
                    "align-items": "center",
                    "justify-content": "space-around",
                }
            )

        ],
        style={
            "width": "100%",
            "display": "flex",
            "flex-direction": "column",
            "align-items": "center",
        }
))

def chart_cont1(gamex):
    chart1 = html.Div(
        className="c1_chart1",
        children=[

        ],
        style={
            "width": "27%",
            "height": "670px",
            "background-color": "#fff",
        }
    )
    chart2 = html.Div(
        className="c1_chart2",
        children=[

        ],
        style={
            "width": "27%",
            "height": "670px",
            "background-color": "#fff",
        }
    )
    chart3 = html.Div(
        className="c1_chart3",
        children=[

        ],
        style={
            "width": "27%",
            "height": "670px",
            "background-color": "#fff",
        }
    )

    return html.Div(
        className="chart1",
        children=[
            chart1,
            chart2,
            chart3,
        ],
        style={
            "width": "100%",
            "display": "flex",
            "align-items": "center",
            "justify-content": "space-around",
        }
    )


def showgame(game_path):
    game = game_path.split('/')[2]
    return html.Div(
        className=f"{game}_div",
        children=[
            navbar,
            graph_nav(game),
            cardbody(game),
            chart_cont1(game)
        ],
        style={
            "background-color":"#f4f3ee",
            "width": "100%",
            "height": "1700px",
        }
    )

