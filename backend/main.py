from fastapi import FastAPI
from backend.db import Base, engine
from backend.routes import products

app = FastAPI()

# create tables in Neon
Base.metadata.create_all(bind=engine)

# include routes
app.include_router(products.router)
