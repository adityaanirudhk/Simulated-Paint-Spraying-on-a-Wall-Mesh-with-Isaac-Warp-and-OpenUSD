from pxr import Usd, UsdGeom, UsdShade, Sdf

stage = Usd.Stage.Open("scene.usda")

wall = stage.GetPrimAtPath("/Wall")

# Create material
material = UsdShade.Material.Define(stage, "/WallMaterial")

shader = UsdShade.Shader.Define(stage, "/WallMaterial/PBRShader")
shader.CreateIdAttr("UsdPreviewSurface")

# Texture shader
tex = UsdShade.Shader.Define(stage, "/WallMaterial/DiffuseTexture")
tex.CreateIdAttr("UsdUVTexture")
tex.CreateInput("file", Sdf.ValueTypeNames.Asset).Set("paint_final.png")

# Connect texture to material
shader.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).ConnectToSource(
    tex.ConnectableAPI(), "rgb"
)

material.CreateSurfaceOutput().ConnectToSource(shader.ConnectableAPI(), "surface")

# Bind material to wall
UsdShade.MaterialBindingAPI(wall).Bind(material)

stage.Save()

print("Texture applied to wall")