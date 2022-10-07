from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1('Text Mining Drug Labels'),
    dcc.Tabs(id='selected-tab', value='classifier-tab', children=[
        dcc.Tab(label='Classifier', value='classifier-tab'),
        dcc.Tab(label='Topic Model', value='topic-model-tab')
    ]),
    html.Div(id='tab-content')
])

@app.callback(
    Output('tab-content', 'children'),
    Input('selected-tab', 'value')
)
def render_content(selected_tab):
    if selected_tab == 'classifier-tab':
        return html.Div([
            html.H3('Dosage and Administration Text'),
            dcc.Textarea(
                id='input-text',
                value='DIRECTIONS Chew tablets and let dissolve in mouth. Do not use more than directed. Do not take with food.',
                style={'width': '100%', 'height': 300}
            ),
            html.Button('Classify', id='classify-button'),
            html.H3('Predicted Route of Administration'),
            html.P('ORAL')
        ])
    elif selected_tab == 'topic-model-tab':
        return html.Div([
            html.H3('Topic Model')
        ])

if __name__ == '__main__':
    app.run_server(debug=True)