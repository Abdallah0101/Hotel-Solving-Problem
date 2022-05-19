import re

class Hotel:
    def __init__(self, nome, classificacao, tx_semana_normal, tx_semana_fidelidade, tx_final_normal, tx_final_fidelidade):
        self.nome = nome
        self.classificacao= classificacao
        self.tx_semana_normal = tx_semana_normal
        self.tx_semana_fidelidade = tx_semana_fidelidade
        self.tx_final_normal = tx_final_normal
        self.tx_final_fidelidade = tx_final_fidelidade

    @staticmethod
    def min_semana_normal(hoteis):
        '''
        Rebece uma lista de objetos do tipo hotel e retorna o menor valor de dia de semana para cliente tipo normal
        '''
        min_val = min(hoteis[0].tx_semana_normal, hoteis[1].tx_semana_normal, hoteis[2].tx_semana_normal)
        hotel_min = [hotel for hotel in hoteis if hotel.tx_semana_normal == min_val][0]
        return hotel_min

    @staticmethod
    def min_semana_fidelidade(hoteis):
        '''
        Recebee uma lista de objetos do tipo hotel  e retorna o menor valor de dia de semana para cliente tipo fidelidade
        '''
        min_val = min(hoteis[0].tx_semana_fidelidade, hoteis[1].tx_semana_fidelidade, hoteis[2].tx_semana_fidelidade)
        hotel_min = [hotel for hotel in hoteis if hotel.tx_semana_fidelidade == min_val][0]
        return hotel_min

    @staticmethod
    def min_final_normal(hoteis):
        '''
        Recebe uma lista de objetos do tipo hotel  e retorna o menor valor de final de semana para cliente tipo normal
        '''
        min_val = min(hoteis[0].tx_final_normal, hoteis[1].tx_final_normal, hoteis[2].tx_final_normal)
        hotel_min = [hotel for hotel in hoteis if hotel.tx_final_normal == min_val][0]
        return hotel_min

    @staticmethod
    def min_final_fidelidade(hoteis):
        '''
        Recebe uma lista de objetos do tipo hotel  e retorna o menor valor de final de semana para cliente tipo fidelidade
        '''
        min_val = min(hoteis[0].tx_final_fidelidade, hoteis[1].tx_final_fidelidade, hoteis[2].tx_final_fidelidade)
        hotel_min = [hotel for hotel in hoteis if hotel.tx_final_fidelidade == min_val][0]
        return hotel_min

    @staticmethod
    def maior_classificacao(hoteis):
        '''
        Recebe uma lista de objetos do tipo hotel e retorna a classificacao mais alta entre os hoteis
        '''
        max_classificacao = max(hotel.classificacao for hotel in hoteis)
        hotel_max = [hotel for hotel in hoteis if hotel.classificacao == max_classificacao][0]
        return hotel_max.nome

def entrada_analisa(entrada):
    '''
    Recebe uma string como entrada , separa e retorna o tipo de cliente e os dias
    '''
    tipo_cliente = re.search("\w+", entrada)
    dias = re.findall("\((\w+)\)", entrada)

    return (tipo_cliente.group(), dias)

def get_cheapest_hotel(number):   #DO NOT change the function's name
    '''
    Recebe uma string como entrada que contem o tipo do cliente e quais dias ira ficar, calcula os valores por dia
    inserido e retorna o minimo valor com a maior classificacao
    '''
    tipo_cliente, dias= entrada_analisa(number)

    if tipo_cliente != "Regular" and tipo_cliente!= "Rewards":
        return 'Tipo de cliente invalido, deve ser Regular ou Rewards'
    for dia in dias:
        if dia not in dias_semana and dia not in final_semana:
            return 'Dias invalido, deve ser mon, tues, wed, thur, fri, sat ou sun'

    lista_resultados = []

    if tipo_cliente == "Regular":
        for dia in dias:
            if dia in dias_semana:
                lista_resultados.append(Hotel.min_semana_normal(hoteis))
            else:
                lista_resultados.append(Hotel.min_final_normal(hoteis))
    else:
        for dia in dias:
            if dia in dias_semana:
                lista_resultados.append(Hotel.min_semana_fidelidade(hoteis))
            else:
                lista_resultados.append(Hotel.min_final_fidelidade(hoteis))

    cheapest_hotel = Hotel.maior_classificacao(lista_resultados)

    return cheapest_hotel

dias_semana = "montueswedthurfri"
final_semana = "satsun"

lakewood = Hotel("Lakewood", 3,110, 80, 90,80)
bridgewood = Hotel( "Bridgewood", 4, 160, 110, 60, 50)
ridgewood = Hotel( "Ridgewood", 5, 220, 100, 150, 40)

hoteis = []
hoteis.append(lakewood)
hoteis.append(bridgewood)
hoteis.append(ridgewood)