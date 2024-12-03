import bpy

from bpy.types import PropertyGroup
from bpy.props import (
    IntProperty,
    BoolProperty,
    StringProperty,
    PointerProperty,
    EnumProperty,
    )

bl_info = {
    "name" : "simple addon",
    "author" : "Johnny",
    "description" : "",
    "blender" : (3, 2, 0),
    "version" : (0, 0, 1),
    # 备注该插件添加到blender中的位置
    "location" : "3D Viewport > Sidebar > TEST",
    "warning" : "",
    "category" : "Development"
}

# 对于物体大小重命名修改
def rename_obj_update(self,context):
    props = context.scene.simple_props      # 获取当前场景中属性
    # context.scene: This accesses the current scene in Blender.
    if props.case_option:
        props.obj_name = props.obj_name.upper()
    else:
        props.obj_name = props.obj_name.lower()
    
def obj_list_callback(self,context):
    res = [] 
    
    objs = bpy.data.objects
    
    for obj in objs:
        tupe = (obj.name, obj.name, '')
        res.append(tupe)

    if len(objs) == 0:
        res.append(('!','!',''))
    return res

def obj_list_update(self,context):
    props = context.scene.simple_props
    props.obj_name = props.enum_prop


#UI面板
class HelloWorldPanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_SIMPLE_ADDON"
    bl_label = "Hello World" #显示标题
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Simple Tool"

    def draw(self, context):
        layout = self.layout
        props = context.scene.simple_props
        col = layout.column()
        col.label(text="1.简单Operator")
        col.operator("mesh.primitive_cube_add",text="创建cube")
 
        col.operator("example.add_cube_size",text="创建自定义cube")     # TODO:example 是啥东西？operator是不是默认就是button？
        col.prop(props, "cube_size", text = "cube尺寸")
        
        col.label(text="2.进阶Operator")
        row = layout.row()

        row.label(text=props.obj_name)
        row.prop(props, "case_option", text = "大小写")                 # 这里的case_option在属性中定义，继承BoolProperty。所以是toggle？
        
        col = layout.column()
        col.operator("example.set_unit",text="设置单位")
        col.operator("example.get_obj_info",text="获取物体信息")
        col.prop(props, "enum_prop", text = "物体列表")
        
        col.prop(props,"objs_count",text = "count")

class HelloWorldProp(bpy.types.PropertyGroup):
    cube_size : IntProperty(
        default = 1,
    )
    
    obj_name : StringProperty(
        default = "",
    )

    objs_count : IntProperty(
        name = "",
        default = 0,
    )
    
    case_option : BoolProperty(
        name = "",
        default = False,
        update = rename_obj_update,
        # TODO:这里的update是啥意思？
    )
    
    enum_prop: EnumProperty(
        name = "",
        description= "Object List",
        items = obj_list_callback,
        update = obj_list_update,
    )

# 新建cube
class AddCubeOperator(bpy.types.Operator):
    bl_idname = "example.add_cube_size"     # 这里的双引号里面的内容就是随便写的，代表使用一个string作为调用方法时的唯一ID而已
    # TODO:猜测idname在实际使用中代替Founction名称发挥调用方法的作用
    bl_label = "Add Cube Size"              # TODO:bl_label有啥用？整个脚本中都没用到啊

    def execute(self,context):      # TODO:execute和update看ppt
        props = context.scene.simple_props
        bpy.ops.mesh.primitive_cube_add(size=props.cube_size, enter_editmode=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

        return {'FINISHED'}

# 设置标准单位
class SetUnitOperator(bpy.types.Operator):
    bl_idname = "example.set_unit"
    bl_label = "Set Unit Length"

    def execute(self,context):
        bpy.context.scene.unit_settings.system = 'METRIC'
        bpy.context.scene.unit_settings.length_unit = 'METERS'
        return {'FINISHED'}

# 获取物体信息
class GetObjInfoOperator(bpy.types.Operator):
    bl_idname = "example.get_obj_info"
    bl_label = "find all objects"

    def execute(self,context):
        objs = bpy.data.objects
        props = context.scene.simple_props
        props.objs_count = len(objs)
        return {'FINISHED'}
    

blender_classes = [
    HelloWorldPanel,
    HelloWorldProp,
    AddCubeOperator,
    SetUnitOperator,
    GetObjInfoOperator,
]

def register():
    for bclass in blender_classes:
        bpy.utils.register_class(bclass)
    bpy.types.Scene.simple_props = PointerProperty(type=HelloWorldProp)
    # 为Scene定义了一个新的属性simple_props，并将一个指向HelloWorldProp类Instance的指针赋予它
    # Add a new property to the Scene object in Blender that is a reference to an instance of the HelloWorldProp class. 
    # This allows you to associate an instance of HelloWorldProp with each Scene object in Blender.
    # The PointerProperty(type=HelloWorldProp) is creating a new pointer property that points to an instance of the HelloWorldProp class

def unregister():
    del bpy.types.Scene.simple_props
    for bclass in blender_classes:
        bpy.utils.unregister_class(bclass)

# Determine whether the script is being run directly or being imported as a module.
# 当脚本直接运行的时候，__name__ 设置为“__main__”。当脚本作为模块导入时，__name__ 将设置为脚本/模块的名称。
# if __name__ == "__main__":
#     register()
register()