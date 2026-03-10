import os
import psycopg2
from dotenv import load_dotenv
from api_request import fetch_data

load_dotenv()

#Creates a connection to the PostgreSQL db
def connect_to_db():
    print("Connecting to PostgresQL DB...")
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST","localhost"),
            port=int(os.getenv("DB_PORT",5432)),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        return conn
    except psycopg2.Error as e:
        print(f"Database failed to connect: {e}")
        raise

#Creates the table for the data to injested. Also creates the schema
def create_table(conn):
    print("Creating table if not exist...")
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE SCHEMA IF NOT EXISTS dev;
            CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
                id SERIAL PRIMARY KEY,
                city TEXT,
                temperature FLOAT,
                weather_descriptions TEXT,
                wind_speed FLOAT,
                time TIMESTAMP,
                inserted_at TIMESTAMP DEFAULT NOW(),
                utc_offset TEXT
            );
        """)
        conn.commit()
        print("Table was created.")
    except psycopg2.Error as e:
        print(f"Failed to create table: {e}")
        raise

#Inserts the records from the request
def insert_records(conn, data):
    try:
        print("Inserting data")
        #Assigning weather and location from the object for visual clarity in insertion
        weather = data['current']
        location = data['location']
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO dev.raw_weather_data (
                    city,
                    temperature,
                    weather_descriptions,
                    wind_speed,
                    time,
                    inserted_at,
                    utc_offset) VALUES (%s,%s,%s,%s,%s,NOW(),%s)
            """,(
                location['name'],
                weather['temperature'],
                weather['weather_descriptions'][0],
                weather['wind_speed'],
                location['localtime'],
                location['utc_offset']
        ))
        conn.commit()
    except psycopg2.Error as e:
        print(f"Error inserting data into database: {e}")


def main():
    try:
        data = fetch_data()
        conn = connect_to_db()
        create_table(conn)
        insert_records(conn,data)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
            print("Close connection")

if __name__ == "__main__":
    main()