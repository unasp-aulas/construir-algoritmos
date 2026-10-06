import numpy as np
import plotly.graph_objects as go
from shiny import App, render, ui, reactive

# Dados iniciais
x = np.array([-2, -2, -1, -1, 0, 0, 1, 1, 2, 2])
y = np.array([0, 0, 2, 3, 4, 4, 5, 6, 8, 8])

app_ui = ui.page_fluid(
    ui.input_slider("slope", "Slope", min=0, max=5, value=2, step=0.1),
    ui.input_slider("intercept", "Intercept", min=0, max=10, value=4, step=0.1),
    ui.output_plot("plot"),
)

def server(input, output, session):
    @render.plot
    def plot():
        fig = go.Figure()
        # Pontos
        fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name='Dados'))
        # Linha
        x_range = np.linspace(-3, 3, 100)
        y_line = input.slope() * x_range + input.intercept()
        fig.add_trace(go.Scatter(x=x_range, y=y_line, mode='lines', name='Regressão'))
        fig.update_layout(title="Regressão Linear Interativa", xaxis_title="x", yaxis_title="y")
        return fig

app = App(app_ui, server)
