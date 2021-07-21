#!/usr/bin/env python

import rospy
from week2.msg import hwMsg


_world = None
_hello = None

def read_hello(msg):
    global _hello
    _hello = msg.content
    
def read_world(msg):
    global _world
    _world = msg.content

def main():
    hw_pub = rospy.Publisher('helloworld', hwMsg, queue_size=10)


    rospy.init_node('hw_sub_node', anonymous=True)
    rospy.Subscriber("hello", hwMsg, read_hello)
    rospy.Subscriber("world", hwMsg, read_world)
    loop_rate = rospy.Rate(5)
    
    while _hello == None or _world==None:
        pass

    while not rospy.is_shutdown():
        hw_msg = hwMsg()
        hw_msg.content = _hello + ', ' + _world + '!'
        hw_pub.publish(hw_msg)
        loop_rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass