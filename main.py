import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from data import country_sum_df, total_sum_df

stylesheets = ["https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css",
               "https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&display=swap"]
app = dash.Dash(__name__, external_stylesheets=stylesheets)

# print(total_sum_df)
print(country_sum_df)

app.layout = html.Div(
    style={"minHeight": "100vh",
           "backgroundColor": "black", "color": "white", "fontFamily": "Open Sans, sans-serif"},
    children=[
        html.Header(
            style={"textAlign": "center",
                   "paddingTop": "50px", "fontSize": "2rem", },
            children=[html.H1("Corona Dashboard")]
        ),
        html.Div(
            children=[
                html.Thead(
                    children=[
                        html.Thead(
                            children=[
                                html.Th(
                                    column_name
                                ) for column_name in country_sum_df
                            ]
                        )
                    ]
                ),
                html.Tbody(
                    children=[
                        html.Tr(
                            children=[
                                html.Td(
                                    col_value
                                ) for col_value in row
                            ]
                        ) for row in country_sum_df.values
                    ]
                )
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
