def extract(db_file, test, proj):

    import pyodbc

    test_data = []

    odbc_conn_str = 'DRIVER={Microsoft Access Driver (*.mdb)};DBQ=%s;'%(db_file)
    conn = pyodbc.connect(odbc_conn_str)
    cursor = conn.cursor()

    sql_select_statement = "select * from %s where PROJ_ID='%s'"%(test, proj)
    cursor.execute(sql_select_statement)

    test_data = cursor.fetchall()

    cursor.commit()

    return test_data
    




