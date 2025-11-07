import requests
from sqlalchemy import text
from backend.services.admitad_auth import get_access_token
from backend.db import SessionLocal
from backend.models.product import Product


def fetch_garmin_products():
    token_data = get_access_token()
    access_token = token_data["access_token"]

    url = "https://api.admitad.com/advcampaigns/"
    headers = {"Authorization": f"Bearer {access_token}"}
    params = {"limit": 20, "offset": 0, "website": 1}  # 1 = default ad space
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    return data


def ingest_garmin_products():
    # fetch data from Admitad
    data = fetch_garmin_products()

    # open DB session
    db = SessionLocal()

    # test database connection
    try:
        db.execute(text("SELECT 1"))
        print("DB connection OK")
    except Exception as e:
        print("DB connection failed:", e)
        db.close()
        raise

    count = 0

    try:
        for item in data.get("results", []):
            name = item.get("name", "")
            if "garmin" in name.lower():
                price = 0.0  # Admitad programs don’t include price yet
                product = Product(name=name, price=price)
                db.add(product)
                count += 1
        db.commit()
        print(f"{count} Garmin items inserted.")
    except Exception as e:
        db.rollback()
        print("Error during ingestion:", e)
        raise
    finally:
        db.close()

    return {"inserted": count}
