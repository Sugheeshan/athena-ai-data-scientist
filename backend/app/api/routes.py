from fastapi import APIRouter
from app.services.health_service import HealthService

health_service = HealthService()
router = APIRouter()


@router.get("/")
def root():
    return{
        "message": "Welcome to Project Athena"
    }

@router.get("/health")
def health():
    return health_service.get_status()