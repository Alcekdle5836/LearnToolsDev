import bpy
from bpy.types import PropertyGroup
from bpy.props import(
    IntProperty,
    StringProperty,
    PointerProperty,
    EnumProperty,
)

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