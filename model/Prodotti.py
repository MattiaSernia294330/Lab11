from dataclasses import dataclass
@dataclass
class Prodotto:
    Product_number:int
    Product:str

    def __hash__(self):
        return hash(self.Product_number)
    def __str__(self):
        return f"{self.Product_number}"