mon = 0
tue = 0
wed = 0
thu = 0
fri = 0
sat = 0
sun = 0

regular = 0
reward = 0

valor_reserva_lakewood = 0
valor_reserva_bridgewood = 0
valor_reserva_ridgewood = 0

def reset_valores ():
    global mon, tue, wed, thu, fri, sat, sun, regular, reward, valor_reserva_bridgewood, valor_reserva_lakewood, valor_reserva_ridgewood

    mon = 0
    tue = 0
    wed = 0
    thu = 0
    fri = 0
    sat = 0
    sun = 0

    regular = 0
    reward = 0

    valor_reserva_lakewood = 0
    valor_reserva_bridgewood = 0
    valor_reserva_ridgewood = 0

def conta_dias_da_semana (entrada_usuario):

    global mon, tue, wed, thu, fri, sat, sun, regular, reward

    entrada_usuario = list(entrada_usuario.split())

    for i in range(len(entrada_usuario)):
        if 'mon' in entrada_usuario[i]:
            mon = mon + 1
        
        if 'tue' in entrada_usuario[i]:
            tue = tue + 1

        if 'wed' in entrada_usuario[i]:
            wed = wed + 1

        if 'thu' in entrada_usuario[i]:
            thu = thu + 1

        if 'fri' in entrada_usuario[i]:
            fri = fri + 1

        if 'sat' in entrada_usuario[i]:
            sat = sat + 1

        if 'sun' in entrada_usuario[i]:
            sun = sun + 1

        if 'Regular' in entrada_usuario[i]:
            regular = regular + 1

        if 'Reward' in entrada_usuario[i]:
            reward = reward + 1



def hotel_lakewood ():
    global valor_reserva_lakewood
    taxa_dias_semana_cliente_regular = 110
    taxa_dias_semana_cliente_reward = 80
    taxa_final_semana_cliente_regular = 90
    taxa_final_semana_cliente_reward = 80

    valor_reserva_regular = regular*((mon + tue + wed + thu + fri)*taxa_dias_semana_cliente_regular + (sat + sun)*taxa_final_semana_cliente_regular)
    valor_reserva_reward = reward*((mon + tue + wed + thu + fri)*taxa_dias_semana_cliente_reward + (sat + sun)*taxa_final_semana_cliente_reward)
    valor_reserva_lakewood = valor_reserva_regular + valor_reserva_reward

    #print('valor reserva lakewood', valor_reserva_lakewood)

def hotel_bridgewood ():
    global valor_reserva_bridgewood
    taxa_dias_semana_cliente_regular = 160
    taxa_dias_semana_cliente_reward = 110
    taxa_final_semana_cliente_regular = 60
    taxa_final_semana_cliente_reward = 50

    valor_reserva_regular = regular*((mon + tue + wed + thu + fri)*taxa_dias_semana_cliente_regular + (sat + sun)*taxa_final_semana_cliente_regular)
    valor_reserva_reward = reward*((mon + tue + wed + thu + fri)*taxa_dias_semana_cliente_reward + (sat + sun)*taxa_final_semana_cliente_reward)
    valor_reserva_bridgewood = valor_reserva_regular + valor_reserva_reward

    #print('valor reserva bridgewoodd', valor_reserva_bridgewood)

def hotel_ridgewood ():
    global valor_reserva_ridgewood
    taxa_dias_semana_cliente_regular = 220
    taxa_dias_semana_cliente_reward = 100
    taxa_final_semana_cliente_regular = 150
    taxa_final_semana_cliente_reward = 40

    valor_reserva_regular = regular*((mon + tue + wed + thu + fri)*taxa_dias_semana_cliente_regular + (sat + sun)*taxa_final_semana_cliente_regular)
    valor_reserva_reward = reward*((mon + tue + wed + thu + fri)*taxa_dias_semana_cliente_reward + (sat + sun)*taxa_final_semana_cliente_reward)
    valor_reserva_ridgewood = valor_reserva_regular + valor_reserva_reward

    #print('valor reserva ridgewood', valor_reserva_ridgewood)


def escolhe_hotel (valor_reserva_ridgewood, valor_reserva_bridgewood, valor_reserva_lakewood):
    classificacao_lakewood = 3
    classificacao_bridgewood = 4
    classificacao_ridgeeood = 5

    numeros = [valor_reserva_ridgewood, valor_reserva_bridgewood, valor_reserva_lakewood]
    numeros.sort()
    #print(numeros)

    if valor_reserva_ridgewood < valor_reserva_bridgewood and valor_reserva_ridgewood < valor_reserva_lakewood and numeros[0] != numeros[1]:
        return 'Ridgewood'

    if valor_reserva_bridgewood < valor_reserva_lakewood and valor_reserva_bridgewood < valor_reserva_ridgewood and numeros[0] != numeros[1]:
        return 'Bridgewood'

    if valor_reserva_lakewood < valor_reserva_bridgewood and valor_reserva_lakewood < valor_reserva_ridgewood and numeros[0] != numeros[1]:
        return 'Lakewood'
        

    if numeros[0] == numeros[1] and numeros[2] == valor_reserva_lakewood:
        if valor_reserva_bridgewood*classificacao_bridgewood > valor_reserva_ridgewood*classificacao_ridgeeood:
            return 'Bridgewood'
        else:
            return 'Ridgewood'

    if numeros[0] == numeros[1] and numeros[2] == valor_reserva_bridgewood:
        if valor_reserva_lakewood*classificacao_lakewood > valor_reserva_ridgewood*classificacao_ridgeeood:
            return 'Lakewood'
        else:
            return 'Ridgewood'

    if numeros[0] == numeros[1] and numeros[2] == valor_reserva_ridgewood:
        if valor_reserva_bridgewood*classificacao_bridgewood > valor_reserva_lakewood*classificacao_lakewood:
            return 'Bridgewood'
        else:
            return 'Lakewood'


def get_cheapest_hotel(number):   #DO NOT change the function's name
    
    conta_dias_da_semana (number)
    hotel_lakewood ()
    hotel_bridgewood ()
    hotel_ridgewood ()    
    cheapest_hotel = escolhe_hotel (valor_reserva_ridgewood, valor_reserva_bridgewood, valor_reserva_lakewood)
    reset_valores()

    return cheapest_hotel