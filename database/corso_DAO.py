# Add whatever it is needed to interface with the DB Table corso
from model.corso import Corso
from database.DB_connect import get_connection
from model.studente import Studente


def _getCorsiDAO():
    cnx = get_connection()
    result = []
    cursor = cnx.cursor(dictionary = True)
    query = "SELECT * FROM corso"
    cursor.execute(query)
    for row in cursor:
        result.append(Corso(row["codins"],row["crediti"], row["nome"], row["pd"]))
    cursor.close()
    cnx.close()
    return result

def get_iscrittiDAO(codins):
    cnx = get_connection()
    result = []
    cursor  = cnx.cursor(dictionary = True)
    query = ("""SELECT studente.* FROM iscrizione, studente
             WHERE iscrizione.matricola = studente.matricola and iscrizione.codins = %s""")
    cursor.execute(query, (codins,))
    for row in cursor:
        result.append(Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"]))
    cursor.close()
    cnx.close()
    return result
