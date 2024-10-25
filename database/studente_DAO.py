from database.DB_connect import get_connection
from model.studente import  Studente

# Add whatever it is needed to interface with the DB Table studente
def get_studenteDAO(matr):
    cnx = get_connection()
    cursor = cnx.cursor()
    query = """SELECT nome, cognome FROM studente WHERE studente.matricola = %s"""
    cursor.execute(query, (matr,))
    row = cursor.fetchone()
    cursor.close()
    cnx.close()
    if row is not None:
        return row[0], row[1]
    else:
        return None, None
