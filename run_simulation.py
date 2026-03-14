
import numpy as np

from spray_simulation import generate_spray, compute_hits
from paint_surface import PaintSurface
from visualization import save_texture

particles = 3000        #Number of spray particles 
steps = 200             #Number of steps for computation

fan_width = 0.3         #Traingular Fan Spray Parameters
fan_height = 0.1
spray_range = 1.0

surface = PaintSurface()

for step in range(steps):

    nozzle_x = -0.8 + 1.6*(step/steps)

    particle_pos = np.array([[nozzle_x,0,0]]*particles)

    directions = generate_spray(
        particles,
        fan_width,
        fan_height,
        spray_range
    )

    hits = compute_hits(particle_pos, directions)

    for hit in hits:

        x,y,z = hit

        u = int((x+1)*surface.width/2)
        v = int((y+1)*surface.height/2)

        surface.add_paint(u,v)

    if step % 50 == 0:
        save_texture(surface.paint, f"paint_step_{step}.png")

save_texture(surface.paint,"paint_final.png")

print("Simulation complete")
