import bpy

class RenameObject(bpy.types.Panel):
    bl_idname = "RenameObject"
    bl_space_type = "VIEW_3D"           # 文档，搜一下
    bl_region_type = "UI"
    bl_label = "物体命名"
    bl_category = "BaseAddons"

    def draw(self,context):   
        props = context.scene.second_props
        layout = self.layout
        layout.prop(props,"new_name",text = "NewName11111")
        layout.operator("object.rename",text="555555555")

blender_classes = [
    RenameObject,
]

def register():
    for b_class in blender_classes:
        bpy.utils.register_class(b_class)

def unregister():
    for b_class in blender_classes:
        bpy.utils.unregister_class(b_class)