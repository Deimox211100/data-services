# Data Services Platform

This project provides a data platform stack using Docker Compose, including Airflow, MinIO, Spark, and JupyterHub for orchestrating, storing, processing, and analyzing data.

## Services

- **PostgreSQL**: Database backend for Airflow.
- **Airflow**: Workflow orchestration for ETL and data pipelines.
- **MinIO**: S3-compatible object storage for data exchange.
- **Spark**: Distributed data processing engine.
- **JupyterHub**: Multi-user Jupyter notebooks for data exploration.

## Folder Structure

```
.
├── dags/                # Airflow DAGs (workflows)
│   └── minio_spark.py   # Example DAG using MinIO and Spark
├── jupyterhub/          # JupyterHub Docker context and config
│   ├── Dockerfile
│   ├── jupyterhub_config.py
│   └── ...
├── spark_jobs/          # Spark job scripts
│   └── main_spark_jobs.py
├── requirements.txt     # Python dependencies for Airflow and Spark jobs
├── docker-compose.yml   # Docker Compose stack definition
├── .env                 # Environment variables (not committed)
└── ...
```

## Quick Start

1. **Set up environment variables**

   Create a `.env` file in the root directory with the following variables (example values):

   ```
   POSTGRES_USER=airflow
   POSTGRES_PASSWORD=airflow
   POSTGRES_DB=airflow
   AIRFLOW_USERNAME=admin
   AIRFLOW_PASSWORD=admin
   JUPYTERHUB_USER=youruser
   JUPYTERHUB_PASS=yourpass
   SPARK_MASTER_URL=spark://spark-master:7077
   ```

2. **Build and start the stack**

   ```sh
   docker-compose up --build
   ```

3. **Access the services**

   - **Airflow Web UI**: [http://localhost:8082](http://localhost:8082)
   - **MinIO Console**: [http://localhost:9002](http://localhost:9002)
     - Default credentials: `minioadmin` / `M1n10@dmin_P4ssw0rd_2206`
   - **Spark Master UI**: [http://localhost:8081](http://localhost:8081)
   - **JupyterHub**: [http://localhost:8888](http://localhost:8888)

## Example Workflow

- The example DAG [`minio_spark_dag`](dags/minio_spark.py) uploads a file to MinIO and then reads it using Spark.

## Customization

- Add your own Airflow DAGs in the [`dags/`](dags/) folder.
- Add Spark jobs in [`spark_jobs/`](spark_jobs/).
- Customize JupyterHub via [`jupyterhub/jupyterhub_config.py`](jupyterhub/jupyterhub_config.py).

## Requirements

- Docker
- Docker Compose

## Notes

- The `.env` file and sensitive files like JupyterHub secrets are excluded from version control via `.gitignore`.
- Python dependencies for Airflow and Spark jobs are managed in [`requirements.txt`](requirements.txt).

---

**License:** MIT (or specify your license)