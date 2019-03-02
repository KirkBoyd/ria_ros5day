#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry


# Define a function called 'callback' that receives a parameter
def callback(msg):
    # named 'msg'

    # Print the value 'data' inside the 'msg' parameter
    print msg


# Initiate a Node called 'topic_subscriber'
rospy.init_node('topic_subscriber')

# Create a Subscriber object that will listen to the /counter
sub = rospy.Subscriber('/odom', Odometry, callback)
# topic and will cal the 'callback' function each time it reads
# something from the topic
rospy.spin()
