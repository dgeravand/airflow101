from airflow import DAG
from airflow.decorators import task

from datetime import datetime

with DAG('xcome_b', start_date=datetime(2022,1 ,1), schedule_interval='@daily', catchup=False):

    @task
    def a_task(ti=None): 
        #ti = task instance - you need it in order to call a special method that allows you to push an xcome
        # to push a value into your data base
        ti.xcom_push(key='mobile_phone', value='iphone')
    
    @task
    def b_task(ti=None):
        phone = ti.xcom_pull(task_ids='a_task', key='mobile_phone')
        print (phone)

    a_task() >> b_task()