bl_info = {
    "name" : "example addon",
    "author" : "课程插件",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "课程插件"
}

if "bpy" in locals():
    import importlib

    # 定义需要reload的模块
    reloadable_modules = ["properties","functions","ui"]

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