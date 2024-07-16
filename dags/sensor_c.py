from airflow.decorators import dag, task
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
from airflow.sensors.python import PythonSensor
from datetime import datetime

def _condition():
    # # Get the current minute
    # current_minute = datetime.now().minute
    # # Return True if the current minute is even, False if odd
    # return current_minute % 2 == 0
    return False
@dag(
    schedule=None,
    start_date=datetime(2023, 1, 1),
    tags=['aws'],
    catchup=False
)
def sensor_dag_c():

    waiting_for_condition = PythonSensor(
        task_id="waiting_for_condition",
        python_callable=_condition,
        poke_interval=10,
        timeout=7 * 24 * 60 * 60
    )

    @task
    def process():
        print("processe start!")

    waiting_for_condition >> process()

sensor_dag_c()