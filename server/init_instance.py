from class_package import TicketReservationSystem, Member, Station, Train, Bogie, Seat, Reminder, Route, Meal, Coupon, Reservation, SeatInUse, Ticket, User
from datetime import time
from class_package import *

# * main
system = TicketReservationSystem()

# * init member

# * init station
A_station = Station("สถานีกลางกรุงเทพอภิวัฒน์")
B_station = Station("นครสวรรค์")
C_station = Station("พิจิตร")
D_station = Station("พิษณุโลก")


E_station = Station("สระบุรี")
F_station = Station("นครราชสีมา")
G_station = Station("สุรินทร์")
station_list = [A_station, B_station, C_station, D_station, E_station, F_station, G_station]

# * init train
train001 = Train()
train002 = Train()
train003 = Train()
train004 = Train()

# * init bogie
bogie001 = Bogie()
bogie002 = Bogie()
bogie_train001 = [bogie001, bogie002]

bogie003 = Bogie()
bogie004 = Bogie()
bogie_train002 = [bogie003, bogie004]

bogie005 = Bogie()
bogie006 = Bogie()
bogie_train003 = [bogie005, bogie006]

bogie007 = Bogie()
bogie008 = Bogie()
bogie_train004 = [bogie007, bogie008]

# * init seat
seat001 = Seat()
seat002 = Seat()
seat003 = Seat()
seat004 = Seat()
seat005 = Seat()
seat_bogie001 = [seat001, seat002, seat003, seat004, seat005]

seat006 = Seat()
seat007 = Seat()
seat008 = Seat()
seat009 = Seat()
seat010 = Seat()
seat_bogie002 = [seat006, seat007, seat008, seat009, seat010]

seat011 = Seat()
seat012 = Seat()
seat013 = Seat()
seat014 = Seat()
seat015 = Seat()

seat_bogie003 = [seat011, seat012, seat013, seat014, seat015]

seat016 = Seat()
seat017 = Seat()
seat018 = Seat()
seat019 = Seat()
seat020 = Seat()

seat_bogie004 = [seat016, seat017, seat018, seat019, seat020]

seat021 = Seat()
seat022 = Seat()
seat023 = Seat()
seat024 = Seat()
seat025 = Seat()

seat_bogie005 = [seat021, seat022, seat023, seat024, seat025]

seat026 = Seat()
seat027 = Seat()
seat028 = Seat()
seat029 = Seat()
seat030 = Seat()

seat_bogie006 = [seat026, seat027, seat028, seat029, seat030]

seat031 = Seat()
seat032 = Seat()
seat033 = Seat()
seat034 = Seat()
seat035 = Seat()

seat_bogie007 = [seat031, seat032, seat033, seat034, seat035]

seat036 = Seat()
seat037 = Seat()
seat038 = Seat()
seat039 = Seat()
seat040 = Seat()

seat_bogie008 = [seat036, seat037, seat038, seat039, seat040]

# Define the reminders for route 1
route1_station_a = Reminder(A_station, time(0, 0))
route1_station_b = Reminder(B_station, time(3, 0))
route1_station_c = Reminder(C_station, time(6, 0))
route1_station_d = Reminder(D_station, time(9, 0))

# Define the reminders for route 2
route2_station_d = Reminder(D_station, time(12, 0))
route2_station_c = Reminder(C_station, time(15, 0))
route2_station_b = Reminder(B_station, time(18, 0))
route2_station_a = Reminder(A_station, time(21, 0))

# Define the reminders for route 3
route3_station_a = Reminder(A_station, time(12, 0))
route3_station_b = Reminder(B_station, time(15, 0))
route3_station_c = Reminder(C_station, time(18, 0))
route3_station_d = Reminder(D_station, time(21, 0))

# Define the reminders for route 4
route4_station_d = Reminder(D_station, time(0, 0))
route4_station_c = Reminder(C_station, time(3, 0))
route4_station_b = Reminder(B_station, time(6, 0))
route4_station_a = Reminder(A_station, time(9, 0))

# Define the reminder for route 5
route5_station_a = Reminder(A_station, time(0, 0))
route5_station_e = Reminder(E_station, time(3, 0))
route5_station_f = Reminder(F_station, time(6, 0))
route5_station_g = Reminder(G_station, time(9,0))

#define the reminder for route 6
route6_station_g = Reminder(G_station, time(12, 0))
route6_station_f = Reminder(F_station, time(15, 0))
route6_station_e = Reminder(E_station, time(18, 0))
route6_station_a = Reminder(A_station, time(21, 0))

# Define the reminder for route 7
route7_station_a = Reminder(A_station, time(21, 0))
route7_station_e = Reminder(E_station, time(18, 0))
route7_station_f = Reminder(F_station, time(15, 0))
route7_station_g = Reminder(G_station, time(12,0))

#define the reminder for route 8
route8_station_g = Reminder(G_station, time(9, 0))
route8_station_f = Reminder(F_station, time(6, 0))
route8_station_e = Reminder(E_station, time(3, 0))
route8_station_a = Reminder(A_station, time(0, 0))

station_route1 = [
    route1_station_a, route1_station_b, route1_station_c, route1_station_d
]

station_route2 = [
    route2_station_d, route2_station_c, route2_station_b, route2_station_a
]

station_route3 = [
    route3_station_a, route3_station_b, route3_station_c, route3_station_d
]

station_route4 = [
    route4_station_d, route4_station_c, route4_station_b, route4_station_a
]

station_route5 = [
    route5_station_a, route5_station_e, route5_station_f, route5_station_g
]

station_route6 = [
    route6_station_g, route6_station_f, route6_station_e, route6_station_a
]

station_route7 = [
    route7_station_a, route7_station_e, route7_station_f, route7_station_g
]

station_route8 = [
    route8_station_g, route8_station_f, route8_station_e, route8_station_a
]

# *init route
route1 = Route(train001, station_route1)
route2 = Route(train001, station_route2)
route3 = Route(train002, station_route3)
route4 = Route(train002, station_route4)
route5 = Route(train003, station_route5)
route6 = Route(train003, station_route6)
route7 = Route(train004, station_route7)
route8 = Route(train004, station_route8)

# *add route
system.add_route_list(route1)
system.add_route_list(route2)
system.add_route_list(route3)
system.add_route_list(route4)
system.add_route_list(route5)
system.add_route_list(route6)
system.add_route_list(route7)
system.add_route_list(route8)


# *add member


# *add station list
for station in station_list:
    system.add_station_list(station)
# * fill data

for seat in seat_bogie001:
    bogie001.add_seat(seat)

for seat in seat_bogie002:
    bogie002.add_seat(seat)

for seat in seat_bogie003:
    bogie003.add_seat(seat)

for seat in seat_bogie004:
    bogie004.add_seat(seat)

for seat in seat_bogie005:
    bogie005.add_seat(seat)

for seat in seat_bogie006:
    bogie006.add_seat(seat)

for seat in seat_bogie007:
    bogie007.add_seat(seat)

for seat in seat_bogie008:
    bogie008.add_seat(seat)

for bogie in bogie_train001:
    train001.add_bogie(bogie)

for bogie in bogie_train002:
    train002.add_bogie(bogie)

for bogie in bogie_train003:
    train003.add_bogie(bogie)

for bogie in bogie_train004:
    train004.add_bogie(bogie)

#add meal
food1 = Meal(50)
food2 = Meal(60)
food3 = Meal(70)
food4 = Meal(80)
food5 = Meal(30)
system.add_meal(food1)
system.add_meal(food2)
system.add_meal(food3)
system.add_meal(food4)
system.add_meal(food5)
#add coupon
coupon2 = Coupon("4220",10)
system.add_coupon(coupon2)