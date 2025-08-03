from prophet import Prophet
import pandas as pd

def generate_forecast(df, target='adr', periods=30):
    data = df.groupby("arrival_date")[target].mean().reset_index()
    data.columns = ['ds', 'y']

    model = Prophet()
    model.fit(data)

    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)

    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
