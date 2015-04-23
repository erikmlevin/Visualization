import bge
import math 


class CameraLook():
	"""docstring for CameraLook"""
	def __init__(self):
		self.cont = bge.logic.getCurrentController()
		self.scene = bge.logic.getCurrentScene()
		bge.logic.mouse.visible = True

	def cameraLook(self):
		camera = self.cont.owner
		if 'max' not in camera:
			camera['max'] = self.scene.objects['Waveform']['lenght']

		if camera['isRuning']:
			camera['x'] += 0.4*0.1
		
		if camera['x'] > camera['max']:
			camera['x'] = camera['max']
		
		camera.position[0] = camera['x']


def camLook():

	cl = CameraLook()
	cl.cameraLook()
