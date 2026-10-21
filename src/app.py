import sqlite3

DBNAME = "MoviesInfo.db"

def init_db():
    conn = sqlite3.connect(DBNAME)
    conn.close()
#----------------
#init_db()

def create_table():
    query = '''
    CREATE TABLE IF NOT EXISTS movies
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    country TEXT,
    year TEXT,
    imdb_rate REAL
    )
    '''
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()        
#--------------
#create_table()  

def insert_record(title, country, year, imdb_rate):
    query = '''
    INSERT INTO movies(title, country, year, imdb_rate)
    VALUES (?, ?, ?, ?)
    '''
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(query,(title, country, year, imdb_rate))
    conn.commit()
    conn.close()
#--------------
#insert_record('Odyse', 'USA', '2026', 9.7)
#insert_record('OpenHimer', 'USA,Irland', '2025', 8.5)

def select_all_record():
    #query = 'SELECT * FROM movies'
    query_2 = 'SELECT title, country FROM movies'
    conn = sqlite3.connect(DBNAME)  
    cursor = conn.cursor()
    #rows = cursor.execute(query).fetchall()
    rows = cursor.execute(query_2).fetchall()
    
    conn.close
    return rows
#---------------
#print(select_all_record())

def select_record_by_id(id):
    query = 'SELECT * FROM movies WHERE id = ?'
    conn = sqlite3.connect(DBNAME)  
    cursor = conn.cursor()
    rows = cursor.execute(query,(id,)).fetchone()
    
    conn.close
    return rows
#---------------
#print(select_record_by_id(4))

def select_record_by_name(title):
    query = 'SELECT * FROM movies WHERE title = ?'
    conn = sqlite3.connect(DBNAME)  
    cursor = conn.cursor()
    rows = cursor.execute(query,(title,)).fetchone()
    
    conn.close
    return rows
#---------------
#print(select_record_by_name("OpenHimer"))

def delete_record_by_id(id):
    query = 'DELETE FROM movies WHERE id = ?'
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    conn.execute(query, (id,))
    conn.commit()
    conn.close()
#---------------
#delete_record_by_id(2)

def update_record_by_id(id, imdb_rate, year):
    query = '''UPDATE movies SET imdb_rate = ?, year =?
    WHERE id = ?''' 
    conn = sqlite3.connect(DBNAME) 
    cursor = conn.cursor()
    conn.execute(query,(imdb_rate, year, id))
    conn.commit()
    conn.close()
#--------------
update_record_by_id(3, 5.7, '2003')    
      
  