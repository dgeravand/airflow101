from airflow.decorators import task, dag
from airflow.exceptions import AirflowException
from datetime import datetime

@dag(start_date=datetime(2023, 1, 1), schedule=None, catchup=False)
def cli():

    @task
    def my_task(val):
        print(val)
        #raise AirflowException()
        return 42

    my_task(80)
cli()

#airflow tasks test <dag_id> <task_id> <logical_date>
#airflow tasks test cli my_task 2023-01-01