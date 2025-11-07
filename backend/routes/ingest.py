from fastapi import APIRouter
from backend.services.admitad_ingest import ingest_garmin_products

router = APIRouter(prefix="/ingest", tags=["ingest"])

@router.post("/admitad")
def ingest_from_admitad():
    result = ingest_garmin_products()
    return result
