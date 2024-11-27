from dataclasses import dataclass
from typing import Optional

@dataclass
class Category:
    id: Optional[int]
    name: str
    description: Optional[str] = None

