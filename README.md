# Simulated-Paint-Spraying-on-a-Wall-Mesh-with-Isaac-Warp-and-OpenUSD
In this assignment, we will create a simulation that demonstrates spray painting a vertical wall surface. The simulation will model a spray nozzle emitting paint in a triangular fan pattern and will update the wall surface over time to reflect paint accumulation.

------------------------**This repository is currently under development and does not represent the final completed version of the project.**----------------------

# Scenario
  ● A single vertical cuboid mesh represents the wall.
  ● A spray nozzle moves in front of the wall.
  ● The spray has a triangular fan pattern with configurable parameters.
  ● Over time, paint accumulates where the spray impacts the wall.

# Using this project
# Installation

1. Clone the repository. (Alternatively you can download this repository and open the folder in VSCode)
 ```git clone https://github.com/adityaanirudhk/spray_paint_usd_project.git```
```cd spray_paint_usd_project```

2. Install dependencies
Ensure Python 3.10+ is installed.
Install required libraries:
`pip install numpy matplotlib usd-core`

Verify the installation of OpenUSD:
`python -c "from pxr import Usd;print(Usd.GetVersion())"`

# Running the Simulation
1. Requirements
`pip install usd-core numpy pillow`

2. To inspect results:
`usdview scene.usda`

-------->Steps

1. Create wall (This will create a .usda file indicating that the wall has been created successfully)
`python create_wall.py`

2. Run simulation (This code runs the simulation and generates images to view the results before moving to OpenUSD)
`python run_simulation.py`
Some results (in png) of the simulation are given in the Files attached with this repository. The pictures depict the progression of paint along the defined wall.

4. Update the same in the USD File
`python apply_texture.py`

3. Inspect scene
`usdview scene.usda`

# Confirming Paint Accumulation
Once the scene opens in Pixar USDView:
  1. Locate the wall surface in the Stage Tree
  2. Inspect the mesh properties
  3. Enable Display Color in the viewport
  4. Observe the triangular spray pattern on the surface

Correct simulation behavior should show:
  1. Higher paint accumulation near the center of the spray
  2. A triangular wedge distribution pattern
  3. Increasing paint density closer to the emitter axis


