import bpy
from bpy.types import PropertyGroup
from bpy.props import(
    IntProperty,
    StringProperty,
    PointerProperty,
)

class SecondProperties(PropertyGroup):
    new_name : StringProperty(
        name = "",
        default = "this is new name"
    )

    new_collection : StringProperty(
        name = "",
        default = "this is new collection",
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