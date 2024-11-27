from dataclasses import dataclass
from typing import Optional

@dataclass
class Product:
    id: Optional[int]         # ID продукта, может быть None до сохранения в БД
    name: str                 # Название продукта
    description: str          # Описание продукта
    price: float              # Цена продукта
    category_id: int          # Категория, к которой принадлежит продукт
    available_quantity: int   # Доступное количество продукта

    def is_available(self) -> bool:
        """Проверяет, доступен ли продукт для покупки."""
        return self.available_quantity > 0

    def update_stock(self, quantity: int) -> None:
        """Обновляет количество на складе после покупки."""
        if quantity <= self.available_quantity:
            self.available_quantity -= quantity
        else:
            raise ValueError("Insufficient stock for the requested quantity.")
