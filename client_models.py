class Client:
    def __init__(self):
        self.items = []
    def clear(self):
        self.items.clear()
    def add_item(self,item):
        self.items.append(ClientAdapter(item))
    def show_items(self):
        pass

class ClientAdapter:
    def __init__(self,item):
        self.item = item
        self.count = int(input("Введіть кількітсть придбаного товару:"))
    def show(self):
        print(f""" придбаний товар - {self.item}
Кількість товару що придбали - {self.count}""")
