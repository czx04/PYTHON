import dash
from dash import dcc, html
from dash.dependencies import Input, Output

from game_layout import showgame

# Khởi tạo ứng dụng Dash
app = dash.Dash(__name__)
app.title = "Dash Multi-Page App"

# define variable
user_counts = 1500
total_games = 24
total_dau = 4080901
average_playtime = 42736
games = ["Valorant", "game 2", "game 3", "game 4", "game 5", "game 6"]

# UI
navbar = html.Div(
    className="navbar",
    children=[
        html.H1("Streaming Dashboard Game", style={"color": "#777777", "margin": 0, "padding-left": "30px"}),
        html.Div(
            className="navbar-icons",
            children=[
                html.Img(
                    src="./assets/IMG/github.png",
                    alt="GitHub",
                    width="24",
                    height="24",
                    style={"cursor": "pointer"},  # Moved cursor styling here
                ),
                html.Img(
                    src="./assets/IMG/info_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg",
                    alt="Info",
                    className="info-icon",
                    width="24",
                    height="24",
                    style={"color": "#777777"},
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
                            src="./assets/IMG/server-svgrepo-com.svg",
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
                                        "margin-bottom": "10px",
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
                            src="./assets/IMG/copy_img.svg",
                            alt="Copy Image",
                            width="26",
                            height="26",
                            style={"cursor": "pointer"},
                        ),
                        html.Img(
                            src="./assets/IMG/question.svg",
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
                            src="./assets/IMG/server-svgrepo-com.svg",
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
                                        "margin-bottom": "10px",
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
                            src="./assets/IMG/copy_img.svg",
                            alt="Copy Image",
                            width="26",
                            height="26",
                            style={"cursor": "pointer"},
                        ),
                        html.Img(
                            src="./assets/IMG/question.svg",
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
                            src="./assets/IMG/server-svgrepo-com.svg",
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
                                        "margin-bottom": "10px",
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
                            src="./assets/IMG/copy_img.svg",
                            alt="Copy Image",
                            width="26",
                            height="26",
                            style={"cursor": "pointer"},
                        ),
                        html.Img(
                            src="./assets/IMG/question.svg",
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
                            src="./assets/IMG/server-svgrepo-com.svg",
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
                                        "margin-bottom": "10px",
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
                            src="./assets/IMG/copy_img.svg",
                            alt="Copy Image",
                            width="26",
                            height="26",
                            style={"cursor": "pointer"},
                        ),
                        html.Img(
                            src="./assets/IMG/question.svg",
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
        "width": "100%",
        "display": "flex",
        "justifyContent": "space-around",
    }
)


def format_game_path(name):
    return name.replace(" ", "").lower()


def get_source_img(game):
    return f"./assets/IMG/{format_game_path(game)}.svg"


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
                                html.P(f"{game}", style={}),
                                html.Img(
                                    src="https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/android-icon.png",
                                    alt="GitHub",
                                    width="32",
                                    height="32",
                                    style={"cursor": "pointer"},
                                )
                            ],
                            style={
                                'display': 'flex',
                                'align-items': 'baseline',
                                'justifyContent': 'space-between',
                                # 'padding-left': '20px',
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
            href=f"/{format_game_path(game)}"
        )
    )

game_list = html.Div(
    children=game_btn,
    style={
        "width": "81%",
        "display": "grid",
        "grid-template-columns": "auto auto auto",
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
    },
    children=[
        navbar,
        from1,
        overViewtotal,
        game_list
    ],

)

app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        html.Div(id="page-content", children=homepage_layout)
    ]
)


@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname"),
)
def display_page(pathname):
    if pathname == "/" or pathname is None:
        return homepage_layout
    else:
        return showgame(pathname)


if __name__ == '__main__':
    app.run_server(debug=True, port=3040)
