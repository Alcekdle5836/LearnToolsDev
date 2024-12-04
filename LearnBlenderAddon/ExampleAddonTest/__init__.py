bl_info = {
    "name" : "example addon",
    "author" : "Alec",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

if "bpy" in locals():
    import importlib

    reloadable_modules = [
        "properties",
        "functions"
        "ui"
        ]

    for module in reloadable_modules:
        if module in locals():
            importlib.reload(locals()[module])
from . import (properties,
               functions,
               ui
               )

def register():
    properties.register()
    functions.register()
    ui.register()

def unregister():
    ui.unregister()
    functions.unregister()
    properties.unregister()