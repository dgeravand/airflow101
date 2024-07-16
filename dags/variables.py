from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable

from datetime import datetime

def _var_task(parameter):
    print(parameter)

with DAG('read_variable', start_date=datetime(2022,1 ,1), schedule_interval='@daily', catchup=False):

    for param in Variable.get('listvariable', deserialize_json = True)["val"]:
        print(param)
        PythonOperator(
            task_id=f'task_{param}',
            python_callable=_var_task,
            op_kwargs={'parameter':param} #op_kwargs parameter expects a dictionary
        )
