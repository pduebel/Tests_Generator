def extract(db_file, test, proj):

    import pyodbc

    holes = []
    test_data = []

    odbc_conn_str = 'DRIVER={Microsoft Access Driver (*.mdb)};DBQ=%s;'%(db_file)
    conn = pyodbc.connect(odbc_conn_str)
    cursor = conn.cursor()

    hole_select = "select distinct HOLE_ID from %s where PROJ_ID='%s'"%(test, proj)
    cursor.execute(hole_select)

    holes = cursor.fetchall()

    cursor.commit()

    return holes

db = "GEODASY.mdb"
holes = extract(db, "SPT", "LS3093")
for hole in holes:
    print(hole)



