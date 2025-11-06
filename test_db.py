from backend.db import engine
from sqlalchemy import text

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 'connected to Neon'"))
        print(result.scalar())
except Exception as e:
    print("Connection failed:", e)
