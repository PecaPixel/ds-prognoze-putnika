import pyodbc

def reverse_and_join(s):
    try:
        records = s.split('*')
        reversed_records = []

        for record in records:
            if "(" in record and ")" in record:
                inside_parentheses = record[record.find("(") + 1: record.find(")")]
                reverse_inside_parentheses = "/".join(reversed(inside_parentheses.split("/")))
                reversed_record = record.replace(inside_parentheses, reverse_inside_parentheses)
                reversed_records.append(reversed_record)
            else:
                reversed_records.append(record)
        reversed_records.reverse()
        return "*".join(reversed_records)
    except Exception as e:
        print(f"Greška u funkciji reverse_and_join za unos: {s}. Detalji: {e}")
        return s