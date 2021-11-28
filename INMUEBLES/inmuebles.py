from DB.db_conection import data_base_conection
from .querys import originalQuery, allData, filter_by_year, filter_year_city, filter_year_city_state


def consultar_inmuebles(year, city, state):
    results = []
    obj_data = {}
    query_structure = ''
    db = data_base_conection()
    cHandler = db.cursor()
    if year == '0' and city == '0' and state == '0':
        query_structure = originalQuery+allData
    if year != '0' and city == '0' and state == '0':
        query_structure = originalQuery+allData+filter_by_year.format(year)
    if year != '0' and city != '0' and state == '0':
        query_structure = originalQuery+allData + \
            filter_year_city.format(year, city)
    if year != '0' and city != '0' and state != '0':
        query_structure = originalQuery + \
            filter_year_city_state.format(year, city, state)
    cHandler.execute(query_structure)
    response = cHandler.fetchall()
    if response != ():
        print("response: ", response)
        for x in response:
            obj_structure = {"Direccion": x[0], "Ciudad": x[1], "Estado": x[2],
                             "Precio_de_venta": x[3], "Descripcion": x[4]}
            results.append(obj_structure)
            obj_data = {"error": False,
                        "message": "Se retorna la data con exito", "data": results}
    else:
        obj_data = {"error": False,
                    "message": "No se encuentra data que coincida con los filtros seleccionados"}
    return obj_data
