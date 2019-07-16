from geneticos import Geneticos
from view.window_ui import *
from view.window_ui import IForm

class Main(QtWidgets.QMainWindow,IForm):

    def __init__(self,*args,**kwargs):
        QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
        self.setupUi(self)
        self.buttonSelect.clicked.connect(self.initial)


    def initial(self):
        k = int(self.textK.text())
        # print(self.textK.text(),"K")
        n_max = int(self.textNMax.text())
        # print(self.textNMax.text(),"nmax")
        m = int(self.textM.text())
        # print(self.textM.text(),"m")
        t_max = int(self.textTMax.text())
        # print(self.textTMax.text(),"tmax")
        t_inicial = int(self.text0.text())
        # print(self.text0.text(),"t0")
        porcentaje = int(self.textcodP.text())
        # print(self.textcodP.text(),"cond")
        cruza = 1
        geneticos = Geneticos(k,n_max,m,t_max,t_inicial,porcentaje,cruza)
        geneticos.start()
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    app.exec_() 



















