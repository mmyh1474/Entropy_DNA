# importing libraries 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,  QAction
from PyQt5 import  QtGui
import sys
import Entropy
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as fig
import numpy as np
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from functools import partial


class Window(QWidget):

	def __init__(self):
		super().__init__()
		#self.setStyleSheet("background-color: black;")

		# setting title
		self.setWindowTitle("Entropy ")
		self.setWindowIcon(QIcon("DNA.png"))

	# setting geometry
		self.setGeometry(100, 100, 1400, 800)
		self.setFixedSize(1410, 800)

		self.formLayout = QFormLayout()
		groupbox = QGroupBox()
		self.buttonList = []
		plt.plot(1 + np.sin(2 * np.pi ))
		self.canvas = fig(plt.Figure(figsize=(15, 6)))

		self.toolbar = NavigationToolbar(self.canvas, self)
		self.ax = self.canvas.figure.subplots()

		#self.toolbars = self.addToolBar("Save")


		graph = QVBoxLayout()
		graph.addWidget(self.toolbar)
		graph.addWidget(self.canvas)



		groupbox.setLayout(self.formLayout)
		self.formLayout.setSpacing(10)
		groupbox.setGeometry(300,300,300,300)
		scroll = QScrollArea()
		scroll.setWidget(groupbox)
		scroll.setWidgetResizable(True)
		scroll.setFixedHeight(600)
		scroll.setFixedWidth(250)
		scroll.setStyleSheet("border-radius : 10px;  background: #E3E4E6 ; border: 1px solid #A29393;")



		groupBox = QGroupBox()
		groupBox.setStyleSheet("border-radius : 10px;  background: #E3E4E6 ; border: 1px solid #A29393; right: 5px ; top: 122px;")



		hbox = QVBoxLayout()
		hSimilarty = QVBoxLayout()

		self.shannon = QCheckBox("Shannon")
		self.renyi = QCheckBox("Renyi")
		self.tsallis = QCheckBox("Tsallis")

		WindowSizeText = QLabel("Window Size")
		WindowSizeText.setStyleSheet(" border: 0; font-size: 24px ; line-height: 28px;")
		WindowSizeText.setAlignment(Qt.AlignCenter)
		WindowSizeText.setFixedHeight(40)


		self.windowSize = QLineEdit()
		self.windowSize.setStyleSheet("border-radius : 0px;  background: white ;")

		RangeText = QLabel("Range Size")
		RangeText.setStyleSheet(" border: 0; font-size: 24px ; line-height: 28px;")
		RangeText.setAlignment(Qt.AlignCenter)
		RangeText.setFixedHeight(40)


		startPointText = QLabel("Start Point")
		startPointText.setStyleSheet(" border: 0; font-size: 24px ; line-height: 28px;")
		startPointText.setAlignment(Qt.AlignCenter)
		startPointText.setFixedHeight(40)


		#self.startPoint = QLineEdit()
		#self.startPoint.setStyleSheet("border-radius : 0px;  background: white ;")

		#self.Range = QLineEdit()
		#self.Range.setStyleSheet("border-radius : 0px;  background: white ;")

		#KemrsSizeText = QLabel("K-mers")
		#KemrsSizeText.setStyleSheet(" border: 0; font-size: 24px ; line-height: 28px;")
		#KemrsSizeText.setAlignment(Qt.AlignCenter)

		entropyText = QLabel("Entropy")
		entropyText.setStyleSheet(" border: 0; font-size: 24px ; line-height: 28px;")
		entropyText.setAlignment(Qt.AlignCenter)
		entropyText.setFixedHeight(40)

		applyBtn = QPushButton("Entropy", self);
		applyBtn.setIcon(QIcon("Play.png"))
		applyBtn.setIconSize(QSize(36, 36))
		applyBtn.setStyleSheet("QPushButton"
							   "{"
							   "background-color : #FFFFFF; border-radius: 4px; font-size: 24px; border: 1px solid #000000;"
							   "}"
							   "QPushButton::pressed"
							   "{"
							   "background-color : #ADA7A7;"
							   "}")
		# E3E4E6

		applyBtn2 = QPushButton("Similarity", self);
		applyBtn2.setIcon(QIcon("Play.png"))
		applyBtn2.setIconSize(QSize(36, 36))
		applyBtn2.setStyleSheet("QPushButton"
								"{"
								"background-color : #FFFFFF; border-radius: 4px; font-size: 24px; border: 1px solid #000000;"
								"}"
								"QPushButton::pressed"
								"{"
								"background-color : #ADA7A7;"
								"}")
		applyBtn2.setFixedHeight(40)
		applyBtn2.clicked.connect(self.apply2)

		applyBtn.setFixedHeight(40)
		applyBtn.clicked.connect(self.apply)

		simText = QLabel("Similarity")
		simText.setStyleSheet(" border: 0; font-size: 24px ; line-height: 28px;")
		simText.setAlignment(Qt.AlignCenter)
		simText.setFixedHeight(40)

		#KemrsSizeText.setFixedHeight(40)
		#KemrsSize = QLineEdit()

		#KemrsSize.setStyleSheet("border-radius : 0px;  background: white ;")
		hbox.addWidget(WindowSizeText)

		hbox.addWidget(self.windowSize);
		#hbox.addWidget(RangeText);
		#hbox.addWidget(self.Range);
		#hbox.addWidget(startPointText);
		#hbox.addWidget(self.startPoint);
		#hbox.addWidget(KemrsSizeText);
		#hbox.addWidget(KemrsSize);
		hbox.addWidget(entropyText);
		hbox.addWidget(self.shannon)
		hbox.addWidget(self.renyi)
		hbox.addWidget(self.tsallis)
		hbox.addWidget(applyBtn)
		hbox.setSpacing(1)

		hSimilarty.addWidget(simText)
		hSimilarty.addWidget(applyBtn2)
		groupBox.setLayout(hbox)
		vox = QVBoxLayout()
		groupBox.setFixedWidth(200)
		groupBox.setFixedHeight(600)
		vox.addWidget(groupBox)



		rightSideLayOut = QVBoxLayout()


		#Apply button



		#upload button
		open = QPushButton("open", self);
		open.setFixedHeight(40)
		open.setIcon(QIcon("Add.png"))
		open.setIconSize(QSize(36, 36))
		open.setStyleSheet("QPushButton"
                             "{"
                             "background-color : #E3E4E6; border-radius: 4px; font-size: 20px; border: 1px solid #000000;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : #ADA7A7;"
                             "}")
		open.clicked.connect(self.openFile)

		#Save button
		save = QPushButton("save", self);
		save.setFixedHeight(40)
		save.setIcon(QIcon("Save.png"))
		save.setIconSize(QSize(36, 36))
		save.setStyleSheet("QPushButton"
                             "{"
                             "background-color : #E3E4E6; border-radius: 4px; font-size: 20px; border: 1px solid #000000;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : #ADA7A7;"
                             "}")
		save.clicked.connect(self.saveFile)

		tabLayout = QHBoxLayout()
		tabLayout.addWidget(open)
		tabLayout.addWidget(save)

		tabFreme = QFrame()
		tabFreme.setLayout(tabLayout)
		tabFreme.setFixedHeight(52)

		leftSideLayout = QVBoxLayout()
		leftSideLayout.addWidget(tabFreme)
		leftSideLayout.addWidget(scroll)

		leftFrame = QFrame()
		leftFrame.setLayout(leftSideLayout)

		simFrame = QFrame()
		simFrame.setLayout(hSimilarty)
		simFrame.setStyleSheet("border-radius : 10px;  background: #E3E4E6 ; border: 1px solid #A29393; right: 5px ; top: 122px;")

		#applyBtn.setGeometry(1200, 720, 130, 50)

		rightSideLayOut.addWidget(groupBox)
		#rightSideLayOut.addWidget(applyBtn)
		rightSideLayOut.addWidget(simFrame)

		frame = QFrame()
		frame.setLayout(rightSideLayOut)

		medFrame = QFrame()
		medFrame.setLayout(graph)

		layout = QHBoxLayout()
		layout.addWidget(leftFrame)
		layout.addWidget(medFrame)
		layout.addWidget(frame)
		self.setLayout(layout)




		# showing all the widgets
		self.show()




	def graphUpdate(self):



		x = Entropy.getGraph()
		self.ax.cla()
		length = []


		self.ax.grid()
		for i in range(x[7], x[8]):
			length.append(i)


		for index in range(len(x[0])):
			print(self.buttonList[index].isChecked())
			if  self.buttonList[index].isChecked():

				if x[3]:
					self.ax.plot(np.array(x[0][index]), label=x[6][index] + ' shannon')
				if x[4]:
					self.ax.plot(np.array(x[1][index]), label=x[6][index] + ' renyi')
				if x[5]:
					self.ax.plot(np.array(x[2][index]), label=x[6][index] + ' tsallis')
		scrollLegend = QScrollArea()

		self.ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",mode="expand", borderaxespad=1, ncol=4)



		# plt.show()
		self.canvas.draw()

	# action method
	def apply(self):
		#check if the user enter the window size
		if self.windowSize.text() == "" or int(self.windowSize.text()) < 51:
			self.infoDialogue("You must fill the window size field with a number bigger than 50.")
			return

#		if self.Range.text() == "":
#			self.infoDialogue("You must fill the range size field with numbers.")
#			return

#		if self.startPoint.text() == "":
#			self.infoDialogue("You must fill the start point field with numbers.")
#			return

		if(self.shannon.isChecked() == True):
			e = "y"
		else:
			e = "n"
		if(self.renyi.isChecked() == True):
			r = "y"
		else:
			r = "n"
		if(self.tsallis.isChecked() == True):
			t = "y"
		else:
			t = "n"
  		# check if the user select at least one entropy
		if (e == "n" and r == "n" and t == "n"):
			self.infoDialogue("You must select at least one entropy..")
			return

		openFail = Entropy.main(int(self.windowSize.text()),  e, r, t )
		if openFail == False:
			self.infoDialogue("You must select at least one Genome.")
			return
		self.graphUpdate()

	def apply2(self):
		#Entropy.poreto(self.buttonList)

		if self.windowSize.text() == "":
			self.infoDialogue("You must fill the window size field with numbers.")
			return



		openFail = Entropy.applySimilarity(int(self.windowSize.text()),self.buttonList)
		if openFail == False:
			self.infoDialogue("You must select at least one Genome.")
			return
		else:
			self.infoDialogue2("The similarity saved in the list location successfully!")

	def btn(self, name):
		self.button = QPushButton(name, self)

		# setting geometry of button
		# button.setGeometry(50, 100, 240, 50)
		self.button.setFixedHeight(35)
		self.button.setFixedWidth(217)
		self.button.setDefault(False)
		self.button.setAutoDefault(False)
		# setting radius and border
		self.button.setStyleSheet("QPushButton"
							 "{"
							 "background-color : #FFFFFF;"
							 "}"
							 "QPushButton::pressed"
							 "{"
							 "background-color : grey;"
							 "}"
							  "QPushButton::Checked"
							 "{"
							 "background-color : grey;"
							 "}"
							 )

		#self.button.clicked.connect(partial(self.on_click, self.button))
		self.button.setCheckable(True)
		return self.button


	cle = False
	def openFile(self):

		if self.cle:
			for i in range(len(self.virList)):
				self.buttonList.append(self.btn(self.virList[i]))
				self.formLayout.removeRow(self.buttonList[i])

		self.cle = True

		self.virList = Entropy.openFiles()
		self.buttonList.clear()
		for i in range(len(self.virList)):
			self.buttonList.append(self.btn(self.virList[i]))
			self.formLayout.addRow(self.buttonList[i])


	def saveFile(self):
		checkSave =	Entropy.saveFile()
		if checkSave  == False:
			self.infoDialogue("there are no result")




	def infoDialogue2(self, errorMsg):  ## Method to open a message box
		infoBox = QMessageBox()

		infoBox.setText("Done")
		infoBox.setInformativeText(errorMsg)
		infoBox.setWindowTitle("Entropy")

		infoBox.setStandardButtons(QMessageBox.Ok)
		infoBox.setEscapeButton(QMessageBox.Close)
		infoBox.exec_()

	def infoDialogue(self, errorMsg):  ## Method to open a message box
		infoBox = QMessageBox()
		print("Im here")
		infoBox.setIconPixmap(QPixmap("ErrorIcon.png"))
		infoBox.setText("Invalid Input")
		infoBox.setInformativeText(errorMsg)
		infoBox.setWindowTitle("Entropy")

		infoBox.setStandardButtons(QMessageBox.Ok)
		infoBox.setEscapeButton(QMessageBox.Close)
		infoBox.exec_()





	# create pyqt5 app
App = QApplication(sys.argv) 

# create the instance of our Window 
window = Window() 

# start the app 
sys.exit(App.exec()) 
