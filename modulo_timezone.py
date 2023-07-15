import pytz
from dateutil import parser

def converter_para_horario_brasilia(created_at):
    fuso_horario_utc = pytz.timezone('UTC')
    fuso_horario_brasilia = pytz.timezone('America/Sao_Paulo')
    horario_utc = parser.isoparse(created_at)
    horario_utc = horario_utc.replace(tzinfo=fuso_horario_utc)
    horario_brasilia = horario_utc.astimezone(fuso_horario_brasilia)
    return horario_brasilia.strftime("%Y-%m-%d %H:%M:%S")
