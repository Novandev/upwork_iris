# Iris Systems Dashboard Application


<img src="https://i.ibb.co/P6p6W9D/iris-systems-1.png" alt="iris-systems-1" border="0" style="margin:0 auto;">

## Architecture

The Iris Systems Dashbaord Application is built as a data ingestion, processing and reporting system.

This aims to do the following: 
- Make viewing reports, aggregations and predictions on inventory data in real-time as simple as possible.
- Make connecting to data origins as easy as possible.
- Make prediction/forecasted based suggestions for inventory levels based on past data and regional inventory levels



## Data Pipeline Flowchart
<img src="https://i.ibb.co/BgsmJHx/iris-flowcahrt.png" alt="iris-flowcahrt" border="0">


## Algorithms for Predictive Models
### Approach
Models Used to produce predictive dashboard are based of time series analysis due to the nature of that data coming in. Data involving inventory changes day to day, week to week, and month to month basedon the amount of patients as well as the types of procedures a certain hospital hands on on regular or irregular basis. This leave the data open to a number of Autoregressive models as well as deep learning approaches such Long Term Short Term Memory (LSTM for brevity) networks. Clustering algorithms are used to group hospitals into categories based on multivariate analysis of of combination of:

 - location of a hospital's resources
 - Prior date inventories
 - The totals of each resource that a hospital makes use of

### Autoregressive Modeling
For the purpose of this demo, the autoregressive model chosen was VARMA, though in the future a combination of autogressive models will be chosen for the highest accuracy possible


### Machine Learning

#### Deep Learning
Currently in development is a full scale LSTM network that will be trained not only off past data but also of the predictions and errors of the Autoregressive models. This model as well as others can be swapped out for higher accuracy if needed.

#### Clustering
This demo makes use of unsupervised learning to make unbiased groups that each hospital will fall in based on a variety of factors.
Agglomerative clustering due to the size of the dataset



## Technologies

- Language: Python
- Databases/Data: SQL, NoSQL, text files
- Libraries: Dash, Plotly, Tensorflow, Scikit-learn, Flask, StatsModels
- Hosting Heroku

## Hosting
Site can be seen at: https://iris-systems-demo.herokuapp.com/



