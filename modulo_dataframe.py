import pandas as pd
from modulo_timezone import converter_para_horario_brasilia
import modulo_timezone

def save_to_dataframe(data, retorno, existing_dataframe, valor_inicial):
    most_recent_entry = data[0]
    server_seed = most_recent_entry.get('server_seed', '')
    color = most_recent_entry.get('color', '')
    roll = most_recent_entry.get('roll', '')
    created_at = modulo_timezone.converter_para_horario_brasilia(most_recent_entry.get('created_at', ''))


    df = pd.DataFrame({
        'server_seed': [server_seed],
        'color': [color],
        'roll': [roll],
        'created_at_brasilia': [created_at],
        'retorno': [retorno],
        'resultado': ['']  # Nova coluna com valores em branco
    })

    df_concatenated = pd.concat([existing_dataframe, df], ignore_index=True)
    df_concatenated = df_concatenated.sort_values(by='created_at_brasilia', ascending=False)
    df_concatenated = df_concatenated.reset_index(drop=True)

    existing_dataframe = df_concatenated.copy()

    if len(existing_dataframe) > 1:
        color_last = existing_dataframe.loc[0, "color"]
        retorno_last = existing_dataframe.loc[1, "retorno"]

        if color_last == retorno_last:
            existing_dataframe.loc[0, "resultado"] = "Ganhou"
        else:
            existing_dataframe.loc[0, "resultado"] = "Perdeu"

    # Contagem de 'Perdeu' consecutivas
    consecutivo = 0
    maior_consecutivo = 0

    for i in range(len(existing_dataframe)):
        if existing_dataframe.loc[i, 'resultado'] == 'Perdeu':
            consecutivo += 1
            if consecutivo > maior_consecutivo:
                maior_consecutivo = consecutivo
        else:
            consecutivo = 0

    # Contagem de 'Perdeu' consecutivas
    count_perdeu_consecutivas = 0
    for i in range(len(existing_dataframe)):
        if existing_dataframe.loc[i, "resultado"] == "Perdeu":
            count_perdeu_consecutivas += 1
        else:
            break

    if count_perdeu_consecutivas > 5:
        retorno = 1 if retorno == 2 else 2

    if count_perdeu_consecutivas == 0:
        resultado_aposta = valor_inicial
        print('Valor da aposta:', resultado_aposta)
    else:
        valor_aposta = valor_inicial * (2 ** count_perdeu_consecutivas)
        resultado_aposta = valor_aposta
        print('Aposta na cor:', valor_aposta)

    existing_dataframe.loc[0, "aposta"] = resultado_aposta  # Adiciona o valor de resultado_aposta à coluna "aposta"

    print(existing_dataframe)
    print("Quantidade de 'Perdeu' consecutivas:", count_perdeu_consecutivas)
    print("Maior sequência consecutiva de 'Perdeu':", maior_consecutivo)

    return existing_dataframe
