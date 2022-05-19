def get_cheapest_hotel(number):   #DO NOT change the function's name
    cheapest_hotel = "cheapest_hotel_name"

    ## base de dados dos hoteis ##
    lakewood = ["Lakewood", 110.00, 90.00, 80.00, 80.00]
    bridgewood = ["Bridgewood", 160.00, 60.00, 110.00, 50.00]
    ridgewood = ["Ridgewood", 220.00, 150.00, 100.00, 40.00]

    data = number.split(":")
    client_type = data[0]
    dates = data[1]

    weekend = 0
    weekday = 0
    # pegando os tipos de dias da semana
    date = dates.split(",")
    for day in date:
        day_type = (day[day.find('(')+1:day.find(')')])
        sat_n_sun = ["sat", "sun"]
        if day_type not in sat_n_sun:
            weekday += 1
        else:
            weekend += 1

    # calculando o valor total das diarias de acordo com o tipo de cliente
    if("Regular" in client_type):
        lakewood.append((lakewood[1] * weekday) + (lakewood[2] * weekend))
        bridgewood.append((bridgewood[1] * weekday) + (bridgewood[2] * weekend))
        ridgewood.append((ridgewood[1] * weekday) + (ridgewood[2] * weekend)  )      
        
    elif("Rewards" in client_type):
        lakewood.append((lakewood[3] * weekday) + (lakewood[4] * weekend))
        bridgewood.append((bridgewood[3] * weekday) + (bridgewood[4] * weekend))
        ridgewood.append((ridgewood[3] * weekday) + (ridgewood[4] * weekend))
        
    else:
        print("tipo de cliente invalido!")

    # retornando o hotel mais barato
    if(lakewood[5] < bridgewood[5] and lakewood[5] < ridgewood[5]):
        cheapest_hotel = lakewood[0]
    elif(bridgewood[5] < lakewood[5] and bridgewood[5] < ridgewood[5]):
        cheapest_hotel = bridgewood[0]
    elif(ridgewood[5] < lakewood[5] and ridgewood[5] < bridgewood[5]):
        cheapest_hotel = ridgewood[0]
    elif(lakewood[5] == bridgewood[5] and bridgewood[5] == ridgewood[5]):
        cheapest_hotel = ridgewood[0]
    elif(ridgewood[5] == lakewood[5] or ridgewood[5] == bridgewood[5]):
        cheapest_hotel = ridgewood[0]
    elif(lakewood[5] == bridgewood[5]):
        cheapest_hotel = bridgewood[0]
    else:
        cheapest_hotel = lakewood[0]

    return cheapest_hotel
    
# descomente as proximas duas linhas para entrada via terminal
#i = input("")
#print(get_cheapest_hotel(i))