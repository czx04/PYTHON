# game_layout.py
from dash import html


def showgame(game_name):
    return html.Div(
        children=[
            html.H1(f"Dashboard for {game_name}", style={"textAlign": "center"}),
            html.P(f"This is the layout for {game_name}.",
                   style={"textAlign": "center", "fontSize": "18px"}),
            # Add more components specific to each game here
        ],
        style={
            "display": "flex",
            "flex-direction": "column",
            "alignItems": "center",
            "width": "80%",
            "margin": "auto",
            "border": "1px solid #ddd",
            "padding": "20px",
        }
    )
