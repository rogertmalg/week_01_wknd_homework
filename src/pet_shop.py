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

# def find_pet_by_name(shop_name, pet_name):
#     found_pet = {}
#     for pet in shop_name["pets"]:
#         if pet["name"] == pet_name:
#             found_pet.update(pet)

#     return found_pet
# Changed above funtion to function bellow, this solves 10 and 11

def find_pet_by_name(shop_name, pet_name):
    found_pet = None
    for pet in shop_name["pets"]:
        if pet["name"] == pet_name:
            found_pet = pet

    return found_pet

def remove_pet_by_name(shop_name, pet_name):
    for pet in shop_name["pets"]:
        if pet["name"] == pet_name:
            shop_name["pets"].remove(pet)

def add_pet_to_stock(shop_name, new_pet):
    shop_name["pets"].append(new_pet)