# WRITE YOUR FUNCTIONS HERE

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