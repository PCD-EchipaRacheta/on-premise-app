from google.cloud import bigquery
import pandas as pd
import json
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:/Users/Maria/OneDrive/Documents/GitHub/data-import/weatherapp-455117-2c3525ada720.json"

def get_forecats_data():
    client = bigquery.Client()

    query = """
        SELECT * 
        FROM `weatherapp-455117.weather_data.weather-forecast`
    """

    query_job = client.query(query)
    df = query_job.to_dataframe()
    json_data = df.to_json(orient="records")
    
    return json_data

# get_forecats_data()