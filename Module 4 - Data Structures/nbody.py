import math


def solve():
    t = 157788000  # total time of simulation
    dt = 25000  # time delta

    # [xPos, yPos, xVel, yVel, mass]
    earth = [1.4960e+11, 0.0000e+00, 0.0000e+00, 2.9800e+04, 5.9740e+24]
    mars = [2.2790e+11, 0.0000e+00, 0.0000e+00, 2.4100e+04, 6.4190e+23]
    mercury = [5.7900e+10, 0.0000e+00, 0.0000e+00, 4.7900e+04, 3.3020e+23]
    sun = [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 1.9890e+30]
    venus = [1.0820e+11, 0.0000e+00, 0.0000e+00, 3.5000e+04, 4.8690e+24]

    # Create a nested list containing the input planet data from above
    bodies = [earth, mars, mercury, sun, venus]

    n = len(bodies)  # Number of planets
    g = 6.67E-11  # Gravitational force
    sun_index = 3  # Index of the sun on the array list
    sun_mass = sun[4]  # Mass of the sun

    t_total = 0.0

    while t_total < t:
        for i in range(n):
            # Skip the sun
            if i == sun_index:
                continue

            planet = bodies[i]
            px = planet[0]
            py = planet[1]
            vx = planet[2]
            vy = planet[3]
            m = planet[4]

            # Calculate the radius between i'th planet and the sun
            # Note that the sun is at the origin
            r = math.sqrt(math.pow(px, 2) + math.pow(py, 2))

            # Calculate the pair-wise force between i'th planet and the sun
            f = -(g * m * sun_mass) / math.pow(r, 2)

            # Calculate the x and y components of the force
            fx = f * (px / r)
            fy = f * (py / r)

            # Calculate the x and y components of the acceleration for the current timestep
            ax = fx / m
            ay = fy / m

            # Calculate the x and y components of the velocity for the next time step
            planet[2] = vx + ax * dt
            planet[3] = vy + ay * dt

            # Calculate the x and y components of the resulting position
            planet[0] = px + planet[2] * dt
            planet[1] = py + planet[3] * dt

        # Update the time by delta_t
        t_total = t_total + dt

    # Output the formatted values for the x and y components of position / velocity and mass
    for i in range(n):
        # Print formatted output for each planet
        planet = bodies[i]
        px = planet[0]
        py = planet[1]
        vx = planet[2]
        vy = planet[3]
        m = planet[4]
        print(f"{px:1.4e} {py:1.4e} {vx:1.4e} {vy:1.4e} {m:1.4e}")


if __name__ == '__main__':
    solve()
