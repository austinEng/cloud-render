import cmd, os, sys, re, threading, time, shutil

path = os.path.dirname(sys.argv[0])
project_path = '\\'.join(path.split('\\')[:-1]) + '\\projects'

class Copier:

	def __init__(self):
		self.run = True

	def start(self, fromDir, toDir):
		self.run = True
		print("Starting copier...")
		try:
			os.makedirs(toDir)
		except: pass
		while self.run:
			try:
				for f in os.listdir(fromDir):
					path = fromDir + '\\' + f
					if os.path.isfile(path) and os.stat(path).st_size != 0:
						shutil.move(path, toDir  + '\\' + f)
						open(path, 'a').close()
						print("Saved " + f)
			except: pass
			time.sleep(1)

	def stop(self):
		self.run = False


class CommandProcessor(cmd.Cmd):

	prompt = '> '

	def do_projects(self, search):
		regex = re.compile(search)
		ending = re.compile('\.blend$')
		matches = []
		for root, dirs, files in os.walk(project_path):
			for name in files:
				if ending.search(name) and regex.search(name):
					matches.append(os.path.join(root, name))
		for match in matches:
			print(match + '\n')

	def help_projects(self):
		print('\n'.join(["Prints a list of the user's projects",
						'[search] optional regex search param']))


	def do_render(self, project):
		if not project:
			print("USAGE:\n")
			cmd.Cmd.onecmd(self, 'help render')
		else:
			regex = re.compile(project+'.blend$')
			matches = []
			for root, dirs, files in os.walk(project_path):
				for name in files:
					if regex.search(name):
						matches.append(os.path.join(root, name))
			if len(matches) is 0:
				print('No projects found with that name!')
			elif len(matches) > 1:
				print('Multiple files with that name!')
				for match in matches: print(match)
			else:
				matches = matches[0].split('\\')
				runfile = '\\'.join(matches[:-1])+'\\.run'
				f = open(runfile, 'a')
				f.close()
				print("Render flag created!")
				dirname = input("Output Directory: ")
				filename = matches[-1][:-6]
				outputdir = '\\'.join(matches[:-2]) + '\\' + filename + "_output"

				t = threading.Thread(target =copier.start, args = (outputdir, dirname))
				t.daemon = True
				t.start()

	def help_render(self):
		print('\n'.join(['Flags a project for rendering',
						'[project] name of the project to render\n']))

	def do_stopcopy(self, line):
		copier.stop()
		print("Stopped copier!")

	def help_stopcopy(self):
		print("Stops the automatic file copier")

copier = Copier()
CommandProcessor().cmdloop()