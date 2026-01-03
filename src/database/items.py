from dataclasses import dataclass
from typing import Optional


@dataclass
class Item:
    item_name: Optional[str]
    item_value: Optional[str]
    item_descp: Optional[str]
    item_image: Optional[list[str]]
