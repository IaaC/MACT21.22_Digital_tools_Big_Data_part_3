from dash import Dash, dcc, html, Input, Output
import plotly.express as px

import pandas as pd

# A new dataset can be used. We selected data from Open Data Barcelona
# https://opendata-ajuntament.barcelona.cat/data/en/dataset/taula-map-scensal
# The columns available are:
df = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/784cefda-9219-4b61-b5d5-68b5ac453070/resource/f1d9d5aa-61d7-460e-b423-1bbfff96fab3/download')

df['ANYO'] = pd.to_numeric(df["DATA_DADES"].str[:2])

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        df['ANYO'].min(),
        df['ANYO'].max(),
        step=None,
        value=df['ANYO'].min(),
        marks={str(year): str(year) for year in df['ANYO'].unique()},
        id='year-slider'
    )
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    filtered_df = df[df.ANYO == selected_year]

    fig = px.scatter(filtered_df, x="HOMES", y="DONES",
                     size="NACIONALS", color="SECCIO_CENSAL", hover_name="NACIONALS",
                     log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
