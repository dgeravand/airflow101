from airflow import DAG
from airflow.decorators import task

from datetime import datetime

with DAG('xcom_e_pulling_mutiple_values', start_date=datetime(2022,1 ,1), schedule_interval='@daily', catchup=False):

    @task
    def p1_task(ti=None): 
        ti.xcom_push(key='mobile_phone', value='iphone')
    
    @task
    def p2_task(ti=None): 
        ti.xcom_push(key='mobile_phone', value='samsung')
    
    @task
    def c_task(ti=None):
        phone = ti.xcom_pull(task_ids=['p1_task','p2_task'], key='mobile_phone')
        print (phone)

    p1_task() >> p2_task() >> c_task()