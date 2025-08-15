from airflow.sdk import asset


@asset(schedule="@daily")
def extracted_data():
    return {"a": 23, "b": 19}