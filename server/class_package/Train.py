# * change train
import re


class Train:
    
    __train_id = "T000"
    def __init__(self):
        self.__train_id = Train.__train_id
        self.__bogie_list = []
        
        number_from_id = re.findall(r'\d', Train.__train_id)
        Train.__train_id = f"T{'{:03}'.format(int("".join(number_from_id)) + 1)}"

    def get_train_id(self):
        return self.__train_id

    def add_bogie(self, bogie):
        self.__bogie_list.append(bogie)

    def get_bogie_list(self):
        return self.__bogie_list
    
    def get_bogie_by_bogie_id(self, bogie_id) :
        for bogie in self.__bogie_list :
            if bogie.get_bogie_id() == bogie_id : return bogie
            
        return None
    def delete_bogie(self, bogie) :
        self.__bogie_list.remove(bogie)
        del bogie
        return "done"
