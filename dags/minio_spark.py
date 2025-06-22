from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from minio import Minio
import findspark
findspark.init()
from pyspark.sql import SparkSession
import os
from os import getenv

minio_user = getenv('MINIO_ROOT_USER', 'minioadmin')
minio_pass = getenv('MINIO_ROOT_PASSWORD', 'minioadmin')

default_args = {
    'owner': 'airflow',
    'retries': 1,
}

dag = DAG(
    dag_id = 'minio_spark_dag',
    default_args = default_args,
    description = 'Ejemplo DAG con MinIO y Spark',
    schedule_interval = None,
    start_date = days_ago(1),
    catchup = False
)

def upload_file_to_minio():
    client = Minio(
        "minio:9000",
        access_key = minio_user,
        secret_key = minio_pass,
        secure = False
    )
    
    bucket = "airflow"
    file_path = "/tmp/dummy.txt"
    file_content = "Archivo generado por Airflow."

    with open(file_path, "w") as f:
        f.write(file_content)

    if not client.bucket_exists(bucket):
        client.make_bucket(bucket)

    client.fput_object(bucket, "dummy.txt", file_path)

def read_minio_with_spark():
    spark = SparkSession.builder \
        .appName("ReadFromMinIO") \
        .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000") \
        .config("spark.hadoop.fs.s3a.access.key", "minioadmin") \
        .config("spark.hadoop.fs.s3a.secret.key", "M1n10@dmin_P4ssw0rd_2206") \
        .config("spark.hadoop.fs.s3a.path.style.access", "true") \
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
        .getOrCreate()

    df = spark.read.text("s3a://airflow/dummy.txt")
    df.show()

upload_task = PythonOperator(
    task_id = 'upload_to_minio',
    python_callable = upload_file_to_minio,
    dag = dag,
)

spark_task = PythonOperator(
    task_id = 'read_with_spark',
    python_callable = read_minio_with_spark,
    dag = dag,
)

upload_task >> spark_task