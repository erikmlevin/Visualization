eximport bge
import math
class Buttons():
	"""docstring for Buttons"""
	def __init__(self):
		self.cont = bge.logic.getCurrentController()
		self.scene = bge.logic.getCurrentScene()
		self.camera = self.scene.objects['Camera']
		
	def buttonHover(self):
		button = self.cont.owner
		absolute = math.fabs(self.camera.position[0] - button.position[0])
		if absolute <= 1:
			button.position[2] = .3 -(absolute*0.3)
		else:
			button.position[2] = .06 

	def button01(self):
		button = self.cont.owner
		mouse = self.cont.sensors['mouseClick']
		scenePointer = button['scenePointer']
		if mouse.positive and math.fabs(self.camera.position[0] - button.position[0]) <= .8:
			self.scene.replace(scenePointer)


def hover():
	hov = Buttons()
	hov.buttonHover()
hover()

def butt():
	but = Buttons()
	but.button01()
butt()