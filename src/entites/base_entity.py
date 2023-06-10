from typing import Optional, Union

import httpx
import pandas as pd

from error_messages import DataNotFound, DataParsingError


class BaseEntity:
    api_url = None

    def fetch(self, url: str) -> dict:
        try:
            response = httpx.get(url)
            if response.status_code == 200 and (json_data := response.json()):
                return json_data
            else:
                raise DataNotFound
        except Exception as e:
            raise DataNotFound(f"Data from {self.api_url} is not found")

    def data(self, id: Optional[int] = None) -> pd.DataFrame:
        try:
            id = f"/{id}" if id else ""
            json_data = self.fetch(f"{self.api_url}{id}")
            json_data = [json_data] if id else json_data
            df = pd.DataFrame(json_data)
            return df
        except DataNotFound:
            raise DataNotFound
        except Exception:
            raise DataParsingError
