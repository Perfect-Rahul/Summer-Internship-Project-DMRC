import mysql.connector
from datetime import datetime, timedelta

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Botchini143!",
        database="threat_db"
    )

def insert_ips(ip_list):
    conn = connect()
    cursor = conn.cursor()
    for ip in ip_list:
        cursor.execute("INSERT INTO ips_table (IP, Time) VALUES (%s, NOW())", (ip,))
    conn.commit()
    conn.close()

def insert_domains(domain_list):
    conn = connect()
    cursor = conn.cursor()
    for domain in domain_list:
        cursor.execute("INSERT INTO domains_table (DOMAIN, Time) VALUES (%s, NOW())", (domain,))
    conn.commit()
    conn.close()

def insert_hashes(hash_list):
    conn = connect()
    cursor = conn.cursor()
    for h in hash_list:
        cursor.execute("INSERT INTO hashes_table (HASH, Time) VALUES (%s, NOW())", (h,))
    conn.commit()
    conn.close()

def get_old_records(table_name):
    conn = connect()
    cursor = conn.cursor()
    ninety_days_ago = datetime.now() - timedelta(days=90)
    cursor.execute(f"SELECT * FROM {table_name} WHERE Time < %s", (ninety_days_ago,))
    old_records = cursor.fetchall()
    conn.close()
    return old_records

def delete_old_records(table_name):
    conn = connect()
    cursor = conn.cursor()
    ninety_days_ago = datetime.now() - timedelta(days=90)
    cursor.execute(f"DELETE FROM {table_name} WHERE Time < %s", (ninety_days_ago,))
    conn.commit()
    conn.close()
