import re

class Hotel:
    def __init__(self, name, rate, weekday_regular, weekend_regular, weekday_reward, weekend_reward):
            self.name = name
            self.rate = rate
            self.weekday_regular = weekday_regular
            self.weekend_regular = weekend_regular
            self.weekday_reward = weekday_reward
            self.weekend_reward = weekend_reward

    def Diaria(self, customer, day):
        weekday = ["mon","tue","wed","thu","fri"]
        if customer == "Regular":
            if day in weekday:
                return self.weekday_regular
            else:
                return self.weekend_regular
        else:
            if day in weekday:
                return self.weekday_reward
            else:
                return self.weekend_reward

lakewood = Hotel("Lakewood", 3, 110, 90, 80, 80)
bridgewood = Hotel("Bridgewood", 4, 160, 60, 110, 50)
ridgewood = Hotel("Ridgewood", 5, 220, 150, 100, 40)

def split_input(input_text):
    return 0

def get_cheapest_hotel(number):   #DO NOT change the function's name
    cheapest_hotel = "cheapest_hotel_name"
    return cheapest_hotel



while(1):
    reserva = input("Bem vindo! Informe o tipo de cliente e as datas para encontrar o hotel mais barato ou digite 'sair' para encerrar o programa")
    if reserva != 'sair':
        print(reserva)
        reserva
        print(split_input(reserva[0]))
    else:
        break