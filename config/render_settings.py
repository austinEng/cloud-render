import bpy, os

try:
	bpy.context.user_preferences.system.compute_device_type = 'CUDA'
	bpy.context.user_preferences.system.compute_device = 'CUDA_0'
except: pass

filename = bpy.path.basename(bpy.context.blend_data.filepath)
filename = os.path.splitext(filename)[0]

scene = bpy.context.scene
render = scene.render
scene.frame_start = 1
scene.frame_end = 5
render.resolution_x = 1920
render.resolution_y = 1080;
render.resolution_percentage = 100
if filename:
	render.filepath = '//../' + filename + "_output/frame_####"
render.engine = 'CYCLES'
render.fps = 24
render.image_settings.color_mode = 'RGBA'
render.image_settings.file_format = 'PNG'
render.use_placeholder = True
render.use_overwrite = False

bpy.ops.render.render(animation=True)