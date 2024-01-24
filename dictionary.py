phone1 = {
    "brand" : "sansung",
    "model" : "galaxy 10",
    "capacity" : "256 GB",
    "color" : "dark green"
}

#print(phone["model"])
#print(phone.get("color", "there is no information on this"))

#if "model" in phone:
#    print(phone["model"])
#else:
#    print("there is no information on this. ")

#phone["capacity"] = "1 TB"
#print(phone)

#phone.popitem()
#print(phone)

#phone.clear()
#print(phone)

#for specification规格 in phone.items():
#    print(specification规格)
#for specification规格 in phone.keys():
#    print(specification规格)
#for specification规格 in phone.values():
#    print(specification规格)

#for title, specification规格 in phone.items():
#    print(f"{title} is {specification规格}")

phone2= {
    "brand" : "meizu",
    "model" : "meizu6",
    "capacity" : "128 GB",
    "color" : "yellow"
}

phone3 = {
    "brand" : "huawei",
    "model" : "rongyao10",
    "capacity" : "512 GB",
    "color" : "blood red"
}

#inventory = [phone1, phone2, phone3]
##print(inventory[1]["color"])

#inventory = [phone1, phone2, phone3]
#check = input("please enter the brand you wanna check:")
#if check in str(inventory):
#    print("in stock")
#else:
#    print("out of stock")

inventory = [phone1, phone2, phone3]
check = input("please enter the brand you wanna check:")
if check in str(inventory):
    for phone in inventory:
        if phone["brand"] == check:
            print(f"{phone['color']} {phone['model']}, capacity is {phone['capacity']} is in stock right now")
else:
    print("currently there is no{check} in stock")