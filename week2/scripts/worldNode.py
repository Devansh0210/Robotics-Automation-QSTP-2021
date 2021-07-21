#!/usr/bin/env python

import rospy
from week2.msg import hwMsg

def main():
    hello_pub = rospy.Publisher('world', hwMsg, queue_size=10)

    rospy.init_node('worldNode', anonymous=True)
    loop_rate = rospy.Rate(5)

    while not rospy.is_shutdown():
        msg1 = hwMsg()
        msg1.content = "World"
        rospy.loginfo("Publishing: ")
        rospy.loginfo(msg1)

        hello_pub.publish(msg1)
        loop_rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass


