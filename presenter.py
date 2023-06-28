from models import(Category,
                   Item,
                   categories)

from client_models import ClientAdapter

def numeration (data2):
    for number, data in enumerate(data2,1):
        print(number,data)
    return number

def check_data(number):
    if number.isdigit() and 0 < int(number) <= len(categories):
        return int(number) - 1

def choose_category(categories):
    numeration(categories)
    number = input("Оберіть номер категорії:")
    return check_data(number)

items = []   

def admin_menu():
    global categories,items
    while True:
        choice = input("""1 create category
2 view categories
3 create items
4 view items
5 show one category
6 exit:""")
        if choice == "1":
            category = Category(input("Назва категорії:"))
            categories.append(category)
            print("ДОдано")
            
        if choice == "2":
            numeration(categories)
                
        if choice == "3":
            category_number = choose_category(categories)
            if category_number is None:
                category_number = 0
            item = Item(name=input("Назва товару:"),
                        price=input("Ціна товару:"),
                        category_number=category_number)
            items.append(item)
        
            
        if choice == "4":
            for number,item in enumerate(items,1):
                print(number,item)
                
        if choice == "5":
            category_number = choose_category(categories)
            if category_number is not None:
                category = categories[category_number]
                print("Товари категорії")
                numeration(self.items)
                print("-"*20)
                    
        if choice == "6":
            break

def get_item_number(items):
    numeration(items)
    number = input("Введіть номер товару:")
    return check_data(number)

def client_menu(client):
    global items,categories
    while True:
        choice = input("1 додати товар 2 подивитись додані товари 3 вийти:")
        if choice == "1":
            item_number = get_item_number(items)
            if item_number is not None:
                item = items[item_number]
                client.add_item(item)
 
        if choice == "2":
            for item in client.items:
                item.show()
        
        if choice == "3":
            break
