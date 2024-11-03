import dash
import os
from dash import dcc, html
import dash_bootstrap_components as dbc
from dotenv import load_dotenv

# load enviroment
load_dotenv()

#get variable


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout
main_layout = html.Div(
    className="app",
    children=[
        html.Div(
            className="navbar",
            children=[
                html.H1("Streaming Dashboard Game", style={"color": "white", "margin": 0}),
                html.Div(
                    className="navbar-icons",
                    children=[
                        html.Img(
                            src="https://stream-metrics-b5f68d63e431.herokuapp.com/assets/github-mark-white.png",
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
                    style={"display": "flex", "justify-content": "center", "align-items": "center", "gap": "10px"},

                ),
            ],
            style={
                "display": "flex",
                "justifyContent": "space-between",
                "alignItems": "center",
                "backgroundColor": "#1e1e1e",
                "padding": "10px 20px",
                "borderBottom": "1px solid #d5d5d5",
                "marginBottom": "20px",
                "width": "100%",
                "padding-bottom": "5px",
            }
        ),
        html.Div(
            className="data-from",
            children=[
                html.P("Data for this app is pulled from the FK company API. Updated 2024-10-18",
                       style={"textAlign": "right", "padding-right": "40px"}, )

            ],
            style={

            }
        ),
        html.Button(
            className="filter-container",
            children=[
                html.P("Filters", style={"font-family": "Roboto", "font-weight": "500", "font-size": "16px",
                                         "padding-top": "10px"}, ),
                html.Img(
                    src="./assets/IMG/outline.svg",
                    alt="GitHub",
                    style={"cursor": "pointer", "transform": "rotate(270deg)"},  # Moved cursor styling here
                )
            ],
            style={
                "display": "flex",
                "justifyContent": "space-between",
                "alignItems": "center",
                "width": "85%",
                "padding": "0px 20px"
            }
        ),
        html.Div(
            className="card-container",
            children=[
                html.Div(
                    className="card",
                    children=[
                        html.P("37",style={
                            "textAlign": "left",
                            "font-family": "Roboto",
                            "font-weight": "700",
                            "font-size": "45px",
                            "padding-top": "10px",
                            "padding-left": "10%",
                            "margin-bottom": "0px",
                        }),
                        html.P("IOS",style={
                            "textAlign": "left",
                            "font-family": "Roboto",
                            "font-size": "18px",
                            "font-weight": "700",
                            "padding-left": "10%",
                        }),
                    ],
                    style={
                        "width": "22%",
                    }
                ),
html.Div(
                    className="card",
                    children=[
                        html.P("37",style={
                            "textAlign": "left",
                            "font-family": "Roboto",
                            "font-weight": "700",
                            "font-size": "45px",
                            "padding-top": "10px",
                            "padding-left": "10%",
                            "margin-bottom": "0px",
                        }),
                        html.P("ANDROID",style={
                            "textAlign": "left",
                            "font-family": "Roboto",
                            "font-size": "18px",
                            "font-weight": "700",
                            "padding-left": "10%",
                        }),
                    ],
                    style={
                        "width": "22%",
                    }
                ),
html.Div(
                    className="card",
                    children=[
                        html.P("37",style={
                            "textAlign": "left",
                            "font-family": "Roboto",
                            "font-weight": "700",
                            "font-size": "45px",
                            "padding-top": "10px",
                            "padding-left": "10%",
                            "margin-bottom": "0px",
                        }),
                        html.P("MACOS",style={
                            "textAlign": "left",
                            "font-family": "Roboto",
                            "font-size": "18px",
                            "font-weight": "700",
                            "padding-left": "10%",
                        }),
                    ],
                    style={
                        "width": "22%",

                    }
                ),
html.Div(
                    className="card",
                    children=[
                        html.P("37",style={
                            "textAlign": "left",
                            "font-family": "Roboto",
                            "font-weight": "700",
                            "font-size": "45px",
                            "padding-top": "10px",
                            "padding-left": "10%",
                            "margin-bottom": "0px",
                        }),
                        html.P("WINDOWS",style={
                            "textAlign": "left",
                            "font-family": "Roboto",
                            "font-size": "18px",
                            "font-weight": "700",
                            "padding-left": "10%",
                        }),
                    ],
                    style={
                        "width": "22%",

                    }
                )
            ],
            style={
                "width": "85%",
                "display": "flex",
                "alignItems": "center",
                "justifyContent": "space-between",
            }
        ),
    ],
    style={
        "width": "100%",
        "display": "flex",
        "flex-direction": "column",
        "alignItems": "center",
        "gap": "10px",
    }
)

layout2 = html.Div(
    className="two",
    children=[
        html.Div(
            className="over-view",
            children=[],
            style={
                "width": "60%",
                "height": "500px",
                "border": "0.1px solid #1e1e1e",
            }
        ),
html.Div(
            className="over-view",
            children=[],
            style={
                "width": "36%",
                "height": "500px",
                "border": "0.1px solid #1e1e1e",
            }
        )
    ],
    style={
        "width": "85%",
        "display": "flex",
        "flex-direction": "row",
        "alignItems": "center",
        "gap": "3.4%",
        "justifyContent": "space-between",
    }
)

layout3 = html.Div(
    className="three",
    children=[],
    style={
        "width": "85%",
        "display": "flex",
        "height": "500px",
        "border": "0.1px solid #1e1e1e",
    }
)

layout4 = html.Div(
    className="three",
    children=[],
    style={
        "width": "85%",
        "display": "flex",
        "height": "5000px",
    }
)

@app.callback(game 1)


#all layout
app.layout = html.Div(children=[main_layout, layout2,layout3,layout2,layout3,layout4],
                      style={
                          "width": "100%",
                          "display": "flex",
                          "flex-direction": "column",
                          "alignItems": "center",
                          "gap": "30px",
                      })
# Run app
if __name__ == "__main__":
    app.run_server(debug=True)
