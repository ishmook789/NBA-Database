import sqlite3
import pandas as pd

from sqlalchemy import create_engine

csv_file = "pythondb.csv"

df = pd.read_csv(csv_file)




def create_database():
    conn = sqlite3.connect("nba.db")
    cursor = conn.cursor()

    # Create table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS nbatable4 (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        pos TEXT NOT NULL,
        age INTEGER,
        team TEXT NOT NULL,
        FG FLOAT,
        Three FLOAT,
        FT FLOAT,
        points FLOAT
        
        
        


    )
    ''')

        # Insert sample data
    df.to_sql("nbatable4", conn, if_exists='replace', index=False)
    
    

    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_database()
