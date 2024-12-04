import bpy

class MY_COLLECTION_OT_AddItem(bpy.types.Operator):
    bl_idname = "my_collection.add_item"
    bl_label = "Add Collection Item"

    def execute(self, context):
        item = context.scene.my_custom_collection.add()
        item.prop1 = "New Item"
        item.prop2 = 5
        return {'FINISHED'}

class MY_COLLECTION_OT_RemoveItem(bpy.types.Operator):
    bl_idname = "my_collection.remove_item"
    bl_label = "Remove Collection Item"
    index: bpy.props.IntProperty()

    def execute(self, context):
        context.scene.my_custom_collection.remove(self.index)
        print('Remove:' + str(self.index))
        return {'FINISHED'}

blender_classes = [
    MY_COLLECTION_OT_AddItem,
    MY_COLLECTION_OT_RemoveItem,
]

def register():
    for bclass in blender_classes:
        bpy.utils.register_class(bclass)

def unregister():
    for bclass in blender_classes:
        bpy.utils.unregister_class(bclass)