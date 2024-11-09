# game_layout.py
import plotly.graph_objs as go
from dash import html, dcc
import plotly.express as px
import pandas as pd


from PYTHON.data import datagame, months


# format
def convert_game_name(gamex):
    return gamex.lower().replace(' ', '')


# UI
back_btn = html.Div(
    style={"textAlign": "left", "display": "flex"},
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
    game_data = next((game for game in datagame if game["game"].lower().replace(" ", "") == game_path), None)
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
            range=[-0.2, len(months) - 1]
        )
    )
    return html.Div(
        className="graph-nav",
        children=[
            html.Div(
                children=[
                    dcc.Graph(figure=fig, config={"displayModeBar": False}, style={
                        "height": "100%",
                        "transform": "translateY(-10px)"
                    }),

                ],
                style={"background": "linear-gradient(to right, #0c2442, #2a5687)", "height": "365px"}
            )
        ],
        style={

        },
    )


def cardbody(gamex):
    game_data = next((game for game in datagame if game["game"].lower().replace(" ", "") == gamex), None)
    total_users = sum(int(game_data["user_up"][month]) for month in months)
    return (
        html.Div(
            className="card-body",
            children=[
                html.Div(
                    children=[
                        html.Div(
                            style={
                                "width": "5px",
                            }
                        ),
                        html.Div(
                            children=[
                                html.Img(
                                    src="../assets/IMG/pages/message.svg",
                                    alt="uuser",
                                    height="48px",
                                    width="48px",
                                ),
                                html.H3(
                                    f"{total_users:,}",
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
                                        "opacity": "0.4",
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
                                        "opacity": "0.4",
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
                                        "opacity": "0.4",
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
                                        "opacity": "0.4",
                                    }
                                )
                            ],
                            style={

                            }
                        ),
                        html.Div(
                            style={
                                "width": "5px",
                            }
                        )
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
                        "justify-content": "space-between",
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


class chart_ctn1:
    def drchart1(self, gamex):
        game_data = next((game for game in datagame if convert_game_name(game["game"]) == convert_game_name(gamex)),
                         None)
        avg_daily_active_user = [int(game_data["avg_daily_active_user"].get(month, 0)) for month in months]
        trace = go.Scatter(
            x=months,
            y=avg_daily_active_user,
            mode='lines+markers',
            name=game_data["game"],
            line=dict(color='#f96b3d', shape='spline', smoothing=1.3),
            fill='tonexty',
            fillcolor='rgba(254, 193, 178, 0.102)',  # Màu bắt đầu với độ trong suốt
            marker=dict(size=8)
        )
        fig = go.Figure(data=[trace])
        fig.update_layout(
            height=420,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            template='plotly_dark',
            margin=dict(l=0, r=0, t=0, b=0),  # Remove chart margins
            xaxis=dict(
                showgrid=False,
                showline=False,
                visible=False
            ),
            yaxis=dict(
                showgrid=False,
                showline=False,
                visible=False
            )
        )
        return html.Div(
            className="graph-nav",
            children=[
                html.Div(
                    children=[
                        dcc.Graph(
                            figure=fig,
                            config={"displayModeBar": False},
                            style={
                                "height": "100%",
                                "width": "100%",  # Ensure full width of container
                                "transform": "translateY(-10px)",
                            }
                        ),
                    ],
                    style={
                        "background": "rgba(0,0,0,0)",
                        "height": "365px",
                        "width": "100%"  # Ensure parent div also takes full width
                    }
                )
            ],
            style={
                "width": "100%",  # Ensure this div stretches fully
            },
        )

    def footer_chart1(self, gamex):
        game_data = next((game_data for game_data in datagame if game_data["game"].lower() == gamex.lower()), None)
        if not game_data:
            return html.Div("Game data not found.")

        # Lấy dữ liệu active_user/country và sắp xếp theo số lượng người dùng giảm dần
        country_data = game_data["active_user/country"]
        sorted_countries = sorted(country_data.items(), key=lambda x: int(x[1]), reverse=True)[:6]

        # Tính tổng số lượng active_user
        total_users = sum(int(value) for value in country_data.values())

        # Tạo các thẻ div cho mỗi quốc gia
        country_divs = []
        for country, users in sorted_countries:
            percentage = (int(users) / total_users) * 100
            country_divs.append(
                html.Div(
                    children=[
                        html.Div(
                            className="country-stat",
                            children=[
                                html.Img(
                                    src=f"../assets/IMG/country/{convert_game_name(country)}.svg",  # Đường dẫn tới cờ
                                    alt=f"{country} flag",
                                    height="24px",
                                    width="36px",
                                    style={"marginRight": "10px"}
                                ),
                                html.Span(f"{country}",
                                          style={"fontWeight": "bold", "marginRight": "10px", "display": "inline-block",
                                                 "width": "100px",
                                                 "font-family": "Montserrat,Helvetica Neue,Arial,sans-serif"}),
                                html.Span(f"{int(users):,}",
                                          style={"marginRight": "10px", "display": "inline-block", "width": "150px",
                                                 "font-family": "Montserrat,Helvetica Neue,Arial,sans-serif"}),
                                html.Span(f"{percentage:.2f}%",
                                          style={"display": "inline-block", "width": "100px",
                                                 "font-family": "Montserrat,Helvetica Neue,Arial,sans-serif"})
                            ],
                            style={
                                "display": "flex",
                                "alignItems": "center",
                                "marginBottom": "8px",
                                "paddingTop": "18px",
                                "paddingBottom": "8px",
                            }
                        ),
                        html.Div(
                            style={
                                "width": "80%",
                                "height": "1px",
                                "background-color": "#e9ecef",
                            }
                        )
                    ],
                    style={
                        "display": "flex",
                        "flex-direction": "column",
                        "alignItems": "center",
                    }
                )
            )

        return html.Div(
            children=country_divs,
            style={
                "width": "100%"
            }
        )

    def drchart3(self, gamex):
        game_data = next((game for game in datagame if convert_game_name(game["game"]) == gamex), None)
        if game_data:
            users_country = game_data["users/country"]
            countries = list(users_country.keys())
            user_counts = [int(value) for value in users_country.values()]

            # Create a bar chart using Plotly
            trace = go.Bar(
                x=countries,
                y=user_counts,
                marker=dict(color='rgba(54, 162, 235, 0.6)', line=dict(color='rgba(54, 162, 235, 1.0)', width=1)),
                text=[f"{count:,}" for count in user_counts],
                textposition='auto'
            )

            fig = go.Figure(data=[trace])
            fig.update_layout(
                height=365,  # Adjust height to fit better within the container
                margin=dict(l=20, r=20, t=40, b=40),  # Adjust margins for better fit
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)'
            )

            # Create an HTML component with the chart
            return html.Div(
                children=[
                    dcc.Graph(figure=fig, style={"height": "100%", "width": "100%"})
                    # Ensure the graph scales within the div
                ],
                style={"width": "100%", "display": "flex", "justify-content": "center"}
            )

    def footer_chart3(self, gamex):
        game_data = next((game for game in datagame if convert_game_name(game["game"]) == gamex.lower()), None)

        users_country = game_data.get("active_user/country", {})
        country = list(users_country.keys())
        value = [int(users_country[country_name]) for country_name in country]
        data = {
            'country': country,
            'value': value
        }
        df = pd.DataFrame(data)
        df['value'] = df['value'].astype(str)
        fig = px.choropleth(
            df,
            locations="country",
            locationmode="country names",
            color="value",
            hover_name="country",
            color_discrete_map={
                '1': "#e7e7e7",  # Màu cho giá trị '1'
                '2': "#8e8e8e",  # Màu cho giá trị '2'
                '3': "#565656",  # Màu cho giá trị '3'
                '4': "#000000"  # Màu cho giá trị '4'
            }
        )
        fig.update_layout(coloraxis_showscale=False)
        return html.Div([
            dcc.Graph(figure=fig)
        ])

    def draw_chart(self, gamex):
        total_active_user = 0
        country_count = 0
        for game in datagame:
            country_count = len(game['active_user/country'])
            if convert_game_name(game['game']) == gamex.lower():
                avg_daily_active_user = game['avg_daily_active_user']
                total_active_user = sum(int(value) for value in avg_daily_active_user.values())
        chart1 = html.Div(
            className="c1_chart1",
            children=[
                html.Div(
                    children=[
                        html.P("Active User",
                               style={"font-size": "18px", "font-family": "Montserrat,Helvetica Neue,Arial,sans-serif",
                                      "margin": "2px 0", "opacity": "0.4"}),
                        html.P(f"{total_active_user:,}",
                               style={"font-size": "40px", "font-family": "Helvetica Neue", "margin": "0px"})
                    ],
                    style={
                        "margin": "0px 30px",
                        "marginTop": "25px",
                    }
                ),
                self.drchart1(gamex),
                html.Div(
                    style={
                        "width": "100%",
                        "height": "20px",
                    }
                ),
                self.footer_chart1(gamex),
                html.Div(
                    style={
                        "width": "100%",
                        "height": "70px",
                    }
                )

            ],
            style={
                "width": "27%",
                "background-color": "#fff",
            }
        )
        chart2 = html.Div(
            className="c1_chart2",
            children=[
                html.Div(
                    children=[
                        html.P("Active User",
                               style={"font-size": "18px", "font-family": "Montserrat,Helvetica Neue,Arial,sans-serif",
                                      "margin": "2px 0", "opacity": "0.4"}),
                        html.P(f"{total_active_user:,}",
                               style={"font-size": "40px", "font-family": "Helvetica Neue", "margin": "0px"})
                    ],
                    style={
                        "margin": "0px 30px",
                        "marginTop": "25px",
                    }
                )
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
                html.Div(
                    children=[
                        html.P("Active Country",
                               style={"font-size": "18px", "font-family": "Montserrat,Helvetica Neue,Arial,sans-serif",
                                      "margin": "2px 0", "opacity": "0.4"}),
                        html.P(f"{country_count:,}",
                               style={"font-size": "40px", "font-family": "Helvetica Neue", "margin": "0px"})
                    ],
                    style={
                        "margin": "0px 30px",
                        "marginTop": "25px",
                    }
                ),
                self.drchart3(gamex),
                self.footer_chart3(gamex),
            ],
            style={
                "width": "27%",
                "height": "870px",
                "background-color": "#fff",
                "padding": "10px",  # Add padding for better spacing
                "box-sizing": "border-box"  # Ensure padding does not exceed the container size
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

                "display": "flex",
                "align-items": "stretch",
                "justify-content": "space-around",
            }
        )


def showgame(game_path):
    game = game_path.split('/')[-1]  # Adjusted to safely extract the game name from the path
    return html.Div(
        className=f"{game}_div",
        children=[
            navbar,
            graph_nav(game),
            cardbody(game),
            chart_ctn1().draw_chart(game)  # Proper instantiation of class if not static
        ],
        style={
            "background-color": "#f4f3ee",
            "width": "100%",
            "height": "1700px",
        }
    )

# huhu
