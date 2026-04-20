import flet as ft

from model.model import Model


class Controller:
    def __init__(self, view):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = Model()
        self._ddCodinsValue = None

    def handlePrintCorsiPD(self, e):
        pd = self._view.ddPD.value

        if pd is None:
            self._view.create_alert("Attenzione, selezionare un periodo didattico.")
            self._view.update_page()
            return
        if pd == "I":
            pdInt = 1       #VERIFICA LA SELEZIONE DELL'UTENTE
        else:
            pdInt = 2

        corsiPd = self._model.getCorsiPd(pdInt)

        if not len(corsiPd):
            self._view.txt_result.controls.append(ft.Text(f"Nessun corso trovato per il {pd} periodo didattico."))
            self._view.update_page()        #VERIFICA LA CLASSE CORSO

        self._view.txt_result.controls.append(
            ft.Text(f"Di seguito i corsi del {pd} periodo didattico: ")       #STAMPA
        )
        for c in corsiPd:
            self._view.txt_result.controls.append(
                ft.Text(c))
        self._view.update_page()



    def handlePrintIscrittiCorsiPD(self, e):
        pd = self._view.ddPD.value

        if pd is None:
            self._view.create_alert("Attenzione, selezionare un periodo didattico.")
            self._view.update_page()
            return
        if pd == "I":
            pdInt = 1  # VERIFICA LA SELEZIONE DELL'UTENTE
        else:
            pdInt = 2

        corsi = self._model.getCorsiPDwIscritti(pdInt)
        if not len(corsi):
            self._view.txt_result.controls.append(ft.Text(f"Nessun corso trovato per il {pd} periodo didattico."))
            self._view.update_page()        #VERIFICA LA CLASSE CORSO

        self._view.txt_result.controls.append(
            ft.Text(f"Di seguito i corsi del {pd} periodo didattico con dettaglio iscritti: ")       #STAMPA
        )
        for c in corsi:
            self._view.txt_result.controls.append(
                ft.Text(f"{c[0]} -- N di iscritti {c[1]}"))
        self._view.update_page()

    def handlePrintIscrittiCodins(self, e):
        if self._ddCodinsValue is None:
            self._view.create_alert("Attenzione, selezionare un insegnamento.")
            self._view.update_page()
            return

        studenti = self._model.getStudentiCorso(self._ddCodinsValue.codins)
        if not len(studenti):
            self._view.txt_result.controls.append(ft.Text("Nessuno studente iscritto a questo corso"))
            self._view.update_page()
            return

        self._view.txt_result.controls.append(ft.Text(f"Di seguito gli studenti iscritti al corso {self._ddCodinsValue.codins}: "))
        for s in studenti:
            self._view.txt_result.controls.append(ft.Text(s))
        self._view.update_page()


    def handlePrintCDSCodins(self, e):
        if self._ddCodinsValue is None:
            self._view.create_alert("Attenzione, selezionare un insegnamento.")
            self._view.update_page()
            return
        cds = self._model.getCDSofCorso(self._ddCodinsValue.codins)

        if not len(cds):
            self._view.txt_result.controls.append(ft.Text(f"Nessun CDS afferente al corso {self._ddCodinsValue.codins}"))
            self._view.update_page()
            return

        self._view.txt_result.controls.append(ft.Text(f"Di seguito i CDS iscritti al corso {self._ddCodinsValue.codins}:"))
        for c in cds:
            self._view.txt_result.controls.append(ft.Text(f"{c[0]} -- N Iscritti {c[1]}"))
        self._view.update_page()

    def fillddCodins(self):
        for c in self._model.getAllCorsi():
            self._view.ddCodins.options.append(
                ft.dropdown.Option(key=c.codins,
                                   data=c,
                                   on_click=self._choiceDDCodins))
            pass

    def _choiceDDCodins(self, e):
        self._ddCodinsValue = e.control.data
        print(self._ddCodinsValue)
