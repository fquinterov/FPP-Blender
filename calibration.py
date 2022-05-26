import os
import bpy
import cv2

# 01. remove SVG collection
collection = bpy.data.collections.get('acircleboard.svg')
if collection:
    print('the calibration patters is already loaded')
else:
    bpy.ops.import_curve.svg(filepath = 'acircleboard.svg')
    collection = bpy.data.collections.get('acircleboard.svg')

for obj in collection.objects:
    bpy.data.objects.remove(obj, do_unlink=True)
    
bpy.data.collections.remove(collection)

# 02. import calibration pattern
bpy.ops.import_curve.svg(filepath = "acircleboard.svg")

# 03. deselect nothing, select all curves, join
bpy.ops.object.select_all(action='DESELECT')
#bpy.ops.object.select_by_type(type='CURVE')

curves = bpy.data.collections["acircleboard.svg"].all_objects
for obj in curves:
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.convert(target='MESH')

bpy.ops.object.join()
bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
calibr_pattern = bpy.data.collections["acircleboard.svg"].all_objects[0]

# 04. read XML file.
poses_xml = cv2.FileStorage("calibr_poses.xml", cv2.FILE_STORAGE_READ)
poses = poses_xml.getNode("calibr_poses").mat() 
nposes = np.shape(poses)[0]

# 05. we prepare the scene to capture the poses images
camera = bpy.data.objects['Camera']
scene = bpy.context.scene
scene.camera = camera
scene.use_nodes = True
scnodes = scene.node_tree

# fringe images path.
imgpath = "C:/Users/USUARIO/OneDrive - Universidad Tecnológica de Bolívar/00. Trabajo de Grado FPP aided by DL/03. FPP Blender Calibration/05. FringePatternImages/fpp_images"
fringe_imgs = os.listdir(imgpath)

# projector calibration captured images path
cimg_path = "C:/Users/USUARIO/OneDrive - Universidad Tecnológica de Bolívar/00. Trabajo de Grado FPP aided by DL/03. FPP Blender Calibration/06. Results"
calibr_folders = os.listdir(cimg_path)
nfolders = len(calibr_folders)
cimg_path = cimg_path + "/calibration_" + str(nfolders)

flag_clbr_cam = 1
flag_clbr_proj = 0

for pos in range(nposes):
    for fimg in fringe_imgs:
        calibr_pattern.location =  poses[pos,0:3]
        calibr_pattern.rotation_euler = poses[pos,3:6]
    
        img = bpy.data.images.load(os.path.join(imgpath, fimg))
        img.alpha_mode = 'NONE'
        bpy.data.lights["Spot"].node_tree.nodes["Image Texture"].image = img
        scene.render.image_settings.file_format = 'PNG'
        
        if fimg == 'white.png' and flag_clbr_cam == True:
            cimg_camera_path = cimg_path + "/cam_calibration/" + str(pos)
            #bpy.context.scene.render.filepath = os.path.join(cimg_camera_path, fimg)
            bpy.context.scene.render.filepath = cimg_camera_path
            bpy.ops.render.render(use_viewport = True, write_still=True)
                
        if flag_clbr_proj == True:
            cimg_projector_path = cimg_path + "/pose_" + str(pos)
            bpy.context.scene.render.filepath = os.path.join(cimg_projector_path, fimg)
            bpy.ops.render.render(use_viewport = True, write_still=True)
