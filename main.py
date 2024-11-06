import dash
import plotly.graph_objs as go
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

datagame = [
    {
        "game": "valorant",
        "user_up": {
            "january": "2400",
            "february": "3400",
            "march": "2440",
            "april": "6400",
            "may": "2400",
            "june": "6400",
            "july": "3400",
            "august": "1240",
            "september": "8400",
            "october": "3400",
            "november": "1400",
            "december": "4400",
        }
    },
    {
        "game": "game 2",
        "user_up": {
            "january": "2700",
            "february": "3300",
            "march": "2240",
            "april": "3400",
            "may": "9400",
            "june": "10400",
            "july": "9400",
            "august": "8240",
            "september": "7400",
            "october": "8400",
            "november": "9400",
            "december": "8400",
        }
    },
    {
        "game": "game 3",
        "user_up": {
            "january": "3623",
            "february": "1071",
            "march": "9731",
            "april": "8854",
            "may": "5372",
            "june": "4305",
            "july": "5583",
            "august": "2211",
            "september": "3610",
            "october": "4722",
            "november": "9814",
            "december": "6170",
        }
    },
    {
        "game": "game 4",
        "user_up": {
            "january": "3886",
            "february": "6660",
            "march": "8281",
            "april": "4767",
            "may": "5551",
            "june": "9656",
            "july": "9159",
            "august": "8001",
            "september": "5772",
            "october": "6356",
            "november": "6776",
            "december": "9817",
        }
    },
    {
        "game": "game 5",
        "user_up": {
            "january": "3783",
            "february": "2225",
            "march": "1508",
            "april": "3039",
            "may": "9284",
            "june": "8751",
            "july": "7573",
            "august": "9686",
            "september": "4511",
            "october": "5228",
            "november": "3711",
            "december": "4826",
        }
    },
    {
        "game": "game 6",
        "user_up": {
            "january": "1055",
            "february": "5511",
            "march": "6298",
            "april": "1930",
            "may": "4236",
            "june": "4219",
            "july": "4984",
            "august": "2464",
            "september": "3694",
            "october": "9692",
            "november": "9068",
            "december": "5955",
        }
    },
    {
        "game": "game 7",
        "user_up": {
            "january": "1080",
            "february": "5448",
            "march": "4476",
            "april": "5984",
            "may": "3684",
            "june": "4040",
            "july": "5559",
            "august": "4780",
            "september": "9012",
            "october": "2635",
            "november": "4748",
            "december": "6746",
        }
    },
    {
        "game": "game 8",
        "user_up": {
            "january": "1860",
            "february": "4354",
            "march": "8487",
            "april": "9498",
            "may": "5309",
            "june": "4981",
            "july": "8770",
            "august": "8247",
            "september": "2986",
            "october": "6187",
            "november": "8612",
            "december": "5959",
        }
    },
    {
        "game": "game 9",
        "user_up": {
            "january": "1360",
            "february": "1327",
            "march": "3270",
            "april": "1087",
            "may": "1826",
            "june": "1647",
            "july": "6888",
            "august": "5592",
            "september": "7974",
            "october": "4641",
            "november": "1540",
            "december": "3759",
        }
    }
]

# UI
navbar = html.Div(
    className="navbar",
    children=[
        html.H1("Streaming Dashboard Game", style={"color": "#777777", "margin": 0, "padding-left": "30px"}),
        html.Div(
            className="navbar-icons",
            children=[
                html.Img(
                    src="./assets/IMG/github.svg",
                    alt="GitHub",
                    width="28",
                    height="28",
                    style={"cursor": "pointer"},  # Moved cursor styling here
                ),
                html.Img(
                    src="./assets/IMG/infor.svg",
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

#########################################################################################################
# total overview
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
                            src="./assets/IMG/game_card.svg",
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
                                        "margin-bottom": "10px",
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
                            src="./assets/IMG/dau.svg",
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
                                        "margin-bottom": "10px",
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
                            src="./assets/IMG/time.svg",
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
                                        "margin-bottom": "10px",
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

# define variable for chart overview
gamess = [game["game"] for game in datagame]
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
                                x=gamess,
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
                            width=680,
                            height=450,
                            plot_bgcolor='rgba(0,0,0,0)'
                        )
                    }
                )
            ],
            style={
                "width": "40%",
                "height": "90%",
                "backgroundColor": "#fff",
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
                            width=680,
                            height=450,
                        )
                    }
                )
            ],
            style={
                "width": "40%",
                "height": "90%",
                "backgroundColor": "#fff",
            }
        )

    ],
    style={
        "width": "100%",
        "height": "500px",
        "display": "flex",
        "margin-top": "40px",
        "justifyContent": "space-around",
    }
)


def format_game_path(name):
    return name.replace(" ", "").lower()


def get_source_img(game):
    return f"./assets/IMG/games/{format_game_path(game)}.svg"


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
        chart,
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
