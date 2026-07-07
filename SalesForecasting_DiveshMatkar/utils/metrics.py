from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    mean_absolute_percentage_error
)

import numpy as np


def regression_metrics(y_true, y_pred):

    return {

        "MAE": mean_absolute_error(y_true, y_pred),

        "RMSE": np.sqrt(mean_squared_error(y_true, y_pred)),

        "MAPE": mean_absolute_percentage_error(y_true, y_pred)

    }