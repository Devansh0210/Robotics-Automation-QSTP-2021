"""Week I Assignment
Simulate the trajectory of a robot approximated using a unicycle model given the
following start states, dt, velocity commands and timesteps
State = (x, y, theta);
Velocity = (v, w) 
1. Start=(0, 0, 0); dt=0.1; vel=(1, 0.5); timesteps: 25
2. Start=(0, 0, 1.57); dt=0.2; vel=(0.5, 1); timesteps: 10
3. Start(0, 0, 0.77); dt=0.05; vel=(5, 4); timestep: 50

Upload the completed python file and the figures of the three sub parts in classroom
"""
import numpy as np
import matplotlib.pyplot as plt

class Unicycle:
    def __init__(self, x: float, y: float, theta: float, dt: float):
        self.x = x
        self.y = y
        self.theta = theta
        self.dt = dt

        # Store the points of the trajectory to plot
        self.x_points = [self.x]
        self.y_points = [self.y]

    def step(self, v: float, w: float, n: int):
        """
        Write the Kinematics model here
        Expectation:
            1. Given v, w and the current state self.x, self.y, self.theta
                and control commands (v, w) for n timesteps, i.e. n * dt seconds,
                return the final pose (x, y, theta) after this time.
            2. Append all intermediate points into the self.x_points, self.y_points list
                for plotting the trajectory.

        Args:
            v (float): linear velocity
            w (float): angular velocity
            n (int)  : timesteps

        Return:
            x, y, theta (float): final pose 
        """

        for i in range(n):
            self.theta += w*self.dt   # angle = angle + angular_velociy * delta
            self.x += v*np.cos(self.theta)*self.dt # X = X + horizontal_velocity * delta
            self.y += v*np.sin(self.theta)*self.dt # Y = Y + vertical_velocity * delta
            self.x_points.append(self.x)
            self.y_points.append(self.y)

        return self.x, self.y, self.theta

    def plot(self, v: float, w: float):
        """Function that plots the intermeditate trajectory of the Robot"""
        plt.figure()
        plt.title(f"Unicycle Model: {v}, {w}")
        plt.xlabel("X-Coordinates")
        plt.ylabel("Y-Coordinates")
        plt.plot(self.x_points, self.y_points, color="red", alpha=0.75)
        plt.grid()

        # If you want to view the plot uncomment plt.show() and comment out plt.savefig()
        # plt.show()
        # If you want to save the file, uncomment plt.savefig() and comment out plt.show()
        
        plt.savefig(f"Unicycle_{v}_{w}.png")
   
if __name__ == "__main__":
    print("Unicycle Model Assignment")

    # make an object of the robot and plot various trajectories


    # 1. Start=(0, 0, 0); dt=0.1; vel=(1, 0.5); timesteps: 25
    uni = Unicycle(0, 0, 0, 0.1)
    uni.step(1, 0.5, 25)
    uni.plot(1, 0.5)
    # -------------------------

    # 2. Start=(0, 0, 1.57); dt=0.2; vel=(0.5, 1); timesteps: 10
    uni = Unicycle(0, 0, 1.57, 0.2)
    uni.step(0.5, 1, 10)
    uni.plot(0.5, 1)
    # -------------------------

    # 3. Start(0, 0, 0.77); dt=0.05; vel=(5, 4); timestep: 50
    uni = Unicycle(0, 0, 0.77, 0.05)
    uni.step(5, 4, 50)
    uni.plot(5, 4)
    # -------------------------


