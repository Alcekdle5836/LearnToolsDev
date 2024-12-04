import bpy
from mathutils import *

from bpy.types import PropertyGroup,Panel
from bpy.props import (
    IntProperty,
    BoolProperty,
    StringProperty,
    PointerProperty,
    EnumProperty,
    CollectionProperty,
    PointerProperty,
    )

class ExampleProperties(PropertyGroup):
    my_int : IntProperty(default = 1)

class CustomPropertyGroup(PropertyGroup):
    prop1: StringProperty(name="", default="Property 1")
    prop2: IntProperty(name="Property 2", default=1, min=0, max=1000)


blender_classes = [
    ExampleProperties,
    CustomPropertyGroup,
]

def register():
    for bclass in blender_classes:
        bpy.utils.register_class(bclass)
    bpy.types.Scene.example_props = PointerProperty(type=ExampleProperties)
    bpy.types.Scene.my_custom_collection = CollectionProperty(type=CustomPropertyGroup)

def unregister():
    del bpy.types.Scene.example_props
    del bpy.types.Scene.my_custom_collection
    for bclass in blender_classes:
        bpy.utils.unregister_class(bclass)