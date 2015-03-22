import subprocess
import time
import os
import sys
import pickle

path = os.path.dirname(sys.argv[0])
program_path = path + '\\..\\programs'

class Renderer:
	def __init__(self):
		self.renderprocess = None
		self.runfile = None

	def run(self):
		return os.path.isfile(self.runfile)	
		
	def render(self):
		blendfile = path + '\\..\\' + open(path+'\\.project', 'r').read()
		self.runfile = '\\'.join(blendfile.split('\\')[:-1])+'\\.run'
		while(True):
			try:
				enabled = self.run()
				if enabled and not self.renderprocess:
					blenderpath = 'C:\\Program Files\\Blender Foundation\\Blender\\blender.exe'
					blenderpath = program_path + '\\BlenderPortable\\BlenderPortable.exe'
					blendfile = path + '\\..\\' + open(path+'\\.project', 'r').read()
					self.runfile = '\\'.join(blendfile.split('\\')[:-1])+'\\.run'
					self.renderprocess = subprocess.Popen([blenderpath, '-b', blendfile, '-P', path + '\\render_settings.py'], shell=True, stdout=subprocess.PIPE)
				elif not enabled and self.renderprocess is not None:
					try:
						self.renderprocess.kill()
						self.renderprocess = None
					except: pass
				if self.renderprocess is not None:
					line = self.renderprocess.stdout.readline()
					if (line == b'' and self.renderprocess.poll() != None):
						print("Render job finished")
						self.renderprocess.kill()
						self.renderprocess = None
						if self.run():
							try:
								os.remove(self.runfile)
							except: pass

					sys.stdout.write(line.decode('utf-8'))
					sys.stdout.flush()
				else:
					time.sleep(2)
			except KeyboardInterrupt:
				if self.renderprocess is not None:
					self.renderprocess.kill()
					self.renderprocess = None
				break

r = Renderer()
r.render()