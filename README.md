Text Mining Drug Labels
==============================

The objective of this project is to build two NLP models and showcase them using a simple web app. The first model classifies a drug’s route of administration (oral, topical, etc.) based on its label’s dosage and administration text. The second model is unsupervised and extracts topics from the dosage and administration text. The two models are then compared. This project uses the <a target="_blank" href="https://open.fda.gov/apis/drug/label/">OpenFDA API</a> as its data source. 

You can view the deployed web app <a target="_blank" href="https://drug-labels.herokuapp.com/">here.</a>

Project Organization
------------

    ├── README.md          <- The top-level README for developers using this project.
    |
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering)
    │                         and a short `-` delimited description, e.g.
    │                         `1.0-get-raw-data.ipynb`.
    |
    ├── cleaning.py        <- Module of helper functions for data cleaning. 
    |
    ├── models             <- Trained and serialized models.
    |
    ├── app.py             <- Dash application
    │
    ├── assets             <- Static assets for the dash app. 
    |
    ├── requirements.txt   <- The requirements file for Heroku deployment. 
    |
    ├── nltk.txt           <- nltk corpus requirements for Heroku deployment. 
    |
    ├── Procfile           <- Commands for Heroku deployment. 
    |
    ├── .slugignore        <- Files for Heroku to ignore.      

--------

<p><small>Project organization based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
