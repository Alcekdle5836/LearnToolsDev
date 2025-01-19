import bpy
import json
import mathutils

json_data = []

# 当前选中物体的xyz的最小最大值
# 无穷 infinite
max_z = 0
min_z = 0

max_x = 0
min_x = 0

max_y = 0
min_y = 0

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

# 通过游标的位置，移动轴心点至特定XYZ
# 游标：标志
def MovePivot(X , Y , Z):
    saved_location = bpy.context.scene.cursor.location.copy()       # 当前游标位置
    # Move the cursor to the location you want the new pivot point to be
    obj = bpy.context.active_object
    bpy.context.scene.cursor.location = mathutils.Vector((X, Y, Z))

    # Set the origin to the cursor's location
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    # 可以将轴心点移动到特定位置，但是无法将轴心点移动到给定位置
    # 如果想直接移动，可以结合3D游标实现

    # Restore the cursor's location
    bpy.context.scene.cursor.location = saved_location

    # 当遇到全局变量被修改的情况时，需要尤其考虑全局变量是否需要重置
    global max_z
    max_z = 0

    global max_x
    max_x = 0

    global max_y
    max_y = 0

    global min_z
    min_z = 0

    global min_x
    min_x = 0

    global min_y
    min_y = 0

# 拿到选中物体的最小值最大值，并修改全局变量
# 为了方便在MovePivot函数中修改轴心点时获取到
def ComputeBoundingBox(target_object):
    import mathutils
    # math utilities

    if target_object.type == 'MESH':
        # 列表推导式
        # objs = [...]
        # obj_list = [obj for obj in objs if obj.type = 'MESH']

        # TODO:通过matrix_world移动轴心点
        world_corners = [target_object.matrix_world @ mathutils.Vector(corner) for corner in target_object.bound_box]
        # target_object.matrix_world @ mathutils.Vector(corner)是将corner转为世界坐标
        # target_object.matrix_world 是4x4的矩阵，用于将对象从local space转为world space
        # @ 是矩阵乘法

        # color.r     color.x
        # color.g     color.y
        # color.b     color.z

        # Compute the min and max of each coordinate
        global min_x
        min_x = min(corner.x for corner in world_corners)
        global max_x
        max_x = max(corner.x for corner in world_corners)
        global min_y
        min_y = min(corner.y for corner in world_corners)
        global max_y
        max_y = max(corner.y for corner in world_corners)
        global min_z
        min_z = min(corner.z for corner in world_corners)
        global max_z
        max_z = max(corner.z for corner in world_corners)

class SetObjectPivot(bpy.types.Operator):
    bl_idname = "objects.set_object_pivot"
    bl_label = "Set select object pivot"

    def execute(self,context):
        # 目标轴心点位置
        pivot_x = 0
        pivot_z = 0
        pivot_y = 0

        props = context.scene.second_props
        selected_objects = bpy.context.selected_objects
        # for item in selected_objects[0].bound_box:
        #     print(item[0],item[1],item[2])
        for obj in selected_objects:
            ComputeBoundingBox(obj)     # AABB,返回xyz最大最小值
            
            # X
            if(props.enum_pivot_prop_x == '0'):
                pivot_x = max_x
            elif(props.enum_pivot_prop_x == '1'):
                pivot_x = 0.5 * (max_x + min_x)
            else:
                pivot_x = min_x

            # Y
            if(props.enum_pivot_prop_y == '0'):
                pivot_y = max_y
            elif(props.enum_pivot_prop_y == '1'):
                pivot_y = 0.5 * (max_y + min_y)
            else:
                pivot_y = min_y

            # Z
            if(props.enum_pivot_prop_z == '0'):
                pivot_z = max_z
            elif(props.enum_pivot_prop_z == '1'):
                pivot_z = 0.5 * (max_z + min_z)
            else:
                pivot_z = min_z
            
            MovePivot(pivot_x , pivot_y , pivot_z)
        return {'FINISHED'}


blender_classes = [
    RenameObjectOperator,
    CreateNewCollection,
    CreateCube,
    Import_Json,
    Clear_Json,
    SetObjectPivot,
]

def register():
    for b_class in blender_classes:
        bpy.utils.register_class(b_class)

def unregister():
    for b_class in blender_classes:
        bpy.utils.unregister_class(b_class)