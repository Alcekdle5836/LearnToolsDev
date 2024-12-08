# import mudules
import bpy
from bpy.types import PropertyGroup
from bpy.props import StringProperty, IntProperty, BoolProperty, EnumProperty, PointerProperty

# UI Class
class MyUIPanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_MY_PANEL"
    bl_label = "12090149"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "My Tool"

    def draw(self, context):
        layout = self.layout
        props = context.scene.simple_props
        layout.label(text="Helloworld")
        layout.prop(props,"folder_path")
        layout.operator("print.folderpath",text="ClickMe!!!!!!")
        layout.operator("print.1111",text="1111ClickMe!!!!!!")

# Properties
class MyProperties(PropertyGroup):
    folder_path : StringProperty(
        name = "FolderPath",
        default = "This is a defualt value",
        subtype = 'DIR_PATH'
    )

# function
class MyFunctions_1(bpy.types.Operator):
    bl_idname = "print.folderpath"
    bl_label = "Print File Paht"

    def execute(self,context):
        props = context.scene.simple_props
        print("%s" % props.folder_path)
        return {'FINISHED'}

class MyFunctions_2(bpy.types.Operator):
    bl_idname = "print.1111"
    bl_label = "Print File Paht"

    def execute(self,context):
        props = context.scene.simple_props
        print("111111")
        return {'FINISHED'}

blender_classes = [
    MyUIPanel,
    MyProperties,
    MyFunctions_1,
    MyFunctions_2,
]

# Register
def register():
    for b_class in blender_classes:
        bpy.utils.register_class(b_class)
    
    bpy.types.Scene.simple_props = PointerProperty(type=MyProperties)

def unregister():
    for b_class in blender_classes:
        bpy.utils.unregister_class(b_class)
    
    del bpy.types.Scene.simple_props

register()