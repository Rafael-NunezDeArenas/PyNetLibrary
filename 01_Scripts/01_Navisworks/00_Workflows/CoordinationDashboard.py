import psutil
import time
import pandas as pd
from dash import Dash, dcc, html, Output, Input
import plotly.express as px
from pathlib import Path
import webbrowser

CSV_PATH = Path.home() / "Desktop" / "clash_dashboard.csv"


MAX_POINTS = 120

HISTORY = pd.DataFrame({
    "timestamp": pd.Series(dtype="datetime64[ns]"),
    "memory_mb": pd.Series(dtype="float"),
    "total_clashes": pd.Series(dtype="int")
})

start_time = time.time()


def get_memory_mb():
    return psutil.Process().memory_info().rss / (1024 * 1024)


def make_card(title, value, state=None, large=False):
    """
    state: 'new', 'active', 'reviewed', 'approved', 'resolved' o None
    """
    classes = ["card"]
    if large:
        classes.append("card-large")
    if state:
        classes.append(f"card-{state}")
    
    return html.Div(
        [
            html.Div(title, className="card-title"),
            html.Div(value, className="card-value"),
        ],
        className=" ".join(classes)
    )


def RunDashboard():
    app = Dash(__name__)

    app.layout = html.Div(
        className="container",
        children=[
            html.H1("Clash Dashboard", className="title"),

            html.Div(id="cards", className="cards-container"),

            html.Div(
                className="graphs-container",
                children=[
                    dcc.Graph(
                        id="pie-chart",
                        className="graph",
                        config={"responsive": False},
                        style={"height": "350px"}
                    ),
                    dcc.Graph(
                        id="line-chart",
                        className="graph",
                        config={"responsive": False},
                        style={"height": "350px"}
                    ),
                ]
            ),

            dcc.Interval(
                id="interval",
                interval=1000,
                n_intervals=0
            )
        ]
    )

    @app.callback(
        Output("pie-chart", "figure"),
        Output("line-chart", "figure"),
        Output("cards", "children"),
        Input("interval", "n_intervals")
    )
    def updateGraphs(_):
        global HISTORY

        if CSV_PATH.exists():
            df = pd.read_csv(CSV_PATH)
        else:
            df = pd.DataFrame({
                "new": [0],
                "active": [0],
                "reviewed": [0],
                "approved": [0],
                "resolved": [0]
            })

        df.columns = df.columns.str.strip().str.lower()
        df = df.fillna(0).astype(int)

        melted = df.melt(
            value_vars=["new", "active", "reviewed", "approved", "resolved"],
            var_name="status",
            value_name="count"
        )

        color_map = {
            "new": "#ff4c4c",
            "active": "#ffb300",
            "reviewed": "#3385ff",
            "approved": "#33cc33",
            "resolved": "#9933ff"
        }

        pie_fig = px.pie(
            melted,
            names="status",
            values="count",
            title="Distribución de clashes",
            color="status",
            color_discrete_map=color_map
        )

        pie_fig.update_traces(
            textinfo="percent+label",
            marker=dict(line=dict(color='#fff', width=2))
        )

        pie_fig.update_layout(
            height=350,
            autosize=False,
            margin=dict(t=50, b=20, l=20, r=20)
        )

        total_clashes = df[["new", "active", "reviewed", "approved", "resolved"]].sum(axis=1).iloc[0]

        new_row = pd.DataFrame([{
            "timestamp": pd.Timestamp.now(),
            "memory_mb": float(get_memory_mb()),
            "total_clashes": int(total_clashes)
        }])

        HISTORY = pd.concat([HISTORY, new_row], ignore_index=True)

        if len(HISTORY) > MAX_POINTS:
            HISTORY = HISTORY.iloc[-MAX_POINTS:]

        line_fig = px.line(
            HISTORY,
            x="timestamp",
            y="memory_mb",
            title="Uso de memoria durante ejecución (MB)"
        )

        line_fig.update_traces(
            mode="lines+markers",
            line=dict(color="#006655", width=3),  # verde oscuro azulado
            marker=dict(size=6, color="#006655", line=dict(width=1, color="white"))
        )

        line_fig.update_layout(
            height=350,
            autosize=False,
            xaxis_title="Tiempo",
            yaxis_title="Memoria (MB)",
            margin=dict(t=50, b=40, l=50, r=20),
            xaxis=dict(
                range=[HISTORY["timestamp"].iloc[0], HISTORY["timestamp"].iloc[-1]],
                fixedrange=True,
                showgrid=True,
                gridcolor="lightgray"
            ),
            yaxis=dict(
                autorange=True,
                fixedrange=True,
                showgrid=True,
                gridcolor="lightgray"
            ),
            plot_bgcolor="white",
            paper_bgcolor="white"
        )

        line_fig.add_traces(
            px.area(HISTORY, x="timestamp", y="memory_mb", color_discrete_sequence=["#99ccb3"]).data
        )

        elapsed_time = time.time() - start_time

        cards = [
            make_card("New", df["new"].iloc[0], state="new"),
            make_card("Active", df["active"].iloc[0], state="active"),
            make_card("Reviewed", df["reviewed"].iloc[0], state="reviewed"),
            make_card("Approved", df["approved"].iloc[0], state="approved"),
            make_card("Resolved", df["resolved"].iloc[0], state="resolved"),
            make_card("Tiempo ejecución", f"{elapsed_time:.1f}s")
        ]

        return pie_fig, line_fig, cards

    webbrowser.open("http://127.0.0.1:8050")
    app.run(port=8050, debug=False, use_reloader=False)