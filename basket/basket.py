class Basket:
    """
    Represents a customer's shopping basket.
    """

    def __init__(self):
        self.items = []

    def add(self, product, quantity):
        """
     Ajoute un produit au panier
     Parameters
     product :Product
     quantity : float
        """
        self.items.append((product, quantity))

    def total(self):
        """
        Calcule le montant total.

        Returns
        -------
        float
        """
        return sum(product.price * quantity for product, quantity in self.items)

    def receipt(self):
        """
       Affiche le ticket de caisse.
        """
        print("\n------ RECEIPT ------")

        for product, quantity in self.items:
            amount = product.price * quantity

            print(
                f"{product.name:<20}"
                f"{quantity} {product.unit}"
                f" x {product.price:.2f} = {amount:.2f} €"
            )

        print("---------------------")
        print(f"TOTAL : {self.total():.2f} €")