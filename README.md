## airflow101
curl -sSL install.astronomer.io | sudo bash -s

astro version

mkdir airflow101

cd airflow101

-------------generate a new Airflow project-------------

astro dev init

code .

-------------------------------
docker up
----------image list-----------
astro dev ps
------------start--------------------
astro dev start
----------------------------------
if we face with port error like this: 
Error: error building, (re)creating or starting project containers: Error response from daemon: Ports are not available: exposing port TCP 127.0.0.1:5432 -> 0.0.0.0:0: listen tcp 127.0.0.1:5432: bind: An attempt was made to access a socket in a way forbidden by its access permissions.
we can chenge this file like this: 
airflow101/.astro/config.yaml

project:
    name: airflow-101
webserver:
    port: 8081
postgres:
    port: 5435

------------------------------------
astro dev stop
astro dev restart
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


> astro dev run info

Apache Airflow
version                | 2.9.2+astro.2
executor               | LocalExecutor
task_logging_handler   | airflow.utils.log.file_task_handler.FileTaskHandler
sql_alchemy_conn       | postgresql://postgres:postgres@postgres:5432
dags_folder            | /usr/local/airflow/dags
plugins_folder         | /usr/local/airflow/plugins
base_log_folder        | /usr/local/airflow/logs
remote_base_log_folder |

#Davood Geravand https://www.linkedin.com/analytics/profile-views/
