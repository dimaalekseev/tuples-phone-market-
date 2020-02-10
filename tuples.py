# a = [1, 22, 44, 48, 52, "Bill"]
# b = ["Monday", "Tuesday", "Wednesday"]

# c = tuple(a+b)

# print(c)
# print(type(c))
# print(c[-1])


# d = "Bill", 28, "Admin"
# print(type(d))


# name, age, role = d
# print(name)
# print(age)
# print(role)


# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married


# user = get_user()
# print(user[0])              # Tom
# print(user[1])              # 22
# print(user[2])              # False

# print(type(user))


# for item in phones:
#     print(item["name"], item["model"], item["price"], "\n")


if __name__ == "__main__":
    add_item()
    show_items()
    delete_item()


def add_item(phones):
    name = input("Vendor name: ")
    model = input("Model: ")
    price = input("Price: ")

    phones.append({
        "id": len(phones)+1,
        "name": name,
        "model": model,
        "price": price
    })


def show_items(phones):
    for item in phones:
        print(item["id"], item["name"].join("||"),
              item["model"].join("||"), str(item["price"]).join("||"))


def delete_item(phones):
    delete = int(input("Enter a num of item to delete"))-1
    phones.pop(delete)


def sort_by_price(phones):
    sort_by = int(
        input("How'd you like to sort by? \nID : 1\nPrice : 2\nName : 3\n=>:"))
    if sort_by == 1:
        sort_by = "id"
    elif sort_by == 2:
        sort_by = "price"
    else:
        sort_by = "name"

    sorted_items = sorted(phones, key=lambda item: item[sort_by])
    print(sorted_items)
    return sorted_items


def sell_phone(phones):
    print(phones)   
    sold = int(input("Enter a num of phone u wanna buy: "))
    for item in phones:
        return item["id"].pop(sold) #int object has not attribute pop??


def sell_statistics(sold_phones): 
    print("[", sold_phones, "]-- Items was sold")
    input("Enter to continue")