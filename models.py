class Category:
    def __init__(self,
                 name=""):
        self.name = name
        self.items = []
    def __str__(self):
        return self.name

categories = [Category("Без категорії")]


class Item:
    def __init__(self,
                 name,
                 price,
                 category_number=0):
        self.name = name
        self.price = price
        self.category_number = category_number
        self.category.items.append(self)
        
        
    @property
    def category(self):
        return categories[self.category_number]

    def __str__(self):
        return self.name
