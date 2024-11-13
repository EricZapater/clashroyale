from repositories import historicaldata_repository

def get_all_historicaldata():
    return [historicaldata.to_dict() for historicaldata in historicaldata_repository.get_all_historicaldata()]