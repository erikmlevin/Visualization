import bge
import math
import Rasterizer as R

class AnimationController(object):
	"""docstring for AnimationController"""
	def __init__(self):
		self.cont = bge.logic.getCurrentController()
		self.scene = bge.logic.getCurrentScene()
		self.camera = self.scene.objects['camera']
		self.play = self.scene.objects['playButton']
		self.stop = self.scene.objects['stopButton']

	def playButton(self):
		self.play.position[0] = self.camera.position[0] + 2
		mouseClick = self.cont.sensors['mouseClick']
		mouseOver = self.cont.sensors['mouseOver']
		if self.play['isActive']: 
			if mouseOver.positive:
				if mouseClick.positive:
					self.camera['isRuning'] = True
					self.play['isActive'] = False
					self.stop['isActive'] = True

	def stopButton(self):
		self.stop.position[0] = self.camera.position[0] + 2.3
		mouseClick = self.cont.sensors['mouseClick']
		mouseOver = self.cont.sensors['mouseOver']
		if self.stop['isActive']: 
			if mouseOver.positive:
				if mouseClick.positive:
					self.camera['isRuning'] = False
					self.stop['isActive'] = False
					self.play['isActive'] = True

	def line(self):
		self.scene.objects['timeLineForShifter'].position[0] = self.camera.position[0]
		shifter = self.scene.objects['shifter']
		progress = self.scene.objects['camera']
		if 'x' not in shifter:
			shifter['x'] = 0.0
		shifter['x'] = (progress['x']/100)*.02 #recreate constat .02 to 
		shifter.position[0] = (self.camera.position[0]-2.4)+shifter['x'] #recreate constat 2.4 to relative size of screen 
		#if self.play['isActive']:
			#code for timeLine interaction with shifter place here
			

def play():
	pButton = AnimationController()
	pButton.playButton()

def stop():
	sButton = AnimationController()
	sButton.stopButton()

def line():
	lineShifter = AnimationController()
	lineShifter.line()