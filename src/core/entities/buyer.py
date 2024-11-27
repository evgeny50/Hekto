from dataclasses import dataclass
from typing import Optional


@dataclass
class Buyer:
    id: Optional[int]
    name: str
    email: str
    address: str

    def update_address(self, new_address: str) -> None:
        self.address = new_address
