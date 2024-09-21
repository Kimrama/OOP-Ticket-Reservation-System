#change
import re


class Meal:
    
    __meal_id = "M000"
    def __init__(self, price):
        self.__meal_id = Meal.__meal_id
        self.__price = price
        
        number_from_id = re.findall(r'\d', Meal.__meal_id)
        Meal.__meal_id = f"M{'{:03}'.format(int("".join(number_from_id)) + 1)}"

    def get_meal_id(self) :
        return self.__meal_id
    def get_price(self) :
        return self.__price
    def update_price(self, new_price) :
        self.__price = new_price