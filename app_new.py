import streamlit as st
import streamlit.components.v1 as components
import pickle 
import pandas as pd 
import plotly.express as px 
import base64 
from cleaning import prepare, get_document_features 

# Load trained classifier 
with open('models/classifier.pkl', 'rb') as f: 
    classifier = pickle.load(f)
# Load classifier featureset 
with open('models/classifier_features.pkl', 'rb') as f:
    classifier_features = pickle.load(f)

st.set_page_config(layout="wide")

st.title('Text Mining Drug Labels')
tab1, tab2 = st.tabs(['Classifier', 'Topic Model'])

# classifier tab 
col1, col2 = tab1.columns(2)

col1.write('Dosage and Administration Text')
text = col1.text_area(
    "Enter the drug's dosage and administration text here.",
    value='DIRECTIONS Chew tablets and let dissolve in mouth. Do not use more than directed. Do not take with food.'
)

def classify_text(text):
    tokens = prepare(text)
    features = get_document_features(tokens, classifier_features)
    pdist = classifier.prob_classify(features)
    pdist_df = pd.DataFrame({
        'route': classifier.labels(),
        'probability': [pdist.prob(route) for route in classifier.labels()]
    }).sort_values(by='probability')
    fig = px.bar(pdist_df, y='route', x='probability')
    return fig 

clicked = col1.button('Classify')

col2.write('Predicted Route of Administration')
if clicked:
    col2.plotly_chart(classify_text(text))

with open('assets/lda_display.html', 'r') as file:
    html = file.read().encode('utf-8')
    html = base64.b64encode(html).decode()

with tab2:
    components.iframe(
        f"data:text/html;base64,{html}", 
        height=900,
        scrolling=True
    )