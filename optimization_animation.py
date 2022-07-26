import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from benchmark_functions import dictionary as function_dictionary
from pso import Particle
from typing import List


def demonstrate(particles: List[Particle], function_number: int,
                iterations: int = 100, number_of_points: int = 1000,
                interval: int = 100, dpi: int = 240,
                cmap: str = 'magma', file_path: str = None) -> None:
    # get the function
    f = function_dictionary[function_number]['func']

    # get the function's bounds
    x_low = function_dictionary[function_number]['x_low']
    x_high = function_dictionary[function_number]['x_high']
    y_low = function_dictionary[function_number]['y_low']
    y_high = function_dictionary[function_number]['y_high']

    # get the function's global minima
    minimum_x = function_dictionary[function_number]['minimum_x']
    minimum_y = function_dictionary[function_number]['minimum_y']

    # generate the plot points
    X = np.linspace(x_low, x_high, number_of_points)
    Y = np.linspace(y_low, y_high, number_of_points)
    X, Y = np.array(np.meshgrid(X, Y))
    Z = function_dictionary[function_number]['func'](np.array([X, Y]))

    # create figure and ax
    fig = plt.figure(figsize=(14, 7))
    ax2d = fig.add_subplot(1, 2, 1)
    ax3d = fig.add_subplot(1, 2, 2, projection='3d')
    fig.set_tight_layout(True)
    img = ax2d.imshow(Z, extent=[x_low, x_high, y_low, y_high], origin='lower', cmap=cmap, alpha=0.5)
    surf = ax3d.plot_surface(X, Y, Z, cmap=cmap, linewidth=0, alpha=0.5)
    fig.colorbar(img, ax=ax2d)

    # mark function's minimum point(s) (if known)
    if minimum_x != None and minimum_y != None:
        if function_number != 4 and function_number != 8:
            ax2d.plot(minimum_x, minimum_y, marker='x', markersize=5, color="white")
            ax3d.plot(minimum_x, minimum_y, f(np.array([minimum_x, minimum_y])), marker='x', markersize=5, color="white")
        else:
            for x in minimum_x:
                for y in minimum_y:
                    ax2d.plot(x, y, marker='x', markersize=5, color="white")
                    ax3d.plot(x, y, f(np.array([x, y])), marker='x', markersize=5, color="white")

    # contours on the 2d plot
    contours2d = ax2d.contour(X, Y, Z, 12, colors='black', alpha=0.4)

    # contours on 'xy' plane of the 3d plot
    contours_offset = f(np.array([minimum_x[0], minimum_y[0]])) if function_number == 4 or function_number == 8 \
        else f(np.array([minimum_x, minimum_y]))
    ax3d.contour(X, Y, Z, 12, offset=contours_offset, cmap='viridis')

    # add contours' z-value (height) as labels
    ax2d.clabel(contours2d, inline=True, fontsize=8, fmt="%.0f")

    # plot the particles' points and 2d arrows
    particle_plots2d = []
    particle_arrows2d = []
    particle_plots3d = []

    for particle in particles:
        # 2d points and arrows
        particle_plot2d = ax2d.scatter(particle.position[0], particle.position[1],
                                       marker='o', color='blue', alpha=0.5)

        particle_arrow2d = ax2d.quiver(particle.position[0], particle.position[1],
                                       particle.next_velocity[0], particle.next_velocity[1],
                                       color='black', width=0.004, angles='xy', scale=5, scale_units='xy', alpha=0.6)

        particle_plots2d.append(particle_plot2d)
        particle_arrows2d.append(particle_arrow2d)

        # 3d points
        particle_plot3d, = ax3d.plot(particle.position[0], particle.position[1], f(particle.position),
                                     marker='.', color='blue', alpha=1)

        particle_plots3d.append(particle_plot3d)

    # plot global best point
    global_best_plot2d = ax2d.scatter(Particle.global_best[0], Particle.global_best[1],
                                      marker='*', s=100, color='black', alpha=0.4)

    global_best_plot3d, = ax3d.plot(Particle.global_best[0], Particle.global_best[1], f(Particle.global_best),
                                    marker='*', color='black', alpha=0.4)

    # set plot dimensions
    ax2d.set_xlim([x_low, x_high])
    ax2d.set_ylim([y_low, y_high])

    ax3d.set_xlim([x_low, x_high])
    ax3d.set_ylim([y_low, y_high])

    # find global minimum (optimize)
    def iterate(t: int) -> None:
        for particle in particles:
            particle.update_position()

        # auto parameterization
        Particle.w = 0.4 * (t - iterations) ** 2 / (iterations ** 2) + 0.4  # slowly goes from 0.8 to 0.4
        Particle.c1 = -3.6 * (t / iterations) + 4.0  # goes from 4.0 to 0.4
        Particle.c2 = 3.5 * (t / iterations) + 0.1  # goes from 0.1 to 3.6

        sys.stdout.write(f'\riteration {t}: {Particle.global_best} ---- func. value: {f(Particle.global_best)}')
        sys.stdout.flush()

    # animation function
    def animate(t):
        iteration_text = f'Iteration {t + 1}'
        w_text = f'W = {format(Particle.w, ".2f")}'
        c1_text = f'C1 = {format(round(Particle.c1, 2), ".2f")}'
        c2_text = f'C2 = {format(round(Particle.c2, 2), ".2f")}'
        title = f'{iteration_text}            {w_text}    {c1_text}    {c2_text}'

        # Update the plot points and arrows coordinates
        ax2d.set_title(title)
        ax3d.set_title(f'{function_dictionary[function_number]["name"]}')
        for index, particle in enumerate(particles):
            particle_plots2d[index].set_offsets(particle.position.T)

            particle_arrows2d[index].set_offsets(particle.position.T)
            particle_arrows2d[index].set_UVC(particle.next_velocity[0], particle.next_velocity[1])

            particle_plots3d[index].set_data(particle.position[0], particle.position[1])
            particle_plots3d[index].set_3d_properties(f(particle.position))

        global_best_plot2d.set_offsets(Particle.global_best.reshape(1, -1))
        global_best_plot3d.set_data(Particle.global_best[0], Particle.global_best[1])
        global_best_plot3d.set_3d_properties(f(Particle.global_best))

        # Iterate the algorithm
        iterate(t + 1)

        return ax2d, particle_plots2d, particle_plots3d, particle_arrows2d, global_best_plot2d, global_best_plot3d

    # animate and save
    func_name = function_dictionary[function_number]['name']
    anim = FuncAnimation(fig, animate, frames=iterations, interval=interval, blit=False, repeat=True)
    if not file_path:
        file_path = f"demo\\{function_number}. {func_name} PSO low_res.gif"
    anim.save(file_path, dpi=dpi)
