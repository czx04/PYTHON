# game_layout.py
from dash import html, dcc


def showgame(game_name):
    return html.Div(
        className=f"{game_name}_div",
        children=[
            html.Div(
                style={"textAlign": "center", "padding": "50px"},
                children=[
                    dcc.Link([
                        html.Img(
                            src="./assets/IMG/back_icon.png",
                            alt="Info",
                            className="info-icon",
                            width="24",
                            height="24",
                            style={"cursor": "pointer"},
                        )
                    ], href="/", style={"fontSize": "20px", "color": "blue"}),
                ],
            ),
            html.H1(f"Dashboard for {game_name}", style={"textAlign": "center"}),
            html.P(f"This is the layout for {game_name}.",
                   style={"textAlign": "center", "fontSize": "18px"}),
            # Add more components specific to each game here
            html.Div(
                style={
                    "height": "500px",
                }
            )
        ],
        style={
            "display": "flex",
            "flex-direction": "column",
            "alignItems": "center",
            "justify-content": "left",
            "width": "100%",
            "margin": "auto",
            "border": "1px solid #ddd",
            "padding": "20px",
        }
    )
