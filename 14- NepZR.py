HOTEL_TAXES = {
    'lakewood': {
        'Regular': {
            True: 110.0,
            False: 90.0
        },
        'Rewards': {
            True: 80.0,
            False: 80.0
        }
    },
    'bridgewood': {
        'Regular': {
            True: 160.0,
            False: 60.0
        },
        'Rewards': {
            True: 110.0,
            False: 50.0
        }
    },
    'ridgewood': {
        'Regular': {
            True: 220.0,
            False: 150.0
        },
        'Rewards': {
            True: 100.0,
            False: 40.0
        }
    }
}

def get_cheapest_hotel(clientData):             #DO NOT change the function's name
    formatedData = getFormatedData(clientData)
      
    pricing = {
        'lakewood': 0.0,
        'bridgewood': 0.0,
        'ridgewood': 0.0
    }

    for hotel in pricing:
        for workDay in formatedData['isWorkDay']:
            pricing[hotel] += HOTEL_TAXES[hotel][formatedData['clientType']][workDay]

    if (pricing['lakewood'] == pricing['bridgewood']):
        cheapest_hotel = 'Bridgewood'
    elif (pricing['lakewood'] == pricing['ridgewood']):
        cheapest_hotel = 'Ridgewood'
    elif (pricing['bridgewood'] == pricing['ridgewood']):
        cheapest_hotel = 'Ridgewood'

    if (pricing['lakewood'] < pricing['bridgewood'] and pricing['lakewood'] < pricing['ridgewood']):
        cheapest_hotel = 'Lakewood'
    elif (pricing['bridgewood'] < pricing['ridgewood']):
        cheapest_hotel = 'Bridgewood'
    else:
        cheapest_hotel = 'Ridgewood'

    return cheapest_hotel

def getFormatedData(clientData):
    workDays = {
        'mon': True,
        'tues': True,
        'wed': True,
        'thur': True,
        'fri': True,
        'sat': False,
        'sun': False 
    }

    datesGiven = clientData[clientData.index(' ')+1:].replace(' ', '').split(',')
    isWorkDay = []
    for date in datesGiven:
        weekDay = date[date.index('(')+1:date.index(')')]
        isWorkDay.append(workDays[weekDay])

    formatedData = {
        'clientType': clientData[:clientData.index(':')],
        'isWorkDay': isWorkDay
    }

    return formatedData