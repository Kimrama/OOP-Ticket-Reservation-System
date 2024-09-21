from typing import List, Dict
import uvicorn
from fastapi import FastAPI
from datetime import time, datetime
from init_instance import system
from pydantic import BaseModel

app = FastAPI()

if __name__ == "__main__" :
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")

class Register(BaseModel):
    username: str
    name: str
    password: str
class Login(BaseModel):
    username: str
    password: str
class ChooseSeats(BaseModel):
    member_id: str
    train_id: str
    bogie_id: str 
    departure: str 
    destination: str 
    departure_time: str 
    destination_time: str 
    date: str 
    choosed_seat_id_list: List[str]

class ChooseMeal(BaseModel):
    reservation_id: str
    total_price_by_adding_food_from_UI: int
    meal_form: List[Dict[str, str]] 

class Pay(BaseModel):
    reservation_id: str
    payment_method: Dict[str, List[str]]
    coupon_id: str|None = None

class Cancel(BaseModel):
    member_id : str
    ticket_id : str
    departure_time : str
    date : str


@app.get("/root")
async def get_all_station() :
    all_station_list = system.get_all_station() 
    return all_station_list

@app.post("/register")
async def register(input : Register):
    response_status = system.register(
        input.username,
        input.name,
        input.password
    )
    return response_status

@app.post("/login")
async def login(input_login: Login):
    user = system.login(
        input_login.username,
        input_login.password
    )
    return user

@app.get("/route")
async def choose_route(departure: str, destination: str, choose_date: datetime, amount: int):
    result_route = system.choose_route(departure, destination, choose_date, amount)
    return result_route

@app.get("/train")
async def choose_train(train_id: str):
    bogies = system.choose_train(train_id)
    return bogies

@app.get("/bogie")
async def choose_bogie(train_id: str, bogie_id: str, departure_time: time, date: datetime):
    seats = system.choose_bogie(train_id, bogie_id, departure_time,date)
    return seats

@app.post("/seat")
async def choose_seat(input_seat : ChooseSeats):
    reservation = system.choose_seat(
        input_seat.member_id,
        input_seat.train_id,
        input_seat.bogie_id,
        input_seat.departure,
        input_seat.destination,
        input_seat.departure_time,
        input_seat.destination_time,
        input_seat.date,
        input_seat.choosed_seat_id_list
    )
    return reservation

@app.post("/meal")
async def choose_meal(input_meal : ChooseMeal):
    summary_data = system.choose_meal(
        input_meal.reservation_id,
        input_meal.total_price_by_adding_food_from_UI,
        input_meal.meal_form
    )
    return summary_data

@app.post("/pay")
async def pay(input_pay : Pay):
    ticket_list = system.pay(
        input_pay.reservation_id,
        input_pay.payment_method,
        input_pay.coupon_id
        )
    return ticket_list

@app.get("/view_ticket")
async def view_ticket(member_id: str) :
    ticket_list = system.view_ticket(member_id)
    return ticket_list

@app.delete("/cancel")
async def cancel(input_cancel : Cancel) :
    response_status = system.cancel(
        input_cancel.member_id,
        input_cancel.ticket_id,
        input_cancel.departure_time,
        input_cancel.date
    )
    return response_status

@app.get("/coupon")
async def coupon(member_id: str):
    return {"coupon" : system.add_coupon_available(member_id)}



    
@app.post("/add_seat_to_bogie", tags=["data manipuration"])
async def add_seat_to_bogie(train_id: str, bogie_id: str, amount: int) :
    response_status = system.add_seat_to_bogie(
        train_id,
        bogie_id,
        amount
    )
    return response_status

    
@app.post("/add_a_bogie_to_train", tags=["data manipuration"])
async def add_a_bogie_to_train(train_id: str) :
    response_status = system.add_a_bogie_to_train(
        train_id
    )
    return response_status

@app.post("/add_a_coupon_to_system", tags=["data manipuration"])
async def add_a_coupon_to_system(coupon_id: str, discount: int) :
    response_status = system.add_a_coupon_to_system(
        coupon_id,
        discount
    )
    return response_status

@app.delete("/delete_a_coupon_from_system", tags=["data manipuration"])
async def delete_a_coupon_from_system(coupon_id: str) :
    response_status = system.delete_a_coupon_from_system(coupon_id)
    return response_status

@app.delete("/delete_a_bogie_from_train", tags=["data manipuration"])
async def delete_a_bogie_from_train(train_id: str, bogie_id: str) :
    response_status = system.delete_a_bogie_from_train(train_id, bogie_id)
    return response_status

@app.delete("/delete_a_seat_from_bogie", tags=["data manipuration"])
async def delete_a_seat_from_bogie(train_id: str, bogie_id: str, seat_id: str) :
    response_status = system.delete_a_seat_from_bogie(train_id, bogie_id, seat_id)
    return response_status

@app.put("/change_coupon_discount", tags=["data manipuration"])
async def change_coupon_discount(coupon_id: str, new_discount: int) :
    response_status = system.change_coupon_discount(coupon_id, new_discount)
    return response_status
    
@app.put("/change_meal_price", tags=["data manipuration"])
async def change_meal_price(meal_id: str, new_price: int) :
    response_status = system.change_meal_price(meal_id, new_price)
    return response_status