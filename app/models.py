from typing import List
from pydantic import BaseModel, validator

from app.utils import clear_link


class UserData(BaseModel):
    links: List[str]

    @validator('links')
    def clean_links(cls, links: List[str]) -> List[str]:
        links = [clear_link(link) for link in links]
        links = sorted(set(links), key=links.index)
        return links
