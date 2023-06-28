from presenter import (admin_menu,
                       client_menu)

from client_models import Client

while True:
    choice = input("1 admin 2 client 3 exit")
    if choice  == "1":
        admin_menu()
    if choice == "2":
        client_menu(Client())
    if choice == "3":
        break
