# game_layout.py
from dash import html, dcc



back_btn = html.Div(
                style={"textAlign": "left","padding": "30px 30px" },
                children=[
                    dcc.Link([
                        html.Img(
                            src="../assets/IMG/back_icon.png",
                            alt="Info",
                            className="info-icon",
                            width="24",
                            height="24",
                            style={"cursor": "pointer"},
                        )
                    ], href="/", style={"fontSize": "20px", "color": "blue"}),
                ],
            )

def notfound(game):
    return html.Div(
        className=f"{game}_div",
        children=[
            back_btn,
            html.H1(f"Đéo có gì ở đây", style={"textAlign": "center"}),
        ],
        style={
        }
    )

