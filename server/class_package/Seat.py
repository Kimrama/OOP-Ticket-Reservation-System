import re


class Seat:
    
    __seat_id = "S000"
    def __init__(self):
        self.__seat_id = Seat.__seat_id
        
        number_from_id = re.findall(r'\d', Seat.__seat_id)
        Seat.__seat_id = f"S{'{:03}'.format(int("".join(number_from_id)) + 1)}"

    def get_seat_id(self):
        return self.__seat_id

    def get_seat_position(self):
        return self.__seat_position