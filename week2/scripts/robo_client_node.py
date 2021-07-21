#!/usr/bin/env python

import rospy
from week2.srv import *
import matplotlib.pyplot as plt


def return_traj_client(x, y, theta, v, w):
    rospy.wait_for_service('return_traj')
    try:
        return_traj = rospy.ServiceProxy('return_traj', roboCmd)
        resp = return_traj(x, y, theta, v, w)
        x_points = resp.x_traj
        y_points = resp.y_traj

        plt.figure()
        plt.title("Unicycle Model")
        plt.xlabel("X-Coordinates")
        plt.ylabel("Y-Coordinates")
        plt.plot(x_points, y_points, color="red", alpha=0.75)
        plt.grid()
        plt.show()

    except rospy.ServiceException as e:
        print("Service not found")

if __name__ == "__main__":
    return_traj_client(0, 0, 0, 1, 0.5)
