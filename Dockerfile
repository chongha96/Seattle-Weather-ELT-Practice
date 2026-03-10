FROM apache/airflow:slim-3.1.8rc1-python3.13

USER root
# Install system dependencies required for postgres drivers
RUN apt-get update && \
    apt-get install -y --no-install-recommends libpq-dev gcc python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER airflow
# Install the python driver
RUN pip install --no-cache-dir psycopg2-binary