import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

stylesheets = ["https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css",
               "https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&display=swap"]
app = dash.Dash(__name__, external_stylesheets=stylesheets)
app.layout = html.Div(
    style={"minHeight": "100vh",
           "backgroundColor": "black", "color": "white", "fontSize": "2rem", "fontFamily": "Open Sans, sans-serif"},
    children=[html.Header(
        style={"textAlign": "center", "paddingTop": "50px"},
        children=[html.H1("Corona Dashboard")]
    )],
)

if __name__ == '__main__':
    app.run_server(debug=True)
