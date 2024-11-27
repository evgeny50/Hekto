from dataclasses import dataclass, field
from typing import List, Optional
from core.entities.product import Product

@dataclass
class OrderItem:
    product: Product
    quantity: int

    def total_price(self) -> float:
        return self.product.price * self.quantity

@dataclass
class Order:
    id: Optional[int]
    buyer_id: int
    items: List[OrderItem] = field(default_factory=list)
    status: str = "Pending"

    def add_item(self, item: OrderItem) -> None:
        self.items.append(item)

    def calculate_total_price(self) -> float:
        return sum(item.total_price() for item in self.items)

    def is_complete(self) -> bool:
        return self.status == "Complete"
