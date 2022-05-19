def get_cheapest_hotel(request):
    hotel = ['Lakewood', 'Bridgewood', 'Ridgewood']
    classification = [3, 4, 5]
    daysOfTheWeek = {'sun': 1, 'mon': 0, 'tues': 0, 'wed': 0, 'thur': 0, 'fri': 0, 'sat': 1}

    weekdayRates = [110, 160, 220]
    weekendRates = [90, 60, 150]
    regularCostumer = [weekdayRates, weekendRates, classification]

    weekdayRates = [80, 110, 100]
    weekendRates = [80, 50, 40]
    rewardCostumer = [weekdayRates, weekendRates, classification]  

    information = request.replace(':',' ').replace(',',' ').split()
    costumerType = information[0]
    listOfDates = information[1:] 
    prices = [0, 0, 0]
    daysBooking = [0, 0]  
    # calculo da quantidade de dias da semana e do fim de semana sendo agendado
    for i in listOfDates:   
        _, day = i.replace('(',' ').split()
        day = day[:-1]
        daysBooking[daysOfTheWeek[day]] += 1

    if (costumerType == 'Regular'):
        prices[0] = (regularCostumer[0][0] * daysBooking[0]) + (regularCostumer[1][0] * daysBooking[1])
        prices[1] = (regularCostumer[0][1] * daysBooking[0]) + (regularCostumer[1][1] * daysBooking[1])
        prices[2] = (regularCostumer[0][2] * daysBooking[0]) + (regularCostumer[1][2] * daysBooking[1])
    elif (costumerType == 'Rewards'):
        prices[0] = (rewardCostumer[0][0] * daysBooking[0]) + (rewardCostumer[1][0] * daysBooking[1])
        prices[1] = (rewardCostumer[0][1] * daysBooking[0]) + (rewardCostumer[1][1] * daysBooking[1])
        prices[2] = (rewardCostumer[0][2] * daysBooking[0]) + (rewardCostumer[1][2] * daysBooking[1])
    else:
        print('Tipo de cliente desconhecido.')
        raise ValueError

    hotelsInfo = [0, 0, 0]
    for i in range(3):
        hotelsInfo[i] = [hotel[i], prices[i], -classification[i]]
    # ordenamento com preço como prioridade e classificação em segundo lugar 
    hotelsInfo.sort(key = lambda lis: (lis[1], lis[2])) 
    
    return hotelsInfo[0][0]  