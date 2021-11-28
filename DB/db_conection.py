import MySQLdb


def data_base_conection():
    try:
        myDB = MySQLdb.connect(host="3.130.126.210", port=3309,
                               user="pruebas", passwd="VGbt3Day5R", db="habi_db")
        return myDB
    except Error as err:
        return err
