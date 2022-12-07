import pandas as pd
from sklearn import metrics 

def evaluate(y_true, y_pred):
    rmse = metrics.mean_squared_error(y_true=y_true, y_pred= y_pred, squared=False)
    mae = metrics.mean_absolute_error(y_true, y_pred)
    r2 = metrics.r2_score(y_true, y_pred)

    metrics_dict = {
        "Metrics": ["Root Mean Square Error (RMSE)", 
                    "Mean Absolute Error (MAE)", 
                    "R2-score (R2)"],
        "Values": [rmse, 
                    mae, 
                    r2]
    }

    metrics_df = pd.DataFrame(metrics_dict)
    print(metrics_df)