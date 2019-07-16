from geneticos import Geneticos
from Interfaz import *
# from Interfaz.window_ui import IForm

class Main(QtWidgets.QMainWindow,Interface):
    def __init__(self,*args,**kwargs):
        QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
        self.setupUi(self)
        self.buttonSelect.clicked.connect(self.initial)


    def initial(self):
        k = int(self.k.text())
        n_max = int(self.nMax.text())
        m = int(self.m.text())
        t_max = int(self.tMax.text())
        t_inicial = int(self.t0.text())
        porcentaje = int(self.codP.text())
        cruza = 1
        geneticos = Geneticos(k,n_max,m,t_max,t_inicial,porcentaje,cruza)
        geneticos.start()
        





# # k          = 15
# # n_max      = 5
# m          = 10
# t_max      = 20
# t_inicial  = 2
# porcentaje = 50
# cruza      = 1




















