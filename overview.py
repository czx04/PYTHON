import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import pandas as pd
import random
from game_layout import showgame
from dash import callback, Output, Input


# Khởi tạo ứng dụng Dash
app = dash.Dash(__name__)
app.title = "Dash Multi-Page App"

# define variable
user_counts = 1500
total_games = 24
total_dau = 4080901
average_playtime = 42736
games = ["Valorant", "game 2","game 3","game 4","game 5", "game 6","game 7","game 8","game 9"] # Assuming 'games' is your array of game names

## một số hàm
# Hàm để chuyển đổi tên trò chơi sang định dạng không dấu và viết liền
def format_game_name(name):
    return name.replace(" ", "").lower()



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

def getsource(game):
    return f"./assets/IMG/{format_game_name(game)}.svg"
#define game button
game_buttons = []
for game in games:
    chilren_button = [
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.P(f"{game}", style={}),
                        html.Img(
                            src="https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/android-icon.png",
                            alt="GitHub",
                            width="32",
                            height="32",
                            style={"cursor": "pointer"},  # Moved cursor styling here
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
                    src=f"{getsource(game)}",
                    width="52px",
                    height="52px",
                    style={"cursor": "pointer",},

                )

            ],
            style={
                'width': '100%',
            }
        )
    ]
    game_buttons.append(
        html.Button(
            id=f"button-{game}",
            children=chilren_button,
            style={'margin': '10px', 'cursor': 'pointer', 'width': '300px', 'height': '100px'}
        )
    )




all_game = html.Div([
    dcc.Location(id='url', refresh=False),  # Theo dõi URL
    html.Div(game_buttons, style={'display': 'grid','grid-template-columns':'auto auto auto','gap':'10px 32px', 'justify-content': 'center','padding-top':'40px'}),
    html.Div(id='page-content')  # Nội dung của trang sẽ được hiển thị ở đây
])

@app.callback(
    Output('page-content', 'children'),
    [Input(f"button-{game}", 'n_clicks') for game in games]
)
def display_page(*args):
    ctx = dash.callback_context
    if not ctx.triggered:
        return ""

    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    game_name = button_id.split('-')[1].replace("-", " ")  # Lấy tên trò chơi từ id
    return showgame(game_name)

# define layout
app.layout = html.Div(
    children=[navbar, from1, overViewtotalUser,all_game],
    style={
        "display": "flex",
        "flex-direction": "column",
        "alignItems": "center",
    }
)

if __name__ == '__main__':
    app.run_server(debug=True, port=1090)  # Thay đổi port thành 8080