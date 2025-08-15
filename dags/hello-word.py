from airflow.sdk import asset

@asset(schedule="@daily")
def extracted_data():
    return {"a": 23, "b": 19}

@asset(schedule=extracted_data)
def transformed_data(context):
    my_data = context["ti"].xcom_pull(
        dag_id="extracted_data",
        task_ids="extracted_data",
        key="return_value",
        include_prior_dates=True,
    )
    summed_data = my_data["a"] + my_data["b"]
    return summed_data