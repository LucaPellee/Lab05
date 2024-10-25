import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._ddCorso = None
        self._btnIscritti = None
        self._tfMatr = None
        self._tfNome = None
        self._tfCognome = None
        self._btnStudente = None
        self._btnCorsi = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW 1
        self._ddCorso = ft.Dropdown(
            label="Corso",
            width = 500,
            hint_text="Selezionare il corso",
            on_change= self._controller._leggiDdCorso
        )
        self._controller._riempiDdCorsi()
        self._btnIscritti = ft.ElevatedButton(text = "Cerca iscritti", on_click= self._controller._cercaIscritti)

        row1 = ft.Row([self._ddCorso, self._btnIscritti], alignment= ft.MainAxisAlignment.CENTER)

        #ROW 2
        self._tfMatr = ft.TextField(label = "matricola", width=300, on_change= self._controller._leggiTfMatr)
        self._tfNome = ft.TextField(label = "Nome", width=200, read_only= True)
        self._tfCognome = ft.TextField(label = "Cognome", width = 200, read_only= True)

        row2 = ft.Row([self._tfMatr, self._tfNome, self._tfCognome], alignment= ft.MainAxisAlignment.CENTER)

        #ROW 3
        self._btnStudente = ft.ElevatedButton(text = "Cerca studente", on_click=self._controller._cercaStudente)
        self._btnCorsi = ft.ElevatedButton(text = "Cerca corsi", on_click=self._controller._cercaCorsi)

        row3 = ft.Row([self._btnStudente, self._btnCorsi], alignment= ft.MainAxisAlignment.CENTER)

        #RESULT
        self._lwResult = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

        self._page.add(row1, row2, row3, self._lwResult)


    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update(self):
        self._page.update()

