from airflow import DAG
from airflow.decorators import task

from datetime import datetime

with DAG('xcome', start_date=datetime(2022,1 ,1), schedule_interval='@daily', catchup=False):

    @task
    def a_task(ti=None): #ti = task instance
        return 'iphone'
        # when you return a value from the python operator, 
        # that value becomes automatically an xcom with the key "retuen_value"
        # so you can shere it with other tasks.
    
    @task
    def b_task(mobile_phone):
        print (mobile_phone)

    b_task (a_task())
