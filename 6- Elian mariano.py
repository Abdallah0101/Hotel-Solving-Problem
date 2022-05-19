import re

# 1st index: lakewood, 2nd index bridgewood, 3rd index ridgewood
hotels = [
    {"star": 3, "regular": {"week_day": 110, "weekend": 90}, "rewards": {"week_day": 80, "weekend": 80}},
    {"star": 4, "regular": {"week_day": 160, "weekend": 60}, "rewards": {"week_day": 110, "weekend": 50}},
    {"star": 5, "regular": {"week_day": 220, "weekend": 150}, "rewards": {"week_day": 100, "weekend": 40}}
]

def parseInput(input):
    # Get client type: Regular or Rewards
    client_type = re.search(r'(\w+)(?=:)', input).group(1)

    # Raise an error if client type is unknown
    if client_type != "Regular" and client_type != "Rewards":
        raise ValueError("Client type should be Regular or Rewards")

    # Get all days of the week in which client will be found
    days_of_the_week = re.findall(r"(?<=\()(\w+)", input)

    return (client_type, days_of_the_week)

# Returns True if day is weekend
def is_weekend(day): return day == "sat" or day == 'sun'

# Calculate result by hotel
def result_by_hotel(hotel, client_type, days_of_the_week):
    result = 0

    for i in range(0, len(days_of_the_week)):
        if client_type == "Regular" and is_weekend(days_of_the_week[i]):
            result += hotel["regular"]["weekend"]
        elif client_type == "Regular" and not is_weekend(days_of_the_week[i]):
            result += hotel["regular"]["week_day"]
        elif client_type == "Rewards" and is_weekend(days_of_the_week[i]):
            result += hotel["rewards"]["weekend"]
        elif client_type == "Rewards" and not is_weekend(days_of_the_week[i]):
            result += hotel["rewards"]["week_day"]
    
    return result

# Calculate the price of the Hotel
def calculate(client_type, days_of_the_week):
    result = ()
    for i in range(len(hotels)):
        result = (*result, result_by_hotel(hotels[i], client_type, days_of_the_week))

    return result

# Compare the hotels result
def compare_hotels_result(result):
    maxindex, maxvalue = 0, result[0]

    for i in range(0, len(result)):
        if result[i] < maxvalue:
            maxindex = i
            maxvalue = result[i]
        elif result[i] == maxvalue and hotels[i]['star'] > hotels[maxindex]['star']:
            maxindex = i
            maxvalue = result[i]
    
    if maxindex == 0:
        return "Lakewood"
    if maxindex == 1:
        return "Bridgewood"
    return "Ridgewood"

def get_cheapest_hotel(number):   #DO NOT change the function's name
    # Parse the number
    client_type, days_week = parseInput(number)
    # Each hotel result inside a tuple
    result = calculate(client_type, days_week)

    return compare_hotels_result(result)