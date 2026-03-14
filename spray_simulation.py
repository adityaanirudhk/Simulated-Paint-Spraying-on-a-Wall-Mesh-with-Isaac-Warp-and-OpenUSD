
import numpy as np

def generate_spray(particles, fan_width, fan_height, spray_range):

    dirs = np.zeros((particles,3))

    dirs[:,0] = np.random.uniform(-fan_width, fan_width, particles)
    dirs[:,1] = np.random.uniform(-fan_height, fan_height, particles)
    dirs[:,2] = spray_range

    return dirs


def compute_hits(particle_pos, directions):

    hits = []

    for pos, d in zip(particle_pos, directions):

        if d[2] <= 0:
            continue

        t = (1 - pos[2]) / d[2]

        if t <= 0:
            continue

        hit = pos + t * d
        hits.append(hit)

    return hits
