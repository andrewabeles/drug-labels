from dash import Dash, dcc, html, Input, Output, State
import pickle
import pandas as pd 
import plotly.express as px
from cleaning import prepare, get_document_features

app = Dash(__name__, suppress_callback_exceptions=True)
server = app.server

# Load trained classifier 
with open('models/classifier.pkl', 'rb') as f: 
    classifier = pickle.load(f)
# Load classifier featureset 
with open('models/classifier_features.pkl', 'rb') as f:
    classifier_features = pickle.load(f)

app.layout = html.Div([
    html.H1('Text Mining Drug Labels'),
    dcc.Tabs([
        dcc.Tab(label='Classifier', children=[
            html.Div(style={'display': 'flex'}, children=[
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
        ]),
        dcc.Tab(label='Topic Model', children=[
            html.Div([
                html.Iframe(
                    src=app.get_asset_url('lda_display.html'),
                    style={
                        'position': 'absolute',
                        'width': '100%',
                        'height': '100%'
                    }
                )
            ])
        ])
    ])
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

if __name__ == '__main__':
    app.run_server(debug=True)