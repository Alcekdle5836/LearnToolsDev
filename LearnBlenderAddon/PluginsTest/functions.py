import bpy

class RenameObjectOperator(bpy.types.Operator):
    bl_idname = "object.rename"
    bl_label = "rename objects"

    def execute(self,context):
        props = context.scene.second_props
        selected_object = context.selected_objects[0]
        selected_object.name = props.new_name
        print("Rename Success:" + selected_object.name)
        return {'FINISHED'}

class CreateNewCollection(bpy.types.Operator):
    bl_idname = "objects.new_collection"
    bl_label = "create new collection"

    def execute(self,context):
        props = context.scene.second_props
        target_collection_name = props.new_collection
        
        selected_objects = bpy.context.selected_objects
        # bpy.data.collections返回当前blender所有的collection名字的列表
        # 通过名字(target_collection_name)在列表中查找目标collection
        target_collection = bpy.data.collections.get(target_collection_name)

        # 如果没找到(target_collection变量就是None)，则新建collection
        if not target_collection:
            # 新建collection
            target_collection = bpy.data.collections.new(target_collection_name)
            # 将一个collection链接到当前场景的collection中，具体来说是将 target_collection 添加到当前场景的集合的子集合中
            bpy.context.scene.collection.children.link(target_collection)
        
        for obj in selected_objects:
            # 将当前对象链接到目标集合中
            target_collection.objects.link(obj)
            # 遍历当前对象所属的所有集合
            for group in obj.users_collection:        # obj.users_collection表示当前对象所属collection
                if(group != target_collection):       # 如果当前对象所属的collection不是目标collection，则将当前对象从当前collection中删除
                    group.objects.unlink(obj)
            self.report({'INFO'}, " Moved to " + target_collection.name + ":" + obj.name)
        return {'FINISHED'}

blender_classes = [
    RenameObjectOperator,
    CreateNewCollection,
]

def register():
    for b_class in blender_classes:
        bpy.utils.register_class(b_class)

def unregister():
    for b_class in blender_classes:
        bpy.utils.unregister_class(b_class)