import bge
import math

class AnimationController(object):
	"""docstring for AnimationController"""
	def __init__(self):
		self.cont = bge.logic.getCurrentController()
		self.scene = bge.logic.getCurrentScene()
		self.camera = self.scene.objects['camera']
		self.play = self.scene.objects['playButton']
		self.stop = self.scene.objects['stopButton']

	def playButton(self):
		mouseClick = self.cont.sensors['mouseClick']
		mouseOver = self.cont.sensors['mouseOver']
		if self.play['isActive']: 
			if mouseOver.positive:
				if mouseClick.positive:
					self.camera['isRuning'] = True
					self.play['isActive'] = False
					self.stop['isActive'] = True

	def stopButton(self):
		mouseClick = self.cont.sensors['mouseClick']
		mouseOver = self.cont.sensors['mouseOver']
		if self.stop['isActive']: 
			if mouseOver.positive:
				if mouseClick.positive:
					self.camera['isRuning'] = True
					self.stop['isActive'] = False
					self.play['isActive'] = True

	def line(self):
		shifter = self.scene.objects['shifter']
		progress = self.scene.objects['camera']
		if 'x' not in shifter:
			shifter['x'] = 0.0
		shifter['x'] = (progress['x']/100)*.02
		shifter.position[0] = (self.camera.position[0]-2.3)+shifter['x']

def play():
	pButton = AnimationController()
	pButton.playButton()

def stop():
	sButton = AnimationController()
	sButton.stopButton()

def line():
	lineShifter = AnimationController()
	lineShifter.line()