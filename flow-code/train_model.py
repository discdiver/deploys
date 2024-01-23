import numpy as np
from prefect import flow
from sklearn.linear_model import LinearRegression


@flow(log_prints=True)
def train_model(forecasted_temps: list[float]):
    X = np.array(forecasted_temps).reshape(-1, 1)
    randvals = np.random.rand(11, 1)  # creating random values for y
    y_train = [val * 10 for val in randvals]
    X_train = X[:11]
    X_test = np.array(X[-1]).reshape(1, -1)
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    prediction = lr.predict(X_test)
    expected_customers = int(prediction.item())
    print(
        f"Expected customers in 12 hours based on our amazing model: {expected_customers}"
    )
    return expected_customers
