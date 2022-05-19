import re

class Hotel:
    def __init__(self, name:str, rate:int, week_prices:list[int], weeknd_prices:list[int]) -> None:
        self.name = name
        self.rate = rate
        self.week_prices = week_prices
        self.weeknd_prices = weeknd_prices

    def estimate(self, client_type, client_dates):
        client_price = 0 if client_type == "Regular" else 1
        total = 0

        for date in client_dates:
            if "sat" == date or "sun" == date:
                total += self.weeknd_prices[client_price]
            else:
                total += self.week_prices[client_price]

        return total

def __get_hotels():
    hotel_1 = Hotel("Lakewood"  , 3, [110,80] , [90,80])
    hotel_2 = Hotel("Bridgewood", 4, [160,110], [60,50])
    hotel_3 = Hotel("Ridgewood" , 5, [220,100], [150,40])

    return [hotel_1,hotel_2,hotel_3]

def get_client_type(input):
    return input.split(":")[0]

def get_client_dates(input):
    res = re.findall(r'\(.*?\)', input)
    res = [re.sub("[()]","", s) for s in res]
    return res

def __get_totals(type, dates, hotels):
    res = []
    for hotel in hotels:
        res.append([hotel.name, hotel.rate, hotel.estimate(type, dates)])
    return res

def get_cheapest_hotel(number):   #DO NOT change the function's name
    client_type = get_client_type(number)
    client_dates = get_client_dates(number)
    hotels = __get_hotels()
    
    totals = __get_totals(client_type, client_dates, hotels)

    # sorts by price then by rate
    sorted_totals = sorted(totals, key=lambda x: [x[2],-x[1]])
    
    cheapest_hotel = sorted_totals[0][0]

    return cheapest_hotel