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
        layout.label(text="动态枚举 - 静态属性")
        # row / column
        row = layout.row()
        row.label(text = "建筑多级分类:")
        row.prop(props,"dynamic_enum_1",text="第1级")
        row.prop(props,"dynamic_enum_2",text="第2级")
        row.prop(props,"dynamic_enum_3",text="第3级")
        row.prop(props,"dynamic_enum_4",text="第4级")
        # row = layout.row()
        # 挤在一行
        # col 和 layout是相同效果
        col = layout.column()
        col.label(text="新标签：" + props.new_label_name)

blender_classes = [
    RenameObject,
    SetCollection,
    CreatePrimitive,
    DynamicEnum,
]

def register():
    for b_class in blender_classes:
        bpy.utils.register_class(b_class)

def unregister():
    for b_class in blender_classes:
        bpy.utils.unregister_class(b_class)