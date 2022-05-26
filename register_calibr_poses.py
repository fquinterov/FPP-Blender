"""Register poses calibration
(Author: Fernando J. Quintero)

This script allows the user to load a calibration pattern in vector graphic format (.SVG) as a plane with which the position and orientation can be manipulated with Blender tools.

The script allows capturing the location and rotation values of the calibration plane and storing them in an XML file. The keyboard shortcuts are as follows:

    * press the "F" key to capture the pose.
    * press the "ESC" key to save the poses in an extensible file (.xml).
"""

import numpy as np
import bpy
import os
import cv2
from bpy.props import IntProperty, FloatProperty

def ShowMessageBox(message = "", title = "Calibration Pattern Poses Register", icon = 'INFO'):

        def draw(self, context):
            self.layout.label(text=message)

        bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)


camera = bpy.data.objects['Camera']
class ModalOperator(bpy.types.Operator):
    bl_idname = "object.modal_operator"
    bl_label = "Simple Modal Operator"
    
    def __init__ (self):
        self.count = -1
        self.pose = []

    def modal(self, context, event):
        if event.type == 'F' and event.value == 'PRESS':
            self.count += 1
            #print(self.count)
            
            pattern_loc = np.array(calibr_pattern.location)
            pattern_rot = np.array(calibr_pattern.rotation_euler)
            pattern_pose = np.append(pattern_loc,pattern_rot)
            
            #Shows a message box with a specific message 
            ShowMessageBox(f"Pose #{self.count} captured")
            self.pose.append(pattern_pose) 
            print(self.pose)

        elif event.type in {'ESC'}:
            fs = cv2.FileStorage("calibr_poses.xml", cv2.FILE_STORAGE_WRITE)
            fs.write('calibr_poses', np.array(self.pose))
            ShowMessageBox("Calibration poses were stored in the following XML file: 'calibr_poses.xml'", "Operation Completed", 'RENDER_RESULT')
            fs.release()
            return {'CANCELLED'}
        return {'PASS_THROUGH'}

    def invoke(self, context, event):
        if context.object:
            context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}
    
def menu_func(self, context):
    self.layout.operator(ModalOperator.bl_idname, text=ModalOperator.bl_label)
# Register and add to the "view" menu (required to also use F3 search "Simple Modal Operator" for quick access)
def register():
    bpy.utils.register_class(ModalOperator)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(ModalOperator)
    bpy.types.VIEW3D_MT_object.remove(menu_func)

if __name__ == "__main__":
    register()
    
    # we check if there is a calibration pattern loaded, if there is not then we load it.
    collection = bpy.data.collections.get('acircleboard.svg')
    if collection:
        print('the calibration patters is already loaded')
    else:
        bpy.ops.import_curve.svg(filepath = 'acircleboard.svg')
        collection = bpy.data.collections.get('acircleboard.svg')

    for obj in collection.objects:
        bpy.data.objects.remove(obj, do_unlink=True)
    
    bpy.data.collections.remove(collection)

    # import calibration pattern
    bpy.ops.import_curve.svg(filepath = "acircleboard.svg")

    # deselect nothing, select all curves, join
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
    
    print(os.path.abspath(os.curdir))
    bpy.ops.object.modal_operator('INVOKE_DEFAULT')
    
