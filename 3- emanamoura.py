def get_cheapest_hotel(data):   #DO NOT change the function's name
    
    client_type = get_client_type(data)
    client_dates = get_client_dates(data)

    if client_type == "Regular":
        return get_best_hotel_based_in_type(client_type, client_dates)
    elif client_type == "Rewards":
        return get_best_hotel_based_in_type(client_type, client_dates)
    else:
        return "You must enter a valid client type, such as 'Regular' or 'Rewards'"

def get_best_hotel_based_in_type(client_type, client_dates):
    result_lakewood = 0;
    result_bridgewood = 0;
    result_ridgewood = 0;
    for i in range(len(client_dates)):
        day = get_week_day(client_dates[i])
        result_lakewood += value_day_lakewood(day, client_type)
        result_bridgewood += value_day_bridgewood(day, client_type)
        result_ridgewood += value_day_ridgewood(day, client_type)
        
    if result_lakewood < result_bridgewood and result_lakewood < result_ridgewood:
        return "Lakewood"
    elif result_bridgewood < result_lakewood and result_bridgewood < result_ridgewood:
        return "Bridgewood"
    elif result_ridgewood < result_lakewood and result_ridgewood < result_bridgewood:
        return "Ridgewood"
    elif result_lakewood == result_bridgewood and result_bridgewood == result_ridgewood:
        return "Ridgewood"
    elif result_ridgewood == result_lakewood or result_ridgewood == result_bridgewood:
        return "Ridgewood"
    elif result_lakewood == result_bridgewood:
        return "Bridgewood"
    else:
        return "Lakewood"


def value_day_lakewood(day, client_type):
    if day == "sat" or day == "sun":
            if client_type == "Regular":
                return 90
            else:
                return 80
    else:
        if client_type == "Regular":
            return 110
        else:
            return 80

def value_day_bridgewood(day, client_type):
    if day == "sat" or day == "sun":
            if client_type == "Regular":
                return 60
            elif client_type == "Rewards":
                return 50
    else:
        if client_type == "Regular":
            return 160
        elif client_type == "Rewards":
            return 110

def value_day_ridgewood(day, client_type):
    if day == "sat" or day == "sun":
            if client_type == "Regular":
                return 150
            elif client_type == "Rewards":
                return 40
    else:
        if client_type == "Regular":
            return 220
        elif client_type == "Rewards":
            return 100
    
def get_week_day(unic_date):
    index_inital_letter_day = unic_date.find("(") + 1
    index_final_letter_day = unic_date.find(")")
    day = unic_date[index_inital_letter_day:index_final_letter_day]
    return day

def get_client_type(data):
    index_last_caracter_type = data.find(":")
    client_type = data[0:index_last_caracter_type]
    return client_type

def get_client_dates(data):
    initial_index_dates = data.find(":") + 2
    dates = data[initial_index_dates:]
    dates = dates.split(", ")
    return dates

# If you want to execute in your terminal, please, uncomment the two lines below
# data = input()
# print(get_cheapest_hotel(data))