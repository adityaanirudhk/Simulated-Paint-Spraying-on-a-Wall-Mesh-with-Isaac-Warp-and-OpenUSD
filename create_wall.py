
from pxr import Usd, UsdGeom

stage = Usd.Stage.CreateNew("scene.usda")

wall = UsdGeom.Cube.Define(stage, "/Wall")
wall.CreateSizeAttr(2.0)

wall.AddScaleOp().Set((2.0,0.1,2.0))

stage.SetDefaultPrim(wall.GetPrim())
stage.Save()

print("Created scene.usda")
