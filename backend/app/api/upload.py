from fastapi import APIRouter
from fastapi import File
from fastapi import HTTPException
from fastapi import UploadFile 

from app.services.upload_service import UploadService

router = APIRouter()

upload_service = UploadService()

@router.post("/upload")
def upload_dataset(
    file: UploadFile = File(...)
):
    try:

        result = upload_service.save_file(file)

        return result 

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )
