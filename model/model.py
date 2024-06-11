import networkx as nx

from database.DAO import DAO
class Model:
    def __init__(self):
        self._grafo=nx.Graph()
        self._nodi={}
        self._archi={}
        self._listaDiListe=[]
        self._numarchi=0
        pass
    def get_color(self):
        return DAO.get_color()

    def crea_grafo(self,anno,colore):
        nodi=DAO.get_Nodi(colore)
        self._grafo.clear()
        self._nodi={}
        for element in nodi:
            self._nodi[element.Product_number]=element
            self._grafo.add_node(element)
        edge=DAO.get_edge(anno,colore)
        for element in edge:
            if (f"{element.p1}-{element.p2}-{element.data}") not in self._archi and (f"{element.p2}-{element.p1}-{element.data}") not in self._archi:
                self._archi[f"{element.p1}-{element.p2}-{element.data}"]=element
                if self._grafo.has_edge(self._nodi[element.p1],self._nodi[element.p2]):
                    self._grafo[self._nodi[element.p1]][self._nodi[element.p2]]['weight']+=1
                else:
                    self._grafo.add_edge(self._nodi[element.p1],self._nodi[element.p2],weight=1)

    def num_Nodi(self):
        return len(self._grafo.nodes())
    def num_Archi(self):
        return len(self._grafo.edges())
    def lista_archi(self):
        lista=[]
        for edge in self._grafo.edges(data=True):  # Itera sugli archi con attributi
            peso = edge[2]['weight']  # Ottieni il peso dell'arco
            lista.append((edge[0], edge[1], peso))
        lista=sorted(lista, key=lambda x:x[2], reverse=True)
        lista=lista[0:3]
        return lista
    def volte_in_piu(self):
        result=[]
        lista=self.lista_archi()
        nodi={}
        for element in lista:
            if element[0] in nodi:
                nodi[element[0]]+=1
            else:
                nodi[element[0]]=1
            if element[1] in nodi:
                nodi[element[1]]+=1
            else:
                nodi[element[1]]=1
        for key in nodi:
            if nodi[key]>1:
                result.append(key)
        return result

    def ricorsione(self,parziale, nodo,pesoIniziale):
        nodo=self._nodi[nodo]
        if pesoIniziale==0:
            parziale.append(nodo)
            self._numarchi=0
        successori=list(self._grafo.neighbors(nodo))
        for element in successori.copy():
            if element in parziale:
                successori.remove(element)
            elif self._grafo[nodo][element]['weight']<=pesoIniziale:
                successori.remove(element)
        if len(successori)==0:
            if len(parziale)>self._numarchi:
                self._listaDiListe=list(parziale)
                self._numarchi=len(parziale)
            return
        else:
            for item in successori:
                nuovo_nodo=item.Product_number
                parziale_nuovo=list(parziale)
                parziale_nuovo.append(nuovo_nodo)
                peso_nuovo=self._grafo[nodo][item]['weight']
                self.ricorsione(parziale_nuovo,nuovo_nodo,peso_nuovo)

    def fillDDProduct(self):
        lista_nodi=[]
        for node in self._grafo.nodes():
            lista_nodi.append(node)
        return lista_nodi
    def getPercorso(self):
        return self._numarchi








