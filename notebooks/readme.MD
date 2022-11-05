# Extracted Features

* We extracted the following features from the assets provided about the creatives

1. Text Features
2. Logo Features
3. Object Features
4. CTA button features
5. the position of the engagement button (tap & hold the icon in the figure above)

* We trained the most popular decision tree algorithms namely the RF and XGboost ML algorithms with the ensembled features together with the performance data for KPI maximization. 
    * ml_preprocess.ipynb is used to prepare the csv data inorder to make it ready to be fed to the   models.
    * ml.ipynb is used to do the main training and compare the models and finally choose the better performing model.
