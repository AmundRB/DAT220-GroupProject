import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

print("🔧 Starting test_db.py")
print("➡️  DB config:")
print("   HOST:", os.getenv("DB_HOST"))
print("   USER:", os.getenv("DB_USER"))
print("   PASS:", os.getenv("DB_PASSWORD"))
print("   DB  :", os.getenv("DB_NAME"))

try:
    print("📡 Attempting mysql.connector.connect()...")
    conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    connection_timeout=5,
    auth_plugin='mysql_native_password',
    use_pure=True,  # ← forces pure Python driver to avoid C extension bugs
    allow_local_infile=True,  # optional but sometimes required
    raise_on_warnings=True
    )
    print("✅ Connected to DB.")
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    print("📦 Tables:", tables)
    conn.close()
except Exception as e:
    print("❌ ERROR:", e)
