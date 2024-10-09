from airflow import DAG
from airflow.operators.mysql_operator import MySqlOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

dag = DAG(
    'mysql_to_postgresql_etl',  # ชื่อของ DAG
    default_args=default_args,
    description='ETL DAG to migrate data from MySQL to PostgreSQL',
)

# Task: Extract data from MySQL
extract_data = MySqlOperator(
    task_id='extract_mysql_data',
    mysql_conn_id='mysql_source_connection',
    sql='SELECT * FROM your_table',
    dag=dag,
)

# Task: Load data into PostgreSQL
load_data = PostgresOperator(
    task_id='load_data_to_postgres',
    postgres_conn_id='postgres_destination_connection',
    sql='INSERT INTO your_postgres_table (column1, column2) VALUES (%s, %s)',
    parameters=[('value1', 'value2')],
    dag=dag,
)

extract_data >> load_data  # Sequence of tasks
