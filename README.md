# Text-message-pipeline
This repository documents a data science project: analysis and classification of disaster text messages.


### Table of Contents


1. [Overview](#overview)
2. [File Descriptions](#files)
3. [Environment](#installation)
4. [Results](#results)
5. [Data Source, License, Acknowledgement](#source)




## Overview<a name="overview"></a>

In this project, we analyze a disaster text messages dataset, build a ETL pipeline and machine learning model to classify messages into different information categories, and deploy them via a web application.

The **DATA** consists of text messages sent following a natural disaster.

The **GOAL** is to identify the needed resource or key information for each message in real time, such as 'water', 'medicare', 'transportation', etc, so that it can be sent to appropriate disaster relief agencies.

The main components of this project are:

(1). **ETL Pipeline**: to clean, transform, and save the text messages and categories data.

(2). **Natural Language Processing**: to vectorize the text data and extract/engineer important features.

(3).  **Category Classification**: to train classifiers to predict which categories a message belong to.

(4). **Web App Deployment**: to launch a web API to take new messages from users and make prediction, based on the pipeline and model we trained.


## File Descriptions <a name="files"></a>

- etl_pipeline.py: a python script that implement the ETL process for text messages.

- classify_messages.py: a python script that runs a ML model and classify a given message into different categories.

- etl_model_prototype.ipynb: a Jupyter Notebook that contains the prototypes of the ETL pipeline, the classification model, as well as some off-line analysis on the dataset.



## Environment <a name="installation"></a>

- The Anaconda distribution of Python3.
- Jupyter Notebook.  
- XGBoost. See [here](https://xgboost.readthedocs.io/en/latest/build.html) for installation guide.
- NLTK package, with some common modules. See [here](https://www.nltk.org/) for installation guide.

## Results<a name="results"></a>

The result of the project will be delivered via this web application (tba).


## Data Source, License, Acknowledgement <a name="source"></a>

The original dataset is generously provided by [Figure Eight](https://appen.com/).

You can find the Licensing for the dataset and other descriptive information in the link above.  Other than that, feel free to use anything here as you would like!

The project is inspired by this [Udacity data science program](https://www.udacity.com/course/data-scientist-nanodegree--nd025).
