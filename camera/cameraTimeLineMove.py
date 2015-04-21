import bge 
import Rasterizer as R
import math 
import mathutils as mathu

class CameraTimeline():
	def __init__(self):
		self.SENSITIVITY = .005
		self.cont = bge.logic.getCurrentController()
		self.scene = bge.logic.getCurrentScene()
		self.camera = self.scene.objects['Camera']
		self.timelineWidth = self

	def shifter(self):
		mouse = self.cont.sensors['mouse']
		if 'x' not in self.camera:
			self.camera['x'] = 0.0
			x = R.getWindowWidth() // 2
			y = R.getWindowHeight() // 2
			self.camera['size'] = (x,y)

		xpos = self.camera['size'][0]
		ypos = self.camera['size'][1]

		R.setMousePosition(xpos,ypos)
		x = float(xpos - mouse.position[0])*self.SENSITIVITY
		
		self.camera['x'] += x
		if self.camera['x'] > 8.5:
			self.camera['x'] = 8.5
		if self.camera['x'] < -8.5:
			self.camera['x'] = -8.5

		
		z = self.camera.position[2]
		self.camera.position[0] = -self.camera['x']

def camera():
	move = CameraTimeline()
	move.shifter()
camera()