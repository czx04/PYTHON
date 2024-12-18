import plotly.graph_objs as go
from dash import dcc, html
from PYTHON.data.data import datagame, user_counts, total_games, total_dau, average_playtime

navbar = html.Div(
    className="navbar",
    children=[
        html.H1("Streaming Dashboard Game", style={"color": "#777777", "margin": 0, "padding-left": "30px"}),
        html.Div(
            className="navbar-icons",
            children=[
                html.Img(
                    src="assets/IMG/others/github.svg",
                    alt="GitHub",
                    width="28",
                    height="28",
                    style={"cursor": "pointer"},  # Moved cursor styling here
                ),
                html.Img(
                    src="assets/IMG/others/infor.svg",
                    alt="Info",
                    className="info-icon",
                    width="24",
                    height="24",
                    style={"cursor": "pointer"},
                ),
            ],
            style={"display": "flex", "justify-content": "center", "align-items": "center", "gap": "10px",
                   "padding-right": "30px"},
        ),
    ],
    style={
        "display": "flex",
        "flex-direction": "row",
        "justifyContent": "space-between",
        "alignItems": "center",
        "backgroundColor": "#f4f3ee",
        "width": "100%",
        "padding": "20px 0",
    }
)
from1 = html.Div(
    className="data-from",
    children=[
        html.P("Data for this app is pulled from the FK company API. Updated 2024-10-18",
               style={"textAlign": "right", "padding-right": "40px", "padding-left": "100px", "color": "#777777"}, )
    ],
    style={
        "width": "100%",
        "padding-bottom": "25px",
        "border-top": "1px solid #777777",
    }
)

overViewtotal = html.Div(
    className="overview-total",
    children=[
        html.Div(
            className="ot",
            children=[
                html.Div(
                    className="ot_nav",
                    children=[
                        html.Img(
                            src="assets/IMG/others/server-svgrepo-com.svg",
                            alt="Server SVG",
                            width="60",
                            height="60",
                            style={"padding-top": "10px",
                                   "padding-right": "10px", },
                        ),
                        html.Div(
                            className="ot",
                            children=[
                                html.P(
                                    f"Total user",
                                    style={
                                        "font-size": "20px",
                                        "margin-top": "5px",
                                        "margin-bottom": "5px",
                                        "font-color": "#3a3937",
                                    },
                                ),
                                html.P(
                                    f"{user_counts}",
                                    style={
                                        "font-color": "#000",
                                        "font-size": "32px",
                                        "margin": "0px",
                                        "padding-left": "10px",
                                    },
                                )
                            ],
                            style={
                            }
                        )
                    ],
                    style={
                        "display": "flex",
                        # "alignItems": "center",
                        "justifyContent": "space-around",
                        "border-bottom": "1px solid #f8f4ef",
                    }
                ),
                html.Div(
                    className="ot_footer",
                    children=[
                        html.Img(
                            src="assets/IMG/others/copy_img.svg",
                            alt="Copy Image",
                            width="26",
                            height="26",
                            style={"cursor": "pointer"},
                        ),
                        html.Img(
                            src="assets/IMG/others/question.svg",
                            alt="Copy Image",
                            width="26",
                            height="26",
                            style={"cursor": "pointer", "opacity": "0.3"},
                        )

                    ],
                    style={
                        "display": "flex",
                        "flex-direction": "row",
                        "justifyContent": "space-between",
                        "alignItems": "center",
                        "margin": "10px 20px",
                    }
                )
            ],
            style={
                "height": "120px",
                "width": "255px",
                "backgroundColor": "#ffffff",
            }

        ),
        html.Div(
            className="ot",
            children=[
                html.Div(
                    className="ot_nav",
                    children=[
                        html.Img(
                            src="assets/IMG/others/game_card.svg",
                            alt="Server SVG",
                            width="60",
                            height="60",
                            style={"padding-top": "10px",
                                   "padding-right": "10px", },
                        ),
                        html.Div(
                            className="ot",
                            children=[
                                html.P(
                                    f"Game",
                                    style={
                                        "font-size": "20px",
                                        "margin-top": "5px",
                                        "margin-bottom": "5px",
                                        "font-color": "#3a3937",
                                    },
                                ),
                                html.P(
                                    f"{total_games}",
                                    style={
                                        "font-color": "#000",
                                        "font-size": "32px",
                                        "margin": "0px",
                                        "padding-left": "10px",
                                    },
                                )
                            ],
                            style={
                            }
                        )
                    ],
                    style={
                        "display": "flex",
                        # "alignItems": "center",
                        "justifyContent": "space-around",
                        "border-bottom": "1px solid #f8f4ef",
                    }
                ),
                html.Div(
                    className="ot_footer",
                    children=[
                        html.Img(
                            src="assets/IMG/others/copy_img.svg",
                            alt="Copy Image",
                            width="26",
                            height="26",
                            style={"cursor": "pointer"},
                        ),
                        html.Img(
                            src="assets/IMG/others/question.svg",
                            alt="Copy Image",
                            width="26",
                            height="26",
                            style={"cursor": "pointer", "opacity": "0.3"},
                        )

                    ],
                    style={
                        "display": "flex",
                        "flex-direction": "row",
                        "justifyContent": "space-between",
                        "alignItems": "center",
                        "margin": "10px 20px",
                    }
                )
            ],
            style={
                "height": "120px",
                "width": "255px",
                "backgroundColor": "#ffffff",
            }

        ),
        html.Div(
            className="ot",
            children=[
                html.Div(
                    className="ot_nav",
                    children=[
                        html.Img(
                            src="assets/IMG/others/dau.svg",
                            alt="Server SVG",
                            width="60",
                            height="60",
                            style={"padding-top": "10px",
                                   "padding-right": "10px", },
                        ),
                        html.Div(
                            className="ot",
                            children=[
                                html.P(
                                    f"DAU",
                                    style={
                                        "font-size": "20px",
                                        "margin-top": "5px",
                                        "margin-bottom": "5px",
                                        "font-color": "#3a3937",
                                    },
                                ),
                                html.P(
                                    f"{total_dau}",
                                    style={
                                        "font-color": "#000",
                                        "font-size": "32px",
                                        "margin": "0px",
                                        "padding-left": "10px",
                                    },
                                )
                            ],
                            style={
                            }
                        )
                    ],
                    style={
                        "display": "flex",
                        # "alignItems": "center",
                        "justifyContent": "space-around",
                        "border-bottom": "1px solid #f8f4ef",
                    }
                ),
                html.Div(
                    className="ot_footer",
                    children=[
                        html.Img(
                            src="assets/IMG/others/copy_img.svg",
                            alt="Copy Image",
                            width="26",
                            height="26",
                            style={"cursor": "pointer"},
                        ),
                        html.Img(
                            src="assets/IMG/others/question.svg",
                            alt="Copy Image",
                            width="26",
                            height="26",
                            style={"cursor": "pointer", "opacity": "0.3"},
                        )

                    ],
                    style={
                        "display": "flex",
                        "flex-direction": "row",
                        "justifyContent": "space-between",
                        "alignItems": "center",
                        "margin": "10px 20px",
                    }
                )
            ],
            style={
                "height": "120px",
                "width": "255px",
                "backgroundColor": "#ffffff",
            }

        ),
        html.Div(
            className="ot",
            children=[
                html.Div(
                    className="ot_nav",
                    children=[
                        html.Img(
                            src="assets/IMG/others/time.svg",
                            alt="Server SVG",
                            width="60",
                            height="60",
                            style={"padding-top": "10px",
                                   "padding-right": "10px", },
                        ),
                        html.Div(
                            className="ot",
                            children=[
                                html.P(
                                    f"Average Play Time",
                                    style={
                                        "font-size": "20px",
                                        "margin-top": "5px",
                                        "margin-bottom": "5px",
                                        "font-color": "#3a3937",
                                    },
                                ),
                                html.P(
                                    f"{average_playtime}",
                                    style={
                                        "font-color": "#000",
                                        "font-size": "32px",
                                        "margin": "0px",
                                        "padding-left": "10px",
                                    },
                                )
                            ],
                            style={
                            }
                        )
                    ],
                    style={
                        "display": "flex",
                        # "alignItems": "center",
                        "justifyContent": "space-around",
                        "border-bottom": "1px solid #f8f4ef",
                    }
                ),
                html.Div(
                    className="ot_footer",
                    children=[
                        html.Img(
                            src="assets/IMG/others/copy_img.svg",
                            alt="Copy Image",
                            width="26",
                            height="26",
                            style={"cursor": "pointer"},
                        ),
                        html.Img(
                            src="assets/IMG/others/question.svg",
                            alt="Copy Image",
                            width="26",
                            height="26",
                            style={"cursor": "pointer", "opacity": "0.3"},
                        )

                    ],
                    style={
                        "display": "flex",
                        "flex-direction": "row",
                        "justifyContent": "space-between",
                        "alignItems": "center",
                        "margin": "10px 20px",
                    }
                )
            ],
            style={
                "height": "120px",
                "width": "255px",
                "backgroundColor": "#ffffff",
            }

        )
    ],
    style={
        "width": "90%",
        "display": "flex",
        "justifyContent": "space-between",
    }
)

# define variable for chart overview
games = [game["game"] for game in datagame]
total_userss = [sum(int(user) for user in game["user_up"].values()) for game in datagame]
months = list(datagame[0]["user_up"].keys())
games_data = []
for game_info in datagame:
    game_name = game_info["game"]
    user_counts = [int(game_info["user_up"][month]) for month in months]
    games_data.append({"game": game_name, "user_counts": user_counts})

#################################################################################################################
# chart overview
chart = html.Div(
    className="chart",
    children=[
        html.Div(
            className="char_1",
            children=[
                dcc.Graph(
                    id="bar-chart",
                    figure={
                        "data": [
                            go.Bar(
                                x=games,
                                y=total_userss,
                                text=total_userss,
                                textposition='auto',
                                marker=dict(color='#f29a42')
                            )
                        ],
                        "layout": go.Layout(
                            title='Tổng số người dùng của các game',
                            xaxis=dict(title='Game'),
                            yaxis=dict(title='Tổng số người dùng'),
                            height=450,
                            plot_bgcolor='rgba(0,0,0,0)'
                        )
                    }
                )
            ],
            style={
                "flex": "1",
                "height": "100%",
                "backgroundColor": "#fff",
                "margin": "10px"
            }
        ),
        html.Div(
            className="char_2",
            children=[
                dcc.Graph(
                    id="line-chart",
                    figure={
                        "data": [
                            go.Scatter(
                                x=months,
                                y=game["user_counts"],
                                mode="lines+markers",
                                name=game["game"]
                            ) for game in games_data
                        ],
                        "layout": go.Layout(
                            title="User Growth by Game and Month",
                            xaxis={"title": "Month"},
                            yaxis={"title": "User Increase"},
                            height=450,
                        )
                    }
                )
            ],
            style={
                "flex": "1",
                "height": "100%",
                "backgroundColor": "#fff",
                "margin": "10px"
            }
        )

    ],
    style={
        "width": "90%",
        "display": "flex",
        "margin-top": "40px",
        "justifyContent": "space-between",
        "alignItems": "center"
    }
)


def format_game_path(name):
    return name.replace(" ", "").lower()


def get_source_img(game):
    return f"./assets/IMG/games/{format_game_path(game)}/logo.jpg"


def get_platform_images(game_name):
    # Find the game in the datagame list
    platforms = []
    for game in datagame:
        if game["game"] == game_name:
            platforms = game["platform"]
            break
    platform_images = []
    for platform in platforms:
        platform_images.append(
            html.Img(
                src=f"./assets/IMG/platforms/{platform}.svg",
                alt=platform,
                width="24",
                height="24",
                style={"cursor": "pointer", "margin-right": "5px"}
            )
        )
    return platform_images


game_f = html.Div(
    className="game_f",
    children=[
        html.Div(
            className="game_fff",
            style={"height": "1px", "width": "100px"},
        ),
        html.P("GAME LIST",
               style={"font-size": "25px", "font-family": "Montserrat, Helvetica Neue, Arial, sans-serif"}),

    ],
    style={
        "width": "100%",
        "display": "flex",
        "justifyContent": "start",
    }
)

game_btn = []
for game in games:
    game_btn.append(
        dcc.Link(
            [
                html.Div(
                    className="chilren-btn",
                    children=[
                        html.Div(
                            children=[
                                html.P(f"{game}", style={
                                    'padding-right': '60px',
                                    'padding-bottom': '5px',
                                    'font-size': '20px',
                                    'font-weight': 'bold',
                                    'color': '#777777',
                                    "font-family": "Montserrat, Helvetica Neue, Arial, sans-serif"
                                }),
                                html.Div(
                                    children=get_platform_images(game),
                                    style={
                                        "position": "relative",
                                        "top": "-5"
                                    }
                                )
                            ],
                            style={
                                'display': 'flex',
                                'justifyContent': 'space-between',
                                'width': '100%',
                            }
                        ),
                        html.Img(
                            src=f"{get_source_img(game)}",
                            width="52px",
                            height="52px",
                            style={"cursor": "pointer", },

                        )
                    ],
                    style={
                        'width': '100%',
                    }
                )
            ],
            href=f"/games/{format_game_path(game)}",
            style={
                'textDecoration': 'none',  # Remove underline for link
                ':hover': {
                    'textDecoration': 'underline'  # Add underline on hover
                },
                ':visited': {
                    'textDecoration': 'none'  # Ensure visited links have no underline
                },
                ':active': {
                    'textDecoration': 'underline'  # Add underline on active
                }
            }
        )
    )
game_list = html.Div(
    children=game_btn,
    style={
        "width": "55%",
        "display": "grid",
        "grid-template-columns": "auto auto auto",
        "row-gap": "50px",
        "align-items": "center",
        "justifyContent": "space-between",
    }
)

homepage_layout = html.Div(
    style={
        "display": "flex",
        "flex-direction": "column",
        "alignItems": "center",
        "background-color": "#f4f3ee",
        "padding-bottom": "150px",
    },
    children=[
        navbar,
        from1,
        overViewtotal,
        chart,
        game_f,
        game_list
    ],
)
