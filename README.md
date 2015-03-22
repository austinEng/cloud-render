# Cloud Render
A Blender render manager that is designed to work over shared or networked folders. It allows a collection of machines to collaboratively render a project by setting up a pseudo render farm.

To get started, create a project in the project directory, for example: projects/test/test.blend

Set the proper settings for your project in render_settings.py. Any settings which are not set will be taken from whatever is set in your Blender project file. It is recommended that you use placeholders and do not overwrite as this will allow multiple machines to work on a single project.

Then, start the render manager in config/manager.py. Enter "projects" to see all your current projects. This will list any valid .blend file in your projects directory.

"render project-name" will flag that project for rendering. The script will prompt you for an output directory. This will start a process in the background which will move images from the output directory "projects/project-name_output" to another directory of your choice. This is useful when rendering into a folder in the cloud, such as Dropbox in order to save space.

Then, on any other machine with access to the root directory, run the render.py script

When the render is finished, "stopcopy" will kill the background process

# Additional Notes
Currently the scripts use a portable Python and Blender installation which should be placed in the programs/ folder. This is useful when rendering on machines which do not have these installed. The folder can shared over Dropbox and rendered on client machines without additional setup. If you do not wish to do this, you will need to manually change the path to Blender in render.py
