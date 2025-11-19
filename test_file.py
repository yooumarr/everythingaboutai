import sqlite3
import os

def get_user_data(user_id):
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

def process_logs():
    with open('logs.txt', 'r') as f:
        lines = f.readlines()
    output = []
    for i in range(len(lines)):
        if "ERROR" in lines[i]:
            output.append("Found error at line " + str(i))
    return output

def calculate_total(items):
 total=0
 for item in items:
     total+=item['price']
 return total