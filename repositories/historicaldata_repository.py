from models.historicaldata import HistoricalData
from utils.db import get_db_connection

def get_all_historicaldata():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT year, week, day, player, battlesdone, comments FROM public.historicaldata')
    historicaldata_data = cursor.fetchall()
    cursor.close()
    conn.close()
    return[HistoricalData(*historicaldata) for historicaldata in historicaldata_data]