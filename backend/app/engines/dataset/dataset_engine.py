from pathlib import Path

from app.engines.dataset.readers.csv_reader import CSVReader
from app.engines.dataset.readers.excel_reader import ExcelReader

class DatasetEngine:
        def __init__(self):
                self.csv_reader = CSVReader()
                self.excel_reader = ExcelReader()

        def get_dataset_metadata(self,dataset_path = Path):
                extension = dataset_path.suffix.lower()

                if extension == ".csv":
                        dataframe = self.csv_reader.read(dataset_path)

                elif extension == ".xlsx":
                        dataframe = self.excel_reader.read(dataset_path)

                else:
                        raise ValueError(
                                f"Unsupported dataset format: {extension}"
                        )    

                return{
                    "rows": len(dataframe),
                    "columns": len(dataframe.columns),
                    "column_names": list(dataframe.columns)
                }
        