from window_ui import *

class MainWindow(QtWidgets.QMainWindow, IForm):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        # self.buttonSelect.clicked.connect(self.selectImage)

    def selectImage(self):
        imageLabel = QtWidgets.QLabel()
        image , _ = QtWidgets.QFileIForm.getOpenFileName(None,
        'Select Image', '', "Image files (*.jpg *.png *.jpeg)")    
        if image:
            
            pixmap = QtGui.QPixmap(image)    
            imageLabel.setPixmap(pixmap)
            self.contenedorImagenPrincipal.setBackgroundRole(QtGui.QPalette.Dark)
            self.contenedorImagenPrincipal.setWidget(imageLabel)   
 
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
