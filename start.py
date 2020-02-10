from tuples import *

phones = [
    {
        "id": 1,
        "name": "Samsung",
        "model": "S10",
        "price": 16000
    },

    {
        "id": 2,
        "name": "iPhone",
        "model": "11",
        "price": 19000
    },

    {
        "id": 3,
        "name": "iPhone",
        "model": "8 Plus",
        "price": 12000
    },

    {
        "id": 4,
        "name": "Samsung",
        "model": "S8",
        "price": 9000
    },

    {
        "id": 5,
        "name": "iPhone",
        "model": "XR",
        "price": 17000
    }
]

sold_phones=[]

while True:
    print("===========================Sales Manager========================")
    choice = int(input(
        "1.Show Items\n2.Add Items\n3.Sort by price\n4.Sell item\n5.sell statistics\n6.delete item\n0.EXIT\n"))
    print("User choice=>", choice)
    if choice == 1:
        show_items(phones)
    elif choice == 2:
        add_item(phones)
        show_items(phones)
    elif choice == 3:
        show_items(phones)
        sort_by_price(phones)
    elif choice == 4:
        sold_phones.append(sell_phone(phones))
        show_items(phones)
        print(sold_phones)
    elif choice== 5:
        sell_statistics(len(sold_phones))
        show_items(phones)
    elif choice == 6:
        show_items(phones)
        delete_item(phones)
        show_items(phones)
    elif choice == 0:
        print("Bye!")
        break
    else:
        print("Read info!")
