from dash import Dash, dcc, html, Input, Output, State
import pickle

### GLOBAL VARIABLES ###

app = Dash(__name__, suppress_callback_exceptions=True)
server = app.server

# Load trained classifier 
with open('models/classifier.pkl', 'rb') as f: 
    classifer = pickle.load(f)

### APP LAYOUT ###

app.layout = html.Div([
    html.H1('Text Mining Drug Labels'),
    dcc.Tabs(id='selected-tab', value='classifier-tab', children=[
        dcc.Tab(label='Classifier', value='classifier-tab'),
        dcc.Tab(label='Topic Model', value='topic-model-tab')
    ]),
    html.Div(id='tab-content')
])

### APP CALLBACKS ###

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
            html.Button('Classify', id='classify-button', n_clicks=0),
            html.H3('Predicted Route of Administration'),
            html.P(id='prediction')
        ])
    elif selected_tab == 'topic-model-tab':
        return html.Div([
            html.H3('Topic Model')
        ])

@app.callback(
    Output('prediction', 'children'),
    Input('classify-button', 'n_clicks'),
    State('input-text', 'value')
)
def classify_text(n_clicks, text):
    if n_clicks > 0: 
        return "The classifier's prediction will be shown here."

### RUN APP ###

if __name__ == '__main__':
    app.run_server(debug=True)