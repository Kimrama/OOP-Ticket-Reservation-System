# * change bogie
import re

class Bogie:
    
    __bogie_id = "B000"
    
    def __init__(self):
        self.__bogie_id = Bogie.__bogie_id
        self.__seat_list = []
        
        number_from_id = re.findall(r'\d', Bogie.__bogie_id)
        Bogie.__bogie_id = f"B{'{:03}'.format(int("".join(number_from_id)) + 1)}"

    def add_seat(self, seat):
        self.__seat_list.append(seat)

    # add
    def get_bogie_id(self):
        return self.__bogie_id

    # add
    def get_seat_list(self):
        return self.__seat_list

    # add
    def get_destination_time(self):
        return self.__destination_time
    
    def delete_all_seat(self):
        for seat in self.__seat_list :
            self.__seat_list.remove(seat)
            del seat
            return "done"
        
    def delete_seat(self, seat_id) :
        for seat in self.__seat_list :
            if seat.get_seat_id() == seat_id :
                self.__seat_list.remove(seat) 
                del seat
                return "done"
        return "fail"
        
    