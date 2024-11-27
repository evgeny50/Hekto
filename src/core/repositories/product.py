from abc import ABC, abstractmethod
from core.entities.product import Product


class ProductRepository(ABC):
    @abstractmethod
    def get_all_products(self) -> list[Product]:
        pass

    @abstractmethod
    def get_product_by_id(self, product_id: int) -> Product:
        pass

    @abstractmethod
    def save_product(self, product: Product) -> None:
        pass
