from pathlib import Path
from fastapi import UploadFile
from app.core.config import settings
from app.engines.dataset.dataset_engine import DatasetEngine

class UploadService:

    UPLOAD_DIRECTORY = Path(settings.UPLOAD_DIRECTORY)

    ALLOWED_EXTENSIONS = {
        ".csv",
        ".xlsx"
    }

    dataset_engine = DatasetEngine()

    def save_file(self, file: UploadFile):
        self.UPLOAD_DIRECTORY.mkdir(
            parents=True, # "If any middle folders are missing, build them!"
            exist_ok=True # "If the folder is already there, don't panic, just skip it!"
        )
        
        extension = Path(file.filename).suffix.lower()

        if extension not in self.ALLOWED_EXTENSIONS:
            raise ValueError(
                "Only CSV and Excel files are supported."
            )

        destination = self.UPLOAD_DIRECTORY / file.filename

        with destination.open("wb") as buffer:

            buffer.write(file.file.read())

        metadata = self.dataset_engine.get_dataset_metadata(destination)

        return {
            "filename": file.filename,
            "location": str(destination),
            "metadata": metadata
        }