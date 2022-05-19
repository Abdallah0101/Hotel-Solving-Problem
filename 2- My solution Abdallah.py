import numpy as np

class Hotel:                      
    def __init__(self, price_weekday_regular, price_weekend_regular,
                price_weekday_reward, price_weekend_reward):

        self.weekday_regular = price_weekday_regular
        self.weekend_regular = price_weekend_regular
        self.weekday_reward = price_weekday_reward
        self.weekend_reward = price_weekend_reward

    def regular_weekday (self):
        return f"{self.weekday_regular}"
    def regular_weekend (self):
        return f"{self.weekend_regular}" 
    def reward_weekday (self):
        return f"{self.weekday_reward}"
    def reward_weekend (self):
        return f"{self.weekend_reward}"

Lakewood = Hotel(110, 90, 80, 80 )
Bridgewood = Hotel(160, 60, 110, 50 )
Ridegewood = Hotel(220, 150, 100, 40 )
                                  

def get_client_type(info):                                                  
    client_type = (info[:info.find(":")])
    return client_type


def get_day_type(info):                                                   
    values = info.split(",")
    day_type_list = []
    for value in values:
        day_type = (value[value.find("(")+1:value.find(")")])
    
        holiday = ["sun", "sat"]                 #add whatever you want of days names                       
        if day_type not in holiday:
            day_type = ("weekday")
            day_type_list.append(day_type)
            
        else:
            day_type = ("weekend")
            day_type_list.append(day_type)

    return day_type_list


def solving_the_problem (client_type, day_type_list):           
    list_of_lists = []

    for day in day_type_list:

        if day == "weekend" and client_type == "Regular":                         
            list1=[]
            list1.append(Hotel.regular_weekend(Lakewood))
            list1.append(Hotel.regular_weekend(Bridgewood))
            list1.append(Hotel.regular_weekend(Ridegewood))
            list1 = list(map(int, list1))
            list_of_lists.append(list1)           

        elif day == "weekday" and client_type == "Regular":                               
            list2=[]   
            list2.append(Hotel.regular_weekday(Lakewood))
            list2.append(Hotel.regular_weekday(Bridgewood))
            list2.append(Hotel.regular_weekday(Ridegewood))
            list2 = list(map(int, list2))
            list_of_lists.append(list2)       

        elif day == "weekend" and client_type == "Rewards":                            
            list3=[]      
            list3.append(Hotel.reward_weekend(Lakewood))
            list3.append(Hotel.reward_weekend(Bridgewood))
            list3.append(Hotel.reward_weekend(Ridegewood))
            list3 = list(map(int, list3))
            list_of_lists.append(list3)
            
        elif day == "weekday" and client_type == "Rewards":                            
            list4=[]      
            list4.append(Hotel.reward_weekday(Lakewood))
            list4.append(Hotel.reward_weekday(Bridgewood))
            list4.append(Hotel.reward_weekday(Ridegewood))
            list4 = list(map(int, list4))
            list_of_lists.append(list4)      

    column_sum = np.array(list_of_lists).sum(axis=0)        #Converting list_of_lists to array and calculating every colmun alone
    
    if column_sum[0] == column_sum[1]== column_sum[2]:
        result = ("Ridgewood")

    elif column_sum[0] == column_sum[1]:
        result = ("Bridgewood")

    elif column_sum[0] == column_sum[2]:
        result = ("Ridgewood")

    elif column_sum[1] == column_sum[2]:
        result = ("Ridgewood")

    elif column_sum[0] == min(column_sum):
        result = ("Lakewood")

    elif column_sum[1] == min(column_sum):
        result = ("Bridgewood")

    elif column_sum[2] == min(column_sum):
        result = ("Ridgewood")

    return result

def get_cheapest_hotel(info):   #DO NOT change the function's name
    
    client_type = get_client_type(info)
    day_type = get_day_type(info)
    cheapest_hotel = solving_the_problem(client_type, day_type)

    return cheapest_hotel


# for argument assignment in function      :======> Uncomment the line under

#print(get_cheapest_hotel(""))


# For assignment in Terminal               :======> Uncomment the line under

#info = input("")
#print(get_cheapest_hotel(info))
