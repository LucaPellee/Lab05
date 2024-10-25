import flet as ft
from model.model import Model
from UI.view import View


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._id_map_corsi = {}
        self._corso = None
        self._matrStudente = None

    def _leggiDdCorso(self, e):
        self._corso = self._view._ddCorso.value

    def _leggiTfMatr(self, e):
        self._matrStudente = self._view._tfMatr.value

    def _cercaIscritti(self, e):
        if self._corso is None:
            self._view.create_alert("Inserire il corso")
            return
        else:
            iscritti = self._model.get_iscritti(self._corso)
            self._view._lwResult.controls.clear()
            if len(iscritti) == 0:
                self._view._lwResult.controls.append(ft.Text("Non ci sono iscritti"))
            else:
                for studente in iscritti:
                    self._view._lwResult.controls.append(ft.Text(f"{studente}"))
                self._view.update()

    def _cercaStudente(self, e):
        if self._matrStudente is None:
            self._view.create_alert("Inserire la matricola")
            return
        else:
            nome, cognome = self._model.get_studente(self._matrStudente)
            self._view._tfNome.value = ""
            self._view._tfCognome.value = ""
            self._view._lwResult.controls.clear()
            if nome is None or cognome is None:
                self._view._lwResult.controls.append(ft.Text("matricola non corrispondente", color = "red"))
            else:
                self._view._tfNome.value = f"{nome}"
                self._view._tfCognome.value = f"{cognome}"
            self._view.update()


    def _cercaCorsi(self, e):
        pass

    def _riempiDdCorsi(self):
        dictCorsi = self._model._getCorsi()
        for corso in dictCorsi:
            self._id_map_corsi[corso.codins] = corso
            self._view._ddCorso.options.append(ft.dropdown.Option(key = corso.codins, text = corso.__str__()))
        self._view.update()

