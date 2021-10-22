# WRITE YOUR FUNCTIONS HERE

import pdb
# pdb.set_trace()


def get_pet_shop_name(shop_name):
    return shop_name["name"]

def get_total_cash(shop_name):
    return shop_name["admin"]["total_cash"]

def add_or_remove_cash(shop_name, amount): 
   shop_name["admin"]["total_cash"] += amount
# this solves 3 and 4 

def get_pets_sold(shop_name):
    return shop_name["admin"]["pets_sold"]

def increase_pets_sold(shop_name, number_pets): 
    shop_name["admin"]["pets_sold"] += number_pets

def get_stock_count(shop_name):
    return len(shop_name["pets"])

def get_pets_by_breed(shop_name, breed_name):
    pets_breed = []
    for pet in shop_name["pets"]:
        if pet["breed"] == breed_name:
            pets_breed.append(pet)

    return pets_breed
# this solves 8 and 9

# def find_pet_by_name(shop_name, shop_pet):
#     found_pet = {}
#     for pet in shop_name["pets"]:
#         if pet["name"] == shop_pet:
#             found_pet.update(pet)

#     return found_pet
# Changed above funtion to function bellow, this solves 10 and 11

def find_pet_by_name(shop_name, shop_pet):
    found_pet = None
    for pet in shop_name["pets"]:
        if pet["name"] == shop_pet:
            found_pet = pet

    return found_pet

def remove_pet_by_name(shop_name, shop_pet):
    for pet in shop_name["pets"]:
        if pet["name"] == shop_pet:
            shop_name["pets"].remove(pet)

def add_pet_to_stock(shop_name, new_pet):
    shop_name["pets"].append(new_pet)

def get_customer_cash(customer_index):
    return customer_index["cash"]

def remove_customer_cash(customer_index, cash_amout):
    customer_index["cash"] -= cash_amout

def get_customer_pet_count(customer_index):
    return len(customer_index["pets"])

def add_pet_to_customer(customer_index, new_pet):
    customer_index["pets"].append(new_pet)

# Optional Exercises 

def customer_can_afford_pet(customer_index, new_pet):
    can_afford = False
    if customer_index["cash"] >= new_pet["price"]:
        can_afford = True
    return can_afford
# solves 18, 19 and 20 

# Integration tests

def sell_pet_to_customer(shop_name, shop_pet, customer_index):
    if shop_pet == None:
        print("We do not have this pet")

    elif customer_index["cash"] >= shop_pet["price"]:
    
        amount = shop_pet["price"]
        number_pets = 1
        customer_index["pets"].append(shop_pet)
        remove_pet_by_name(shop_name, shop_pet)
        increase_pets_sold(shop_name, number_pets)
        add_or_remove_cash(shop_name, amount)
        remove_customer_cash(customer_index, amount)

    else:
        print("you cant afford this pet")

# for the if and else statement, if I don't add an indented line under I get an error
# I thought I would be able to use the if withtout anything happening if true
# the work around was to print something after it, so I added the else as it also prints something 
# when the customer cant afford, the else is not needed tho. 

        