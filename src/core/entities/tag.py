from dataclasses import dataclass
from typing import Optional

@dataclass
class Tag:
    id: Optional[int]
    name: str
    description: Optional[str] = None
