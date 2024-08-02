from typing import Dict

from pydantic import BaseModel


class MultiLangString(BaseModel):
    values: Dict[str, str]
