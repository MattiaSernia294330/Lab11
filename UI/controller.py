import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []
        self._anno=None
        self._colore=None
        self._product=None

    def fillDD(self):
        for i in range(2015,2019):
            self._view._ddyear.options.append(ft.dropdown.Option(text=f"{i}", on_click=self.read_anno))
        listacolori=self._model.get_color()
        for element in listacolori:
            self._view._ddcolor.options.append(ft.dropdown.Option(text=f"{element}", on_click=self.read_colore))
        pass
    def read_anno(self,e):
        self._anno=int(e.control.text)
    def read_colore(self,e):
        self._colore=e.control.text
    def handle_graph(self, e):
        if not self._anno:
            self._view.create_alert("anno non inserito")
            return
        if not self._colore:
            self._view.create_alert("colore non inserito")
            return
        self._view.txtOut.clean()
        self._model.crea_grafo(self._anno,self._colore)
        self._view.txtOut.controls.append(ft.Text(f" il grafo creato ha {self._model.num_Nodi()} nodi"))
        self._view.txtOut.controls.append(ft.Text(f" il grafo creato ha {self._model.num_Archi()} archi"))
        lista=self._model.lista_archi()
        for element in lista:
            self._view.txtOut.controls.append(ft.Text(f"{element[0]} - {element[1]} - {element[2]}"))
        for element in self._model.volte_in_piu():
            self._view.txtOut.controls.append(ft.Text(f"{element.Product_number}"))
        self.fillDDProduct()
        self._view.update_page()



    def fillDDProduct(self):
        listaNodi=self._model.fillDDProduct()
        self._view._ddnode.options=[]
        for element in listaNodi:
            self._view._ddnode.options.append(ft.dropdown.Option(text=f"{element.Product_number}", on_click=self.readprodotto))


    def handle_search(self, e):
        if not self._product:
            self._view.create_alert("prodotto non inserito")
            return
        self._model.ricorsione([],self._product,0)
        numarchi=self._model.getPercorso()
        self._view.txtOut2.clean()
        self._view.txtOut2.controls.append(ft.Text(f"il percorso piu lungo ha {numarchi} archi"))
        self._view.update_page()
    def readprodotto(self,e):
        self._product=int(e.control.text)