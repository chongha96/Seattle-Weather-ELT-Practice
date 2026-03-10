### Note: This was created by following a guide for learning purposes.

# Automated Data ELT Pipeline (API → Postgres → dbt) with Airflow:


A containerized ELT data pipeline that extracts real-time weather data via Weatherstack API. 

Loads the data into a PostgreSQL dev environment, and performs transformations using dbt, orchestrated by Apache Airflow. 



# Project Overview:

The goal of this project is to practice building a modern data stack with automated scheduling using modern tools like Airflow and Docker.

It demonstrates how to manage dependencies between ingestion modules and transformation modules in a fully containerized environment. 



# Architecture
The pipeline follows an ELT (Extract, Load, Transform) pattern: 

    1. Creates an API call to Weather Stack for local Seattle weather at current time
    
    2. Loads the data into the dev.raw_weather_data table
    
    3. Performs basic transformations (Average wind speed and temperature) using dbt.
       This task only runs after Airflow confirms that the data load task was successful.
       
    4. Airflow DAG orchestrates the automation by scheduling the task every 60 minutes
    
    5. All 3 tools (Postgres, Airflow, dbt) are run through Dockerfile and Docker Compose


# Lessons Learned

```text
Automation: Learned how to use the basics of Airflow to create a simple reoccurring task, and how to navigate the Airflow UI for DAG management.

Bash & Virtualization: The project was created using WSL & VSCode. Operations conducted were primarily through BASH scripts.

Collaboration: Learned how to use the .env variable as constant values to use for sensitive data. Learned how to properly commit and push changes via BASH.

Containerization: How to compose a Dockerfile and Docker Compose to create a consistent development environment for collaborative efforts.
