# game_layout.py
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from dash import html, dcc

from PYTHON.data.data import datagame, months

# format
def convert_game_name(gamex):
    return gamex.lower().replace(' ', '')

class navbar:
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
                    src="../assets/IMG/others/undo-white.svg",
                    alt="Info",
                    className="info-icon",
                    width="24",
                    height="24",
                    style={"cursor": "pointer", "padding": "30px 30px"},
                )
            ], href="/", style={"fontSize": "20px", "color": "blue"}),
        ],
    )
    navbarx = html.Div(
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

    def card(gamex):
        game_data = next((game for game in datagame if game["game"].lower().replace(" ", "") == gamex), None)
        total_users = sum(int(game_data["user_up"][month]) for month in months)
        req = game_data.get("request")
        today_revenue = game_data.get("today_revenue")
        return (
            html.Div(
                className="card",
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
                                        alt="user",
                                        height="48px",
                                        width="48px",
                                    ),
                                    html.H3(
                                        f"{total_users//40:,}",
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
                                        f"$ {today_revenue}",
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
                                        f"{req}",
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
                visible=False,
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
        game_data = next((game for game in datagame if convert_game_name(game["game"]) == convert_game_name(gamex)),
                         None)
        if not game_data:
            return html.Div("Game data not found.")

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
                "width": "100%",
                "margin": "0 auto",
                "padding": "10px",
                "box-sizing": "border-box"
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
                    dcc.Graph(figure=fig, config={"displayModeBar": False}, style={"height": "100%", "width": "100%"})
                    # Ensure the graph scales within the div
                ],
                style={"width": "100%", "display": "flex", "justify-content": "center"}
            )

    def footer_chart3(self, gamex):
        game_data = next((game for game in datagame if convert_game_name(game["game"]) == gamex.lower()), None)
        if not game_data:
            return html.Div("No data available for this game.")

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
                '1': "#e7e7e7",
                '2': "#e7e7e7",
                '3': "#8e8e8e",
                '4': "#8e8e8e",
                '5': "#8e8e8e",
                '6': "#565656",
                '7': "#565656",
                '8': "#565656",
                '9': "#565656",
                '10': "#000000"
            }
        )
        fig.update_layout(
            coloraxis_showscale=False,
            showlegend=False,
            margin=dict(l=0, r=0, t=0, b=0),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )

        return html.Div(
            children=[
                dcc.Graph(
                    figure=fig,
                    config={"displayModeBar": False},
                    style={"width": "100%", "height": "100%"}
                )
            ],
            style={"width": "100%", "height": "100%"}
        )

    def show(self, gamex):
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
                "width": "48%",
                "background-color": "#fff",
            }
        )
        chart3 = html.Div(
            className="c1_chart3",
            children=[
                html.Div(
                    children=[
                        html.P("Active Country",
                               style={
                                   "font-size": "18px",
                                   "font-family": "Montserrat,Helvetica Neue,Arial,sans-serif",
                                   "margin": "2px 0",
                                   "opacity": "0.4"
                               }),
                        html.P(f"{country_count:,}",
                               style={
                                   "font-size": "40px",
                                   "font-family": "Helvetica Neue",
                                   "margin": "0px"
                               })
                    ],
                    style={
                        "margin": "0px 30px",
                        "width": "27%",
                        "marginTop": "25px",
                    }
                ),
                self.drchart3(gamex),
                self.footer_chart3(gamex),
            ],
            style={
                "width": "48%",
                "height": "100%",
                "background-color": "#fff",
                "padding": "10px",
                "box-sizing": "border-box",
                "display": "flex",
                "flex-direction": "column",
                "justify-content": "space-between"
            }
        )

        return html.Div(
            className="chart1",
            children=[
                html.Div(
                    children=[
                        chart1,
                        chart3,
                    ],
                    style={
                        "width": "90%",
                        "display": "flex",
                        "align-items": "stretch",
                        "justify-content": "space-between",
                    }
                )
            ],
            style={
                "width": "100%",
                "justify-content": "center",
                "display": "flex",
                "margin": "auto",
            }
        )

class chart_ctn2:
    def show(self, game):
        # game_data = next((g for g in datagame if g["game"].lower() == game.lower()), None)
        game_data = next((g for g in datagame if convert_game_name(g["game"]) == convert_game_name(game)), None)
        if not game_data:
            return html.Div("Game not found.")

        selling_products = game_data.get("selling_product", [])
        products = game_data.get("products", [])
        product_details = [prod for prod in products if prod["prd"] in selling_products]

        table_rows = []
        for product in product_details:
            price = int(product["price"])
            sales_volume = int(product["sales volume"])
            total = price * sales_volume
            table_rows.append(
                html.Div(
                    className="data-row",
                    children=[
                        html.Img(src=f"../assets/IMG/games/{game}/products/{product['prd'].lower()}.jpg",
                                 style={"width": "30px", "flex": "0.5"}, ),
                        html.Div("", style={"flex": "1"}),
                        html.Div(
                            children=[
                                html.Span(product["prd"], style={"margin-left": "10px",
                                                                 "font-family": "Montserrat, Helvetica Neue, Arial, sans-serif",
                                                                 "font-size": "18px"})
                            ],
                            style={"display": "flex", "align-items": "center", "flex": "2"}
                        ),
                        html.Div(
                            children=[
                                html.Div(f"${price:,}",
                                         style={"font-family": "Montserrat, Helvetica Neue, Arial, sans-serif",
                                                "font-size": "18px"}),
                            ],
                            style={"display": "flex", "align-items": "center", "flex": "1"}
                        ), html.Div(
                            children=[
                                html.Div(product["tier"],
                                         style={"font-family": "Montserrat, Helvetica Neue, Arial, sans-serif",
                                                "font-size": "18px"}),
                            ],
                            style={"display": "flex", "align-items": "center", "flex": "1"}
                        ), html.Div(
                            children=[
                                html.Div(f"{sales_volume:,}",
                                         style={"font-family": "Montserrat, Helvetica Neue, Arial, sans-serif",
                                                "font-size": "18px"}),
                            ],
                            style={"display": "flex", "align-items": "center", "flex": "1"}
                        ),
                        html.Div(
                            children=[
                                html.Div(f"{total:,}",
                                         style={"font-family": "Montserrat, Helvetica Neue, Arial, sans-serif",
                                                "font-size": "18px"}),
                            ],
                            style={"display": "flex", "align-items": "center", "flex": "0.95"}
                        ),
                    ],
                    style={
                        "display": "flex",
                        "padding": "10px 30px",
                        "border": "none"
                    }
                )
            )
        total_sum = sum(int(prod["price"]) * int(prod["sales volume"]) for prod in product_details)
        total_row = html.Div(
            className="total-row",
            children=[
                html.Div(f"Total:   ${total_sum:,}",
                         style={"flex": "0.912", "font-weight": "bold", "text-align": "right",
                                "font-family": "Montserrat, Helvetica Neue, Arial, sans-serif", "font-size": "20px"}),
            ],
            style={
                "display": "flex",
                "padding": "10px 30px",
                "margin-top": "10px"
            }
        )

        return html.Div(
            children=[
                html.Div(
                    children=[
                        html.P(
                            "Best Selling Products",
                            style={"font-size": "24px", "padding-left": "30px", "opacity": "0.9", "color": "#2c2c2c"}
                        ),
                        html.Div(
                            className="table_products",
                            children=[
                                         # Header Row
                                         html.Div(
                                             className="header-row",
                                             children=[
                                                 html.Div("", style={"flex": "0.5"}),
                                                 html.Div("", style={"flex": "1"}),
                                                 html.Div("Product", style={"font-size": "18px", "font-weight": "bold",
                                                                            "flex": "2", "color": "#9c9ea0",
                                                                            "font-size": "20px",
                                                                            "font-family": "Montserrat, Helvetica Neue, Arial, sans-serif", }),
                                                 html.Div("Price", style={"font-size": "18px", "font-weight": "bold",
                                                                          "font-size": "20px",
                                                                          "flex": "1", "color": "#9c9ea0",
                                                                          "font-family": "Montserrat, Helvetica Neue, Arial, sans-serif"}),
                                                 html.Div("Tier", style={"font-size": "18px", "font-weight": "bold",
                                                                         "font-size": "20px",
                                                                         "flex": "1", "color": "#9c9ea0",
                                                                         "font-family": "Montserrat, Helvetica Neue, Arial, sans-serif"}),
                                                 html.Div("Sales Volume",
                                                          style={"font-size": "18px", "font-weight": "bold",
                                                                 "font-size": "20px",
                                                                 "flex": "1", "color": "#9c9ea0",
                                                                 "font-family": "Montserrat, Helvetica Neue, Arial, sans-serif"}),
                                                 html.Div("Total", style={"font-size": "18px", "font-weight": "bold",
                                                                          "flex": "1", "color": "#9c9ea0",
                                                                          "font-size": "20px",
                                                                          "font-family": "Montserrat, Helvetica Neue, Arial, sans-serif"})
                                             ],
                                             style={
                                                 "display": "flex",
                                                 "padding": "10px 30px",
                                             }
                                         )
                                     ] + table_rows + [total_row],
                            style={"width": "100%", "background-color": "#fff", }
                        )
                    ],
                    style={
                        "width": "90%",
                        "background-color": "#fff",
                        "margin": "20px auto",
                        "padding": "10px 0",
                    }
                )
            ]
        )


class chart_ctn3:
    def chart_l(self, game):
        game_data = next((g for g in datagame if convert_game_name(g["game"]) == convert_game_name(game)), None)
        if not game_data:
            return html.Div("Game not found.")
        session = game_data.get("session")
        if not session:
            return html.Div("Không có dữ liệu phiên chơi cho game này.")
        df = pd.DataFrame(session)
        df['session'] = df['session'].astype(int)
        df['cumulative_session'] = df['session']
        trace = go.Scatter(
            x=df['day'],
            y=df['cumulative_session'],
            mode='lines+markers',
            line=dict(color='rgba(255, 99, 132, 0.8)', shape='spline'),
            marker=dict(size=8),
        )

        layout = go.Layout(
            title="Biểu Đồ Tăng Trưởng Phiên Chơi Theo Ngày",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(title="Ngày"),
            yaxis=dict(title="Tổng Phiên Chơi Tích Lũy", gridcolor='rgba(204, 204, 204, 0.35)'),
            # template='plotly_dark',
        )

        return dcc.Graph(figure=go.Figure(data=[trace], layout=layout), config={"displayModeBar": False})

    def chart_r(self, game):
        game_data = next((g for g in datagame if convert_game_name(g["game"]) == convert_game_name(game)), None)
        if not game_data:
            return html.Div("Game not found.")
        avgtime = game_data.get("avgtime/day")
        if not avgtime:
            return html.Div("Không có dữ liệu về thời gian chơi cho game này.")
        df = pd.DataFrame(avgtime)
        df['avg'] = df['avg'].astype(float)
        trace = go.Scatter(
            x=df['day'],
            y=df['avg'],
            mode='lines+markers',
            line=dict(color='rgba(255, 99, 132, 0.8)', shape='spline'),
            marker=dict(size=8),
        )

        layout = go.Layout(
            title="Trung bình thời gian chơi theo ngày",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(title="Ngày"),
            yaxis=dict(title="Thời gian chơi trung bình mỗi người chơi", gridcolor='rgba(204, 204, 204, 0.35)'),
            # template='plotly_dark',
        )

        return dcc.Graph(figure=go.Figure(data=[trace], layout=layout), config={"displayModeBar": False})

    def chart_left(self, game):
        return html.Div(
            children=[
                self.chart_l(game),
            ],
            style={
                "width": "48%",
                "background-color": "#fff",
            }
        )

    def chart_right(self, game):
        return html.Div(
            children=[
                self.chart_r(game),
            ],
            style={
                "width": "48%",
                "background-color": "#fff",
            }
        )

    def show(self, game):
        return html.Div(
            children=[
                html.Div(
                    children=[self.chart_left(game),
                              self.chart_right(game)
                              ],
                    style={
                        "width": "90%",
                        "display": "flex",
                        "align-items": "stretch",
                        "justify-content": "space-between",
                    }
                )
            ],
            style={
                "width": "100%",
                "display": "flex",
                "align-items": "center",
                "justify-content": "center",
            }
        )


class chart_ctn4:
    def retention_chart(self, game):
        game_data = next((g for g in datagame if convert_game_name(g["game"]) == game), None)
        if game_data is None:
            return html.Div("Game không tồn tại.")
        retention_data = game_data.get("retention_data")
        if not retention_data:
            return html.Div("Không có dữ liệu retention cho game này.")

        df_retention = pd.DataFrame(retention_data)
        df_retention['day'] = pd.to_datetime(df_retention['day'], format='%d/%m/%Y')
        df_retention = df_retention.sort_values(by='day', ascending=False)  # Sắp xếp theo ngày giảm dần
        traces = []
        days = ['retention_day_1', 'retention_day_2', 'retention_day_3', 'retention_day_4', 'retention_day_5',
                'retention_day_6', 'retention_day_7']

        # Tạo 7 đường cho Retention của từng ngày
        for i, day in enumerate(days):
            trace = go.Scatter(
                x=df_retention['day'],
                y=df_retention[day],
                mode='lines+markers',
                name=f"Ngày {i + 1}",
                line=dict(shape='spline'),
                marker=dict(size=8),
            )
            traces.append(trace)
        xlayout = go.Layout(
            title="Retention Theo Ngày (7 Ngày)",
            xaxis=dict(title="Ngày", tickangle=45),
            yaxis=dict(title="Số Lượt Quay Lại Chơi", gridcolor='rgba(204, 204, 204, 0.35)'),
            showlegend=True,
            autosize=True,
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=20, r=20, t=40, b=40),
            xaxis_rangeslider_visible=False,
            height=400,
        )
        return dcc.Graph(figure=go.Figure(data=traces, layout=xlayout), config={"displayModeBar": False})

    def chart(self, game):
        return html.Div(
            children=[
                self.retention_chart(game),
            ],
            style={
                "padding-top": "30px",
                "width": "90%",
                "background-color": "#fff",
            }
        )

    def show(self, game):
        return html.Div(
            className="chart4",
            children=[
                self.chart(game),
                html.Div(
                    style={
                        "width": "90%",
                        "height": "25px",
                        "background-color": "#fff",
                    }
                )
            ],
            style={
                "width": "100%",
                "display": "flex",
                "flex-direction": "column",
                "align-items": "center",
                "justify-content": "center",
                "margin": "20px 0",
            }
        )


class chart_ctn5:
    def revenue_chart(self, game):
        # Chuẩn hóa tên game
        game_normalized = convert_game_name(game)
        # Tìm game trong datagame
        game_data = next((g for g in datagame if convert_game_name(g["game"]) == game_normalized), None)
        if game_data is None:
            return html.Div("Game không tồn tại.")
        # Lấy dữ liệu doanh thu
        revenue_data = game_data.get("revenue_data")
        if not revenue_data:
            return html.Div("Không có dữ liệu doanh thu cho game này.")

        df_revenue = pd.DataFrame(revenue_data)
        df_revenue['day'] = pd.to_datetime(df_revenue['day'], format='%d/%m/%Y')

        # Tính tổng doanh thu lũy tích
        df_revenue['cumulative_revenue'] = df_revenue['revenue'].cumsum()

        # Tạo biểu đồ cho doanh thu lũy tích
        trace = go.Scatter(
            x=df_revenue['day'],
            y=df_revenue['cumulative_revenue'],
            mode='lines+markers',
            name="Doanh Thu Lũy Tích",
            line=dict(shape='spline', color='rgba(0, 123, 255, 0.8)'),
            marker=dict(size=8),
        )

        # Layout của biểu đồ
        layout = go.Layout(
            title="Tổng Doanh Thu Lũy Tích Theo Ngày",
            xaxis=dict(title="Ngày", tickangle=45),
            yaxis=dict(title="Doanh Thu Lũy Tích ($)", gridcolor='rgba(204, 204, 204, 0.35)'),
            showlegend=True,
            autosize=True,
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=20, r=20, t=40, b=40),
            xaxis_rangeslider_visible=False,
            height=400,
        )

        # Trả về dcc.Graph cho biểu đồ
        return dcc.Graph(figure=go.Figure(data=[trace], layout=layout), config={"displayModeBar": False})

    def chart(self, game):
        return html.Div(
            children=[
                html.Div(
                    style={
                        "width": "90%",
                        "height": "10px",
                        "background-color": "#fff",
                    }
                ),
                self.revenue_chart(game),
            ],
            style={
                "width": "90%",
                "background-color": "#fff",
            }
        )

    def show(self, game):
        return html.Div(
            className="chart5",
            children=[
                html.Div(
                    style={
                        "width": "90%",
                        "height": "10px",
                        "background-color": "#fff",
                    }
                ),
                self.chart(game),
                html.Div(
                    style={
                        "width": "90%",
                        "height": "30px",
                        "background-color": "#fff",
                    }
                )
            ],
            style={
                "width": "100%",
                "display": "flex",
                "flex-direction": "column",
                "align-items": "center",
                "justify-content": "center",
                "margin-bottom": "20px",
            }
        )


class chart_ctn6:
    def revenue_analysis_chart(self, game):
        game_normalized = convert_game_name(game)
        game_data = next((g for g in datagame if convert_game_name(g["game"]) == game_normalized), None)
        if game_data is None:
            return html.Div("Game không tồn tại.")
        # Lấy dữ liệu doanh thu
        ad_revenue_data = game_data.get("ad_revenue_data")
        df_ad_revenue = pd.DataFrame(ad_revenue_data)
        df_ad_revenue['ad_rev_avgk'] = (df_ad_revenue['ad_rev_median'] + df_ad_revenue['ad_rev_avg']) / 2
        traces = []
        traces.append(go.Bar(
            x=df_ad_revenue['day'],
            y=df_ad_revenue['ad_rev_median'],
            name='Ad Rev Median ($)',
            marker=dict(color='rgba(255, 99, 132, 0.6789)')
        ))
        traces.append(go.Bar(
            x=df_ad_revenue['day'],
            y=df_ad_revenue['ad_rev_avgk'],
            name='Ad Rev Avg ($)',
            marker=dict(color='rgba(54, 162, 235, 0.6789)')
        ))
        traces.append(go.Bar(
            x=df_ad_revenue['day'],
            y=df_ad_revenue['ad_rev_avg'],
            name='Avg Revenue ($)',
            marker=dict(color='rgba(75, 192, 192, 0.6789)')
        ))

        layout = go.Layout(
            title="Doanh Thu Quảng Cáo Theo Ngày",
            xaxis=dict(title="Ngày", tickangle=45),
            yaxis=dict(title="Doanh Thu ($)", gridcolor='rgba(204, 204, 204, 0.35)'),
            barmode='group',
            plot_bgcolor='rgba(0,0,0,0)',
            showlegend=False,
            autosize=True,
            margin=dict(l=20, r=20, t=40, b=40),
            height=400,
        )
        return dcc.Graph(figure=go.Figure(data=traces, layout=layout), config={"displayModeBar": False})

    def chart(self, game):
        return html.Div(
            children=[
                self.revenue_analysis_chart(game),
            ],
            style={
                "padding-top": "10px",
                "width": "90%",
                "background-color": "#fff",
            }
        )

    def show(self, game):
        return html.Div(
            className="chart",
            children=[
                self.chart(game),
                html.Div(
                    style={
                        "padding-top": "20px",
                        "width": "90%",
                        "height": "10px",
                        "background-color": "#fff",
                    }
                )
            ],
            style={
                "width": "100%",
                "display": "flex",
                "flex-direction": "column",
                "align-items": "center",
                "justify-content": "center",
            }
        )
def showgame(game_path):
    game = game_path.split('/')[-1]
    game = convert_game_name(game)
    return html.Div(
        className=f"{game}_div",
        children=[
            navbar.navbarx,
            navbar.graph_nav(game),
            navbar.card(game),
            chart_ctn1().show(game),
            chart_ctn2().show(game),
            chart_ctn3().show(game),
            chart_ctn4().show(game),
            chart_ctn5().show(game),
            chart_ctn6().show(game),
        ],
        style={
            "background-color": "#f4f3ee",
            "width": "100%",
            "height": "4000px",
        }
    )
