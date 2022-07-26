from pso import Particle
import optimization_animation


PARTICLES = 30  # number of particles
FUNCTION_NUM = 7  # number of the function that you want to perform PSO on

# set up Particles' function environment
Particle.set_function_environment(FUNCTION_NUM)

# generate particles
particles = [Particle() for _ in range(PARTICLES)]

# create gif
optimization_animation.demonstrate(particles, FUNCTION_NUM, interval=80, dpi=120, iterations=100, cmap='magma')
