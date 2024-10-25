import database
from database import corso_DAO
from database import studente_DAO
class Model:
    def __init__(self):
        pass

    def _getCorsi(self):
        return corso_DAO._getCorsiDAO()

    def get_iscritti(self, corso):
        return corso_DAO.get_iscrittiDAO(corso)

    def get_studente(self, matr):
        return studente_DAO.get_studenteDAO(matr)