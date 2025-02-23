import bpy
from . import functions
from bpy.types import PropertyGroup
from bpy.props import(
    IntProperty,
    StringProperty,
    PointerProperty,
    EnumProperty,
    BoolProperty,
)

def update_function(self,context):
    self.new_label_name = self.dynamic_enum_1 + '/' + self.dynamic_enum_2 + '/' + self.dynamic_enum_3
    print("enum property has been update!")

def obj_list_callback(self,context):
    res = [] 
    objs = bpy.data.objects
    
    for obj in objs:
        tupe = (obj.name, obj.name, '')
        res.append(tupe)

    if len(objs) == 0:
        res.append(('!','!',''))
    return res

def get_new_name(self , context):
    # ('0', '建筑', ''), ('1', '多物件组装', ''), ('2', '单物件', '')
    name_json_1 = functions.GetBranch_1(self, context)[int(self.enum_branch_1_prop)][1].split('_' , -1)[0]
    name_json_2 = functions.GetBranch_2(self, context)[int(self.enum_branch_2_prop)][1].split('_' , -1)[0] 
    name_json_3 = self.enum_branch_4_prop
    return name_json_1  + ' / ' + name_json_2 + ' / ' + name_json_3

def get_fbx_export_path(self):
    pathExport = self.path_project_string
    # pathExport = self.path_project_string + "/Art/MapSources/Architecture/LiDanYang/" + bpy.context.active_object.name.split("_")[0] + "/" + bpy.context.active_object.name.split("_")[1] + "/" + bpy.context.active_object.name.split("_")[0] + "_" + bpy.context.active_object.name.split("_")[1] + "_" + bpy.context.active_object.name.split("_")[2] + "/" + "Fbx" + "/" + "High"
    # pathExport = self.path_project_string + "/Art/MapSources/Architecture/LiDanYang/" + str(functions.name_fbx_1) + "/" + str(functions.name_fbx_2) + "/" + str(functions.name_fbx_1) + "_" + str(functions.name_fbx_2) + "_" + str(functions.name_fbx_3) + "/" + "Fbx" + "/" + "High"
    return pathExport

def update_new_name(self , context):
    self.new_name_string = self.enum_branch_1_prop + ' / ' + self.enum_branch_2_prop + ' / ' + self.enum_branch_4_prop
    self.new_name_string_2 = get_new_name(self,context)

class SecondProperties(PropertyGroup):
    new_name : StringProperty(
        name = "",
        default = "this is new name"
    )

    new_collection : StringProperty(
        name = "",
        default = "this is new collection",
    )

    size_monkey : IntProperty(
        name = "",
        default = 2,
        min = 5,
        max = 20,
    )

    color_enum : EnumProperty(
        name = "",
        # 静态写法
        # items = [
        #     ("0","第1个元素",""),
        #     ("1","第2个元素",""),
        #     ("2","第3个元素",""),
        # ]
        # 动态写法
        items = obj_list_callback,
    )

    dynamic_enum_1 : EnumProperty(
        name="",
        items=[
            ("1","1",""),
            ("2","2",""),
            ("3","3",""),
            ("4","4",""),
        ],
        update = update_function,
    )

    dynamic_enum_2 : EnumProperty(
        name="",
        items=[
            ("建筑_index","建筑",""),
            ("多物件组装_index","多物件组装",""),
            ("3_index","3",""),
            ("4_index","4",""),
        ],
        update = update_function,
    )

    dynamic_enum_3 : EnumProperty(
        name="",
        items=[
            ("1","1",""),
            ("2","2",""),
            ("3","3",""),
            ("4","4",""),
        ],
        update = update_function,
    )

    dynamic_enum_4 : EnumProperty(
        name="",
        items=[
            ("1","1",""),
            ("2","2",""),
            ("3","3",""),
            ("4","4",""),
        ],
        update = update_function,
    )

    new_label_name : StringProperty(
        name = "",
        default = ""
    )

    # json文件路径
    path_json_string : StringProperty(
        name = "",
        # TODO:默认路径
        default = r"LearnToolsDev/LearnBlenderAddon/Script/NewPattern.json",
        subtype = 'FILE_PATH',              # 用于添加文件夹图标
    )

    # 项目路径
    path_project_string : StringProperty(
        name = "",
        default = "E:/Unity Projects/SESUN_HDRP/Assets",
        subtype = 'FILE_PATH',
    )

    # fbx导出路径
    fbx_export_path : StringProperty(
        name = "",
        default="请先导入Json",
        # FIXME:如何持续回调函数？
        get = get_fbx_export_path
    )

    # json数据是否已导入
    json_state_bool : BoolProperty(
        name = "",
        default = False,        # 默认flase为空
    )

    new_name_string : StringProperty(
    name = "",
    default = "default",
    )

    new_name_string_2 : StringProperty(
        name = "",
        default = "default",
    )

# 建筑配置
    enum_branch_1_prop: EnumProperty(
        name = "第1级",
        items = functions.GetBranch_1,
        update = update_new_name,
        default=0,
    )

    enum_branch_2_prop: EnumProperty(
        name = "第2级",
        items = functions.GetBranch_2,
        default= 0,
        update = update_new_name,
    )

    enum_branch_4_prop: EnumProperty(
        name = "第4级",
        items = [
            ("A","A",""),
            ("B","B",""),
            ("C","C",""),
            ("D","D",""),
            ("E","E",""),
        ],
        default=0,
        update = update_new_name,
    )

# 物体轴心点
    enum_pivot_prop_x: EnumProperty(
        name = "",
        items=[
            ("0","+x",""),
            ("1","0",""),
            ("2","-x",""),
        ]
    )
    enum_pivot_prop_y: EnumProperty(
        name = "",
        items=[
            ("0","+y",""),
            ("1","0",""),
            ("2","-y",""),
        ]
    )
    enum_pivot_prop_z: EnumProperty(
        name = "",
        items=[
            ("0","+z",""),
            ("1","0",""),
            ("2","-z",""),
        ]
    )


blender_classes = [
    SecondProperties,
]

def register():
    for b_class in blender_classes:
        bpy.utils.register_class(b_class)
    bpy.types.Scene.second_props = PointerProperty(type = SecondProperties)

def unregister():
    for b_class in blender_classes:
        bpy.utils.unregister_class(b_class)
    del bpy.types.Scene.second_props