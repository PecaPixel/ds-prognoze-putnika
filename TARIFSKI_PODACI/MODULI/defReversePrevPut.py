import pyodbc

def reverse_and_join(s):
    records = s.split('*')  # Razdvaja string na delove po separatoru *
    reversed_records = []    # Lista za čuvanje obrnuti reči

    for record in records:
        if "(" in record and ")" in record:  # Proverava da li postoje zagrade u stringu
            inside_parentheses = record[record.find("(") + 1: record.find(")")]  # Izdvajanje teksta unutar zagrada
            reverse_inside_parentheses = "/".join(reversed(inside_parentheses.split("/")))  # Okretanje redosleda reči unutar zagrada
            
            # Zamenjuje deo unutar zagrada
            reversed_record = record.replace(inside_parentheses, reverse_inside_parentheses)  
            reversed_records.append(reversed_record)  # Dodaje celokupan obrnuti zapis u listu
        else:
            reversed_records.append(record)  # Dodavanje onoga što je izvan zagrada

    reversed_records.reverse()  # Obrtanje redosleda celokupnih zapisa
    return "*".join(reversed_records)  # Spajanje reči u string tako da čini prevozni put

# Konekcija sa bazom podataka
connection_string = r"DSN=MyAccessDSN;"
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

# Preuzimanje podataka iz tabele
select_query = "SELECT OPJZ FROM TabelaJZrelacija"
cursor.execute(select_query)
rows = cursor.fetchall()

# Iteriranje kroz redove i ažuriranje kolone
for row in rows:
    prevozni_put = row.OPJZ
    if prevozni_put is not None:
        reversePrevPut = reverse_and_join(prevozni_put)  # Pozivanje funkcije

        # Ažuriranje kolone u bazi podataka sa okrenutim vrednostima
        update_query = f"UPDATE TabelaJZrelacija SET OPJZ_rev = '{reversePrevPut}' WHERE OPJZ = '{prevozni_put}'"
        cursor.execute(update_query)

# Potvrđivanje promena
connection.commit()

# Zatvaranje konekcije
connection.close()

