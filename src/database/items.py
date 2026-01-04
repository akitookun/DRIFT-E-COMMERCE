from dataclasses import dataclass, field
from typing import Optional, List
from bson import ObjectId


@dataclass
class Item:
    item_name: Optional[str]
    item_value: float
    item_descp: Optional[str]
    item_image: List[str] = field(default_factory=list)
    _id: Optional[ObjectId] = None
