import numpy as np
from .benchmark_functions import dictionary as function_dictionary


class Particle:
    def __init__(self) -> None:
        x = np.random.uniform(Particle.x_low, Particle.x_high)
        y = np.random.uniform(Particle.y_low, Particle.y_high)
        self.position = np.array([x, y])
        self.velocity = np.random.randn(2)
        self.p_best = self.position
        self.next_velocity = self.get_velocity()

        if Particle.f(self.position) < Particle.f(Particle.global_best):
            Particle.global_best = self.position

    # global best
    global_best = np.random.randn(2)

    # parameters
    w = 0.8  # inertia
    c1 = 3.5  # weight of personal_best (exploration)
    c2 = 0.5  # weight of global_best (exploitation)

    # function environment
    f = None
    x_low = None
    x_high = None
    y_low = None
    y_high = None

    def update_position(self) -> None:
        curr_x = self.position[0]
        curr_y = self.position[1]

        self.velocity = self.next_velocity

        next_x = curr_x + self.velocity[0]
        next_y = curr_y + self.velocity[1]

        # boundary check
        if next_x < 0:
            next_x = max(next_x, Particle.x_low)
        else:
            next_x = min(Particle.x_high, next_x)

        if next_y < 0:
            next_y = max(next_y, Particle.y_low)
        else:
            next_y = min(Particle.y_high, next_y)

        self.position = np.array([next_x, next_y])
        self.next_velocity = self.get_velocity()

        if Particle.f(self.position) < Particle.f(self.p_best):
            self.p_best = self.position
            if Particle.f(self.position) < Particle.f(Particle.global_best):
                Particle.global_best = self.position

    def get_velocity(self) -> np.array:
        curr_vel_x = self.velocity[0]
        curr_vel_y = self.velocity[1]

        r1 = np.random.uniform(0, 1)
        r2 = np.random.uniform(0, 1)

        next_vel_x = Particle.w * curr_vel_x + Particle.c1 * r1 * (self.p_best[0] - self.position[0]) \
                     + Particle.c2 * r2 * (Particle.global_best[0] - self.position[0])
        next_vel_y = Particle.w * curr_vel_y + Particle.c1 * r1 * (self.p_best[1] - self.position[1]) \
                     + Particle.c2 * r2 * (Particle.global_best[1] - self.position[1])

        return np.array([next_vel_x, next_vel_y])

    @staticmethod
    def set_function_environment(function_number: int) -> None:
        Particle.f = function_dictionary[function_number]['func']
        Particle.x_low = function_dictionary[function_number]['x_low']
        Particle.x_high = function_dictionary[function_number]['x_high']
        Particle.y_low = function_dictionary[function_number]['y_low']
        Particle.y_high = function_dictionary[function_number]['y_high']
