from fastapi import FastAPI
from backend.db import Base, engine
from backend.routes import products
from backend.routes import products, ingest
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# create tables in Neon
Base.metadata.create_all(bind=engine)

# include routes
app.include_router(products.router)
app.include_router(ingest.router)
app.mount("/", StaticFiles(directory="backend/static", html=True), name="static")
