class Employee:
    def __init__(self, name, sale):
        self.name = name
        self.sale = sale

    def give_raise(self, risen=5000):
        self.sale  = self.sale + risen