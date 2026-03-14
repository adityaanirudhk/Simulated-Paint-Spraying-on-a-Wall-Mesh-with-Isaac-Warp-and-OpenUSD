
# Spray Paint Simulation using OpenUSD

This project implements a spray paint simulation that follows the assignment tasks provided.

## Requirements
pip install usd-core numpy pillow

To inspect results:
usdview scene.usda

## Steps

1. Create wall (This will create a .usda file indicating that the wall has been created successfully)
python create_wall.py 

2. Run simulation (This code runs the simulation and generates images to view the results before moving to OpenUSD)
python run_simulation.py

3. Update the same in the USD File
python apply_texture.py

3. Inspect scene
usdview scene.usda

Outputs:
paint_step_0.png
paint_step_50.png
paint_step_100.png
paint_final.png

Texture applied to wall
