from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root():
    return{
        "message": "Welcome to Project Athena"
    }

@router.get("/health")
def health():
    return{
        "status": "Healthy"
    }