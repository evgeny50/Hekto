from dataclasses import dataclass
from typing import Optional
from core.entities.product import Product
from core.entities.buyer import Buyer

@dataclass
class ProductReview:
    id: Optional[int]
    product: Product
    buyer: Buyer
    rating: float
    comment: Optional[str] = None

    def is_positive(self) -> bool:
        return self.rating >= 4
