import sys
from PySide2 import QtCore as qtc, QtGui as qtg, QtWidgets as qtw
from random import choice
def genpwd(taillemdp=8, min=True, maj=True, chif=True, sym=True):
	caracteres = ""
	#if x: sous entend que if x == True
	if min: 
		caracteres += "abcdefghijklmnopqrstuvwxyz"
	if maj:
		caracteres += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	if chif:
		caracteres += "0123456789"
	if sym:
		caracteres += "&~#{([-|_\^@)=+$]}*%!/:.;?,"
	pwd = ""
	for i in range(taillemdp):
		pwd += choice(caracteres)
	return(pwd)

class Window(qtw.QDialog):
	def __init__(self, parent=None):
		qtw.QDialog.__init__(self, parent)
		#Les cases
		self.caseMaj = qtw.QCheckBox("Majuscules")
		self.caseChif = qtw.QCheckBox("Chiffres")
		self.caseMin = qtw.QCheckBox("Minuscules")
		self.caseSym = qtw.QCheckBox("Symboles")
		#Les boutons
		self.boutonQuit = qtw.QPushButton("Quit")
		self.boutonCopy = qtw.QPushButton("Copy")
		self.boutonGen = qtw.QPushButton("Générer")
		#Champ de texte
		self.cdtMotdepasse = qtw.QLineEdit("")
		#Glissière
		self.glissiere = qtw.QSlider(qtc.Qt.Horizontal)
		#Label
		self.taille = qtw.QLabel("Taille du mot de passe + " + str(self.glissiere.value()))
		layout = qtw.QGridLayout()
		#Le layout est de type (élément, y, x)
		layout.addWidget(self.caseMaj, 0, 0) 
		layout.addWidget(self.caseChif, 1, 0)
		layout.addWidget(self.boutonQuit, 3, 0)
		layout.addWidget(self.taille, 0, 1)
		layout.addWidget(self.glissiere, 1, 1)
		layout.addWidget(self.cdtMotdepasse, 2, 1)
		layout.addWidget(self.boutonCopy, 3, 1)
		layout.addWidget(self.caseMin, 0, 2)
		layout.addWidget(self.caseSym, 1, 2)
		layout.addWidget(self.boutonGen, 3, 2)
		self.setLayout(layout)
		self.setWindowTitle("Générateur de mdp")
		self.caseMin.setChecked(True)
		self.caseChif.setChecked(True)
		self.glissiere.setMaximum(30)
		self.glissiere.setMinimum(1)
		icone = qtg.QIcon()
		icone.addPixmap(qtg.QPixmap("cadenas.svg"))
		self.setWindowIcon(icone)
		#élément.signal.connect(x) = lorsque l'élément émet le signal, exécuter la fonction x
		self.boutonQuit.clicked.connect(self.quit)
		self.boutonCopy.clicked.connect(self.copy)
		self.boutonGen.clicked.connect(self.generate)
		self.glissiere.valueChanged.connect(self.changetaillemdp)
	def quit(self):
		self.accept()
	def copy(self):
		pressePapier = qtw.QApplication.clipboard()
		pressePapier.setText(self.cdtMotdepasse.text())
	def generate(self):
		#x.value() = valeur de x
		#x.isChecked = l'état checked de x est-il true or false.
		taillemdp = self.glissiere.value() 
		maj = self.caseMaj.isChecked()
		chif = self.caseChif.isChecked()
		min = self.caseMin.isChecked()
		sym = self.caseSym.isChecked()
		self.cdtMotdepasse.setText(genpwd(taillemdp, min, maj, chif, sym)) #Ecrit la valeur de genpwd(*params) dans le champ de texte
	def changetaillemdp(self):
		self.taille.setText("Taille du mot de passe : " + str(self.glissiere.value()))
app = qtw.QApplication(sys.argv) #Fourni les arguments de la ligne de commande
dialog = Window() #instancie la fenêtre
dialog.exec_() #Affiche la fenêtre