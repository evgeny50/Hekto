from dataclasses import dataclass
from typing import Optional

@dataclass
class Seller:
    id: Optional[int]
    name: str
    store_name: str
    email: str
    rating: float = 0.0

    def update_rating(self, new_rating: float) -> None:
        self.rating = new_rating
