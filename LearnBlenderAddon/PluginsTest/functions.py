import bpy
import json

json_data = []

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

class CreateCube(bpy.types.Operator):
    bl_idname = "cube.create"
    bl_label = "create cube"

    # 豆包 Marscode / codefuse
    def execute(self,context):
        props = context.scene.second_props
        bpy.ops.mesh.primitive_monkey_add(size = props.size_monkey ,enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        return {'FINISHED'}

# 导入json文件
class Import_Json(bpy.types.Operator):
    bl_idname = "file.json_import"
    bl_label = "Import_Json"

    def execute(self, context):
        props = context.scene.second_props
        filepath = props.path_json_string
        with open(filepath, 'r', encoding='utf-8') as JsonFile:
            json_read = JsonFile.read()
        global json_data
        json_data = json.loads(json_read)

        # bpy.ops.info({'report'}, json_data)
        print("Import Success : json_data")
        props.json_state_bool = True
        return {'FINISHED'}

# 第一级：建筑 / 多物件 / 单物件
def GetBranch_1(self,context):
    props = bpy.context.scene.second_props
    branch_1 = []
    if(props.json_state_bool):
        index = 0
        # TODO：json_data全局变量
        for item in json_data[0]['topic']['topics']:
            branch_1.append((str(index) , item['title'] , ""))
            # 这一行是类比enumproperty的格式写的，写法请见properties.py搜索“写法存档：常规枚举属性”
            index += 1
    else:
        branch_1 = [
            ('0', '未导入', ''),
            ('0', '未导入', ''),
            ('0', '未导入', '')
        ]
    return branch_1

def GetBranch_2(self,context):
    props = bpy.context.scene.second_props
    if(props.json_state_bool):
        index = 0
        branch_2 = []
        for i in json_data[0]['topic']['topics'][int(props.enum_branch_1_prop)]['topics']:
            branch_2.append((str(index) , i['title'] , ""))
            index += 1
        # for i in range(len(branch_2)):
        #     print(branch_2[i])
        return branch_2
    else:
        return []

# 清空 json数据
class Clear_Json(bpy.types.Operator):
    bl_idname = "file.json_clear"
    bl_label = "Clear_Json"

    def execute(self, context):
        global json_data
        json_data = []
        props = context.scene.second_props
        props.json_state_bool = False
        return {'FINISHED'}

blender_classes = [
    RenameObjectOperator,
    CreateNewCollection,
    CreateCube,
    Import_Json,
    Clear_Json,
]

def register():
    for b_class in blender_classes:
        bpy.utils.register_class(b_class)

def unregister():
    for b_class in blender_classes:
        bpy.utils.unregister_class(b_class)