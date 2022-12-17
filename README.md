# Developer's Salary Prediction

## Dataset

* Use [Stack Overflow Annual Developer Survey](https://insights.stackoverflow.com/survey) dataset to train model. 

* For Salary prediction purpose, use 9 features `RemoteWork`, `EdLevel`, `YearsCodePro`, `DevType`, `LanguageHaveWorkedWith`, `PlatformHaveWorkedWith`, 
`ToolsTechHaveWorkedWith`,
`Country`, `Age` to predict `ConvertedCompYearly` as Salary.

* Data preprocessing: [preprocess.py](dataset/preprocess.py)

* Data visualization: [visual.ipynb](visual.ipynb)

## Model

* Ultilize [Ensemble Method](https://scikit-learn.org/stable/modules/ensemble.html) to train model.

* Experiment with [RandomForest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html), [Bagging](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html), [AdaBoost](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html), [GradientBoosting](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html). Details in [main.ipynb](main.ipynb)

* Apply [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html) found best model is `Gradient Boosting (n_estimators=450)`.

### Best Result

| Metrics | Values |
| --- | --- | 
| [RMSE](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html) | 37359.955759 |  
| [MAE](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html) | 25795.854225 |   
| [R2-score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html) | 0.613329 | 

## Run Code

1. Install dependencies

```
pip install -r requirements.txt
```

2. Run streamlit web app

I build a streamlit app to easily view the data and predict the salary.

Run code:

```
streamlit run web.py
```

The result for reference only :>