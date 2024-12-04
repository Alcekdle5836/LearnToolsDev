import bpy

class MY_COLLECTION_PT_Panel(bpy.types.Panel):
    bl_label = "My Collection Panel"
    bl_idname = "MY_COLLECTION_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'My Collection'

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        my_collection = scene.my_custom_collection
        layout.operator("my_collection.add_item", text="Add Item", icon='ADD')

        for i, item in enumerate(my_collection):
            box = layout.box()
            box.prop(item, "prop1", text="Property 1")
            box.prop(item, "prop2", text="Property 2")
            remove_op = box.operator("my_collection.remove_item", text="Remove Item", icon='REMOVE')
            remove_op.index = i

blender_classes = [
    MY_COLLECTION_PT_Panel,
]

def register():
    for bclass in blender_classes:
        bpy.utils.register_class(bclass)
    
def unregister():
    for bclass in blender_classes:
        bpy.utils.unregister_class(bclass)