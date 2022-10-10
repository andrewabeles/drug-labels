from dash import Dash, dcc, html, Input, Output, State
import pickle
import pandas as pd 
import plotly.express as px
from notebooks.cleaning import prepare, get_document_features

### GLOBAL VARIABLES ###

app = Dash(__name__, suppress_callback_exceptions=True)
server = app.server

# Load trained classifier 
with open('models/classifier.pkl', 'rb') as f: 
    classifier = pickle.load(f)
# Load classifier featureset 
with open('models/classifier_features.pkl', 'rb') as f:
    classifier_features = pickle.load(f)

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
        return html.Div(style={'display': 'flex'}, children=[
            html.Div(style={'width': '49%', 'display': 'inline-block'}, children=[
                html.H3('Dosage and Administration Text'),
                dcc.Textarea(
                    id='input-text',
                    style={'width': '99%', 'height': 370, 'resize': 'none'},
                    value='DIRECTIONS Chew tablets and let dissolve in mouth. Do not use more than directed. Do not take with food.'
                ),
                html.Button('Classify', id='classify-button', n_clicks=0)
            ]),
            html.Div(style={'width': '49%', 'display': 'inline-block'}, children=[
                html.H3('Predicted Route of Administration'),
                html.Div(id='pdist')
            ])
        ])
    elif selected_tab == 'topic-model-tab':
        return html.Div([
            html.H3('Topic Model')
        ])

@app.callback(
    Output('pdist', 'children'),
    Input('classify-button', 'n_clicks'),
    State('input-text', 'value')
)
def classify_text(n_clicks, text):
    if n_clicks > 0: 
        tokens = prepare(text)
        features = get_document_features(tokens, classifier_features)
        prediction = classifier.classify(features)
        pdist = classifier.prob_classify(features)
        pdist_df = pd.DataFrame({
            'route': classifier.labels(),
            'probability': [pdist.prob(route) for route in classifier.labels()]
        }).sort_values(by='probability')
        fig = px.bar(pdist_df, y='route', x='probability')
        return [dcc.Graph(figure=fig)]

### RUN APP ###

if __name__ == '__main__':
    app.run_server(debug=True)