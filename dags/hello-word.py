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

@asset(schedule=transformed_data)
def loaded_data(context):
    my_sum = context["ti"].xcom_pull(
        dag_id="transformed_data",
        task_ids="transformed_data",
        key="return_value",
        include_prior_dates=True,
    )
    return f"Sum of a and b is {my_sum}"