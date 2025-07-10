import pyodbc
from MODULI import defReversePrevPut
conection_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\predr\OneDrive\Documents\TARIFSKI_PODACI\data\imput\db_Data108_1_2024_25.accdb'
connection = pyodbc.connect(conection_string)
cursor = connection.cursor()

select_query = "SELECT OPJZ FROM TabelaJZrelacija"
cursor.execute(select_query)
rows = cursor.fetchall()

for row in rows:
    prevozni_put = row.OPJZ
    if prevozni_put is not None:
        reversePrevPut = defReversePrevPut.reverse_and_join(prevozni_put)
        print(reversePrevPut)

