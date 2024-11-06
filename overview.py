import dash
from dash import dcc, html, dash_table
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
games = ["Valorant", "game 2","game 3","game 4","game 5","game 6"]

#UI
navbar = html.Div(
    className="navbar",
    children=[
        html.H1("Streaming Dashboard Game", style={"color": "white", "margin": 0, "padding-left": "30px"}),
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
        "backgroundColor": "#1e1e1e",
        "width": "100%",
        "padding": "20px 0",
    }
)
from1 = html.Div(
    className="data-from",
    children=[
        html.P("Data for this app is pulled from the FK company API. Updated 2024-10-18",
               style={"textAlign": "right", "padding-right": "40px", "padding-left": "100px"}, )
    ],
    style={
        "width": "100%",
        "padding-bottom": "25px",
    }
)
overViewtotalUser = html.Div(
    className="overview-totaluser",
    children=[
        html.Div(
            className="view_cont",
            children=[
                html.P(f"{user_counts}", style={
                            "textAlign": "left",
                            "font-family": "Roboto",
                            "font-weight": "700",
                            "font-size": "38px",
                            "margin-top": "8px",
                            "margin-bottom": "8px",
                            "margin-left": "20px"
                }),
                html.P("TOTAL USERS", style={
                            "textAlign": "left",
                            "font-family": "Roboto",
                            "font-size": "14px",
                            "font-weight": "700",
                            "margin-bottom": "8px",
                            "margin-left": "20px"
                })
            ],
            style={
                "width": "20%",
                "height": "100px",
                "border": "1px solid black",
                "background-color": "#fff",
            }
        ),
html.Div(
            className="view_cont",
            children=[
                html.P(f"{total_games}", style={
                            "textAlign": "left",
                            "font-family": "Roboto",
                            "font-weight": "700",
                            "font-size": "38px",
                            "margin-top": "8px",
                            "margin-bottom": "8px",
                            "margin-left": "20px"
                }),
                html.P("TOTAL GAMES", style={
                            "textAlign": "left",
                            "font-family": "Roboto",
                            "font-size": "14px",
                            "font-weight": "700",
                            "margin-bottom": "8px",
                            "margin-left": "20px"
                })
            ],
            style={
                "width": "20%",
                "height": "100px",
                "border": "1px solid black",
"background-color": "#fff",
            }
        ),
html.Div(
            className="view_cont",
            children=[
                html.P(f"{total_dau}", style={
                            "textAlign": "left",
                            "font-family": "Roboto",
                            "font-weight": "700",
                            "font-size": "38px",
                            "margin-top": "8px",
                            "margin-bottom": "8px",
                            "margin-left": "20px"
                }),
                html.P("TOTAL DAU", style={
                            "textAlign": "left",
                            "font-family": "Roboto",
                            "font-size": "14px",
                            "font-weight": "700",
                            "margin-bottom": "8px",
                            "margin-left": "20px"
                })
            ],
            style={
                "width": "20%",
                "height": "100px",
                "border": "1px solid black",
"background-color": "#fff",
            }
        ),
html.Div(
            className="view_cont",
            children=[
                html.P(f"{average_playtime}", style={
                            "textAlign": "left",
                            "font-family": "Roboto",
                            "font-weight": "700",
                            "font-size": "38px",
                            "margin-top": "8px",
                            "margin-bottom": "8px",
                            "margin-left": "20px"
                }),
                html.P("AVERAGE PLAYTIME", style={
                            "textAlign": "left",
                            "font-family": "Roboto",
                            "font-size": "14px",
                            "font-weight": "700",
                            "margin-bottom": "8px",
                            "margin-left": "20px"
                })
            ],
            style={
                "width": "20%",
                "height": "100px",
                "border": "1px solid black",
                "background-color": "#fff",
            }
        ),
    ],
    style={
        "display": "flex",
        "flex-direction": "row",
        "justifyContent": "space-between",
        "width": "81%",
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
            children= game_btn,
            style = {
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
        "background-color": "#f3f4f8",
    },
    children=[
        navbar,
        from1,
        overViewtotalUser,
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
