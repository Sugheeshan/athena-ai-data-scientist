from pathlib import Path
from fastapi import UploadFile
from app.core.config import settings

class UploadService:

    UPLOAD_DIRECTORY = Path(settings.UPLOAD_DIRECTORY)

    ALLOWED_EXTENSIONS = {
        ".csv",
        ".xlsx"
    }

    def save_file(self, file: UploadFile):
        self.UPLOAD_DIRECTORY.mkdir(
            parents=True,
            exist_ok=True
        )
        
        extension = Path(file.filename).suffix.lower()

        if extension not in self.ALLOWED_EXTENSIONS:
            raise ValueError(
                "Only CSV and Excel files are supported."
            )

        destination = self.UPLOAD_DIRECTORY / file.filename

        with destination.open("wb") as buffer:

            buffer.write(file.file.read())

        return {
            "filename": file.filename,
            "location": str(destination)
        }