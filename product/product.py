class Product:
    """
    Represents a fruit or a vegetable sold by weight or by unit.

    Attributes
    ----------
    name : str
        Product name.
    price : float
        Product price.
    stock : float
        Available quantity.
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
        Removes a quantity from the stock.

        Parameters
        ----------
        quantity : float

        Returns
        -------
        bool
            True if the sale can be completed.
        """
        if quantity <= self.stock:
            self.stock -= quantity
            return True
        return False

    def display(self):
        """
        Displays the product information.
        """
        print(f"{self.name:<20} {self.stock} {self.unit} - {self.price:.2f} €/ {self.unit}")