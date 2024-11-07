# game_layout.py
import plotly.graph_objs as go
from dash import html, dcc
from openpyxl.styles.builtins import title

from PYTHON.data import datagame, months

back_btn = html.Div(
    style={"textAlign": "left"},
    children=[
        dcc.Link([
            html.Img(
                src="../assets/IMG/back_icon.png",
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
        line=dict(color='white', shape='spline', smoothing=1.3),  # Đường vẽ màu trắng
        fill='tonexty',  # Tạo vùng nền mờ dưới đường vẽ
        fillcolor='rgba(255, 255, 255, 0.2)',  # Màu nền mờ (trắng, độ mờ 0.2)
        marker=dict(size=8)
    )
    fig = go.Figure(data=[trace])
    fig.update_layout(
        title={
            'text': 'User Growth Over the Year',
            'x': 0.06,
            'xanchor': 'left',  # Cố định vị trí tiêu đề từ bên trái
            'yanchor': 'top'  # Giữ tiêu đề nằm ở trên
        },
        paper_bgcolor='rgba(0,0,0,0)',  # Làm nền biểu đồ trong suốt để lộ gradient phía sau
        plot_bgcolor='rgba(0,0,0,0)',  # Làm nền khu vực plot trong suốt
        template='plotly_dark'
    )
    return html.Div(
        className="graph-nav",
        children=[
            html.Div(
                children=[
                    dcc.Graph(figure=fig,config={"displayModeBar": False}),

                ],
                style={"padding": "20px","background": "linear-gradient(to right, #0c2442, #2a5687)"}
            )
        ],
        style={},
    )


navbar = html.Div(
    className="navbar",
    children=[
        back_btn
    ],
    style={}
)


def showgame(game):
    games = game.split('/')[2]
    return html.Div(
        className=f"{game}_div",
        children=[
            navbar,
            graph_nav(games)
        ],
        style={

        }
    )
