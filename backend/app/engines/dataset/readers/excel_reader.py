from pathlib import Path

import pandas as pd

class ExcelReader:

    def read(self,dataset_path: Path) -> pd.DataFrame :
        return pd.read_excel(dataset_path)