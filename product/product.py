class Product:
    """
    Représente un fruit ou un légume vendu au kilo ou à l'unité.

    Attributes
    ----------
    name : str
        Product name./Nom du produit.
    price : float
        Product price./Prix du produit.
    stock : float
        Available quantity./Quantité disponible.
    unit : str
        'kg' or 'unit'.
    category : str
        'Fruit' or 'Vegetable'.
    """

    def __init__(self, name, price, stock, unit, category):
        self.name = name
        self.price = price
        self.stock = stock
        self.unit = unit
        self.category = category

    def sell(self, quantity):
        """
        Retire une quantité du stock.

        Parameters
        ----------
        quantity : float

        Returns
        -------
        bool
        True si la vente est possible.
        """
        if quantity <= self.stock:
            self.stock -= quantity
            return True
        return False

    def display(self):
        """
        Affiche les informations du produit.
        """
        print(f"{self.name:<20} {self.stock} {self.unit} - {self.price:.2f} €/ {self.unit}")