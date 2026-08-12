from pathlib import Path

import pandas as pd

class CSVReader:

    def read(self, dataset_path: Path) -> pd.DataFrame:
        return pd.read_csv(dataset_path)