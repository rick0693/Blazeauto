import time
import pandas as pd
from modulo_api import make_request
from modulo_timezone import converter_para_horario_brasilia
from modulo_firestore import armazenar_dados_firestore
from modulo_util import verificar_numero
from modulo_dataframe import save_to_dataframe

import requests

valor_inicial = 0.10


def obter_novo_dado(dados_api, ultimo_server_seed, count_perdeu_consecutivas):
    novo_server_seed = dados_api[0]["server_seed"]

    if novo_server_seed != ultimo_server_seed:
        color4 = dados_api[3]["color"]
        color1 = dados_api[2]["color"]
        color2 = dados_api[1]["color"]
        color3 = dados_api[0]["color"]

        numero1 = dados_api[2]["roll"]
        numero2 = dados_api[1]["roll"]
        numero3 = dados_api[0]["roll"]

        created_at = dados_api[0]["created_at"]

        retorno = verificar_numero(color1, color2, color3, color4, count_perdeu_consecutivas)  # Obtém o valor de retorno

        return color1, color2, color3, color4, numero1, numero2, numero3, created_at, novo_server_seed, retorno

    return None

def check_server_seed(previous_server_seed):
    request_count = 0
    existing_dataframe = pd.DataFrame()
    count_perdeu_consecutivas = 0

    while True:
        request_count += 1
        try:
            data = make_request()
            new_data = obter_novo_dado(data, previous_server_seed, count_perdeu_consecutivas)
            if new_data:
                color1, color2, color3, color4, numero1, numero2, numero3, created_at, server_seed, retorno = new_data
                created_at_brasilia = converter_para_horario_brasilia(created_at)
                existing_dataframe = save_to_dataframe(data, retorno, existing_dataframe, valor_inicial)

                previous_server_seed = server_seed
            else:
                time.sleep(1)  # Espera 1 segundo antes de fazer uma nova requisição

        except requests.exceptions.RequestException as e:
            time.sleep(1)  # Espera 1 segundo antes de fazer uma nova requisição

if __name__ == '__main__':
    previous_server_seed = ''
    check_server_seed(previous_server_seed)
