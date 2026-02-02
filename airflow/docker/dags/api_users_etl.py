import requests
import pandas as pd
from airflow.decorators import dag, task
from datetime import datetime, timedelta

# Define default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG using the @dag decorator
@dag(
    dag_id='api_users_etl',
    default_args=default_args,
    schedule_interval='@daily', # Runs once a day
    catchup=False,
    tags=["users"],
    doc_md="""
    ### API to Pandas ETL DAG
    This DAG fetches data from a sample API, transforms it into a pandas DataFrame, and simulates loading the data.
    """
)
def api_users_etl():

    @task()
    def extract_data():
        """
        Fetches data from a sample API and returns a list of dictionaries.
        """
        url = "https://jsonplaceholder.typicode.com/users" # Sample API
        response = requests.get(url)
        data = response.json()
        # Return value is automatically pushed to XCom
        return data

    @task()
    def transform_data(api_data: list):
        """
        Converts the list of dictionaries to a pandas DataFrame and performs a simple transformation.
        """
        df = pd.DataFrame(api_data)
        # Select and rename columns
        df = df[['id', 'name', 'email', 'company']]
        df.columns = ['user_id', 'full_name', 'email_address', 'company_info']
        # Return value (the DataFrame) is automatically pushed to XCom
        return df

    @task()
    def load_data(dataframe: pd.DataFrame):
        """
        Simulates loading the DataFrame to a destination (e.g., print to console, save to S3/DB).
        """
        print("--- Final DataFrame ---")
        print(dataframe.head())
        print(f"Data loaded successfully. Total rows: {len(dataframe)}")
        # In a real scenario, you would use a Hook to store data in a persistent storage
        # e.g., df.to_csv("/tmp/extracted_data.csv", index=False)

    # Define the workflow
    extracted_data = extract_data()
    transformed_dataframe = transform_data(extracted_data)
    load_data(transformed_dataframe)

# Instantiate the DAG
api_users_etl()
