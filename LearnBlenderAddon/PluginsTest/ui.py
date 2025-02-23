import bpy

class RenameObject(bpy.types.Panel):
    bl_idname = "RenameObject"
    bl_space_type = "VIEW_3D"           # 文档，搜一下
    bl_region_type = "UI"
    bl_label = "物体命名"
    bl_category = "BaseAddons"

    def draw(self,context):   
        props = context.scene.second_props
        layout = self.layout
        layout.prop(props,"new_name",text = "New Name")
        layout.operator("object.rename",text="物体重命名")

class SetCollection(bpy.types.Panel):
    bl_idname = "SetCollection"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "分组"
    bl_category = "BaseAddons"

    def draw(self,context):
        props = context.scene.second_props
        layout = self.layout
        layout.prop(props,"new_collection",text = "NewCollection")
        layout.operator("objects.new_collection",text = "创建Collection")

class CreatePrimitive(bpy.types.Panel):
    bl_idname = "OBJECT_PT_SIMPLE_ADDON"
    bl_label = "创建立方体"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "BaseAddons"

    def draw(self, context):
        props = context.scene.second_props
        layout = self.layout
        layout.operator("cube.create", text = "创建猴")
        layout.prop(props,"size_monkey", text = "monkey size111")
        layout.operator("mesh.primitive_cube_add", text = "创建立方体")
        layout.prop(props,"color_enum", text = "物体列表")

class DynamicEnum(bpy.types.Panel):
    bl_idname = "Enum"
    bl_label = "动态枚举"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "BaseAddons"

    def draw(self,context):
        props = context.scene.second_props
        layout = self.layout
        # 静态属性
        layout.label(text="动态枚举")
        layout.prop(props,"path_json_string",text="Json配置表文件路径")
        row = layout.row()
        row.operator("file.json_import",text="导入Json")
        row.operator("file.json_clear", text='清空 Json')
        # TODO:其他模式可以参考文档
        # row.alignment = 'EXPAND'

        row = layout.row()
        # row.label(text = "建筑多级分类:")
        # row.prop(props,"dynamic_enum_1",text="第1级")
        # row.prop(props,"dynamic_enum_2",text="第2级")
        # row.prop(props,"dynamic_enum_3",text="第3级")
        # row.prop(props,"dynamic_enum_4",text="第4级")
        row = layout.row()
        row.label(text="建筑命名列表：")
        row.prop(props,"enum_branch_1_prop")
        row.prop(props,"enum_branch_2_prop")
        row.prop(props,"enum_branch_4_prop")
        col = layout.column()
        row = layout.row()
        row.label(text="新命名index：" + props.new_name_string)
        row.label(text="新命名名称：" + props.new_name_string_2)

class SetPivot(bpy.types.Panel):
    bl_idname = "SetPivot"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "设置轴心点"
    bl_category = "BaseAddons"

    def draw(self,context):
        props = context.scene.second_props
        layout = self.layout
        layout.label(text="设置轴心点")

        row = layout.row()
        row.prop(props,"enum_pivot_prop_x")
        row.prop(props,"enum_pivot_prop_y")
        row.prop(props,"enum_pivot_prop_z")

        layout.operator("objects.set_object_pivot", text = "单个物体")

class ExportFbx(bpy.types.Panel):
    bl_idname = "ExportFbx"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "导出FBX"
    bl_category = "BaseAddons"

    def draw(self,context):
        props = context.scene.second_props
        layout = self.layout
        layout.label(text="导出FBX")
        layout.prop(props,"path_project_string",text="导出路径")
        layout.operator("file.fbx_export",text="导出FBX")

blender_classes = [
    RenameObject,
    SetCollection,
    CreatePrimitive,
    DynamicEnum,
    SetPivot,
    ExportFbx,
]

def register():
    for b_class in blender_classes:
        bpy.utils.register_class(b_class)

def unregister():
    for b_class in blender_classes:
        bpy.utils.unregister_class(b_class)