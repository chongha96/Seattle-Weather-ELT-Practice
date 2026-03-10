-- SQL file to create tables to be turned into reports

{{config (
    materialized='table',
    unique_key='id'
)}}

select *
from {{ref('stg_weather_data')}}