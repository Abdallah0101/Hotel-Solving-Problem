def get_cheapest_hotel(number):                                                                 #function returns str with cheapest hotel
    cheapest_hotel = "cheapest_hotel_name"

    hotel_Lakewood = {'rating': 3,'weekdayValueRegular' : 110,'weekdayValueReward' : 80,        
                  'weekendValueRegular' : 90, 'weekendValueReward' : 80}            
    hotel_Bridgewood = {'rating': 4, 'weekdayValueRegular' : 160,'weekdayValueReward' : 110,    #hotel prices declaration
                    'weekendValueRegular' : 60, 'weekendValueReward' : 50}
    hotel_Ridgewood = {'rating': 5, 'weekdayValueRegular': 220,'weekdayValueReward' : 100,     
                   'weekendValueRegular' : 150, 'weekendValueReward' : 40}
    
    totalLake = int(0)                                                                          
    totalBridge = int(0)                                                                        #var with total price of hotel
    totalRidge = int(0)                                                                             
    auxiliar1 = number                                                                          #auxiliar var to receive str input
    auxiliar2 = []                                                                              #auxiliar var to convert str to list
    auxiliar2 = auxiliar1.split()
    if 'Regular:' == auxiliar2[0]  :                                                            #conditional to determine type of client
        for i in auxiliar2[1:] :                                                                #loop to increase value based on day of the week
            if (('mon' in i) or ('tues' in i) or ('wed' in i) or ('thur' in i) or ('fri' in i)):
                totalLake += hotel_Lakewood['weekdayValueRegular']
                totalBridge += hotel_Bridgewood['weekdayValueRegular']
                totalRidge += hotel_Ridgewood['weekdayValueRegular']
            else :
                totalLake += hotel_Lakewood['weekendValueRegular']
                totalBridge += hotel_Bridgewood['weekendValueRegular']
                totalRidge += hotel_Ridgewood['weekendValueRegular']

    elif 'Rewards:' == auxiliar2[0]   :                                                         #conditional to determine type of client
        for i in auxiliar2[1:] :                                                                #loop to increase value based on day of the week
            if (('mon' in i) or ('tues' in i) or ('wed' in i) or ('thur' in i) or ('fri' in i)):
                totalLake += hotel_Lakewood['weekdayValueReward']
                totalBridge += hotel_Bridgewood['weekdayValueReward']
                totalRidge += hotel_Ridgewood['weekdayValueReward']
            else :
                totalLake += hotel_Lakewood['weekendValueReward']
                totalBridge += hotel_Bridgewood['weekendValueReward']
                totalRidge += hotel_Ridgewood['weekendValueReward']
    else :
        cheapest_hotel = 'Wrong parameter input'                                                #wrong input error

    if (totalLake == totalBridge == totalRidge == 0) :                                          #wrong input error
        cheapest_hotel = 'Wrong parameter input'
    else :
        if ((totalLake < totalBridge) and (totalLake < totalRidge)):                          #conditional to determine which hotel is cheaper
            cheapest_hotel = 'Lakewood'

        elif ((totalBridge < totalLake) and (totalLake < totalRidge)):
            cheapest_hotel = 'Bridgewood'

        elif ((totalRidge < totalLake) and (totalRidge < totalBridge)):
            cheapest_hotel = 'Ridgewood'
        elif ((totalRidge == totalLake) and (totalRidge < totalBridge)):
            if ((hotel_Ridgewood['rating'] > hotel_Lakewood['rating'])) :
                cheapest_hotel = 'Ridgewood'
            else: cheapest_hotel = 'Lakewood'
        elif ((totalRidge == totalBridge) and (totalRidge < totalLake)):
            if ((hotel_Ridgewood['rating'] > hotel_Bridgewood['rating'])) :
                cheapest_hotel = 'Ridgewood'
            else: cheapest_hotel = 'Bridgewood'
        elif ((totalBridge == totalLake) and (totalBridge < totalRidge)):
            if ((hotel_Ridgewood['rating'] > hotel_Lakewood['rating'])) :
                cheapest_hotel = 'Ridgewood'
            else: cheapest_hotel = 'Lakewood'
        elif ((totalRidge == totalLake) and (totalRidge == totalBridge)):
            if ((hotel_Ridgewood['rating'] > hotel_Lakewood['rating']) and (hotel_Ridgewood['rating'] > hotel_Bridgewood['rating'])) :
                cheapest_hotel = 'Ridgewood'
            elif((hotel_Bridgewood['rating'] > hotel_Lakewood['rating']) and (hotel_Bridgewood['rating'] > hotel_Ridgewood['rating'])):
                 cheapest_hotel = 'Bridgewood'
            else:cheapest_hotel = 'Lakewood'
        else : cheapest_hotel = 'erro'                                                         #in case of unknown error
    return cheapest_hotel                                                                      #fucntion return