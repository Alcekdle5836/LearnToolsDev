import bpy
from bpy.types import PropertyGroup
from bpy.props import(
    IntProperty,
    StringProperty,
    PointerProperty,
    EnumProperty,
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