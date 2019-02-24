#! /usr/bin/env python

import rospy

rospy.init_node('Greetings')
rate = rospy.Rate(.5)                # We create a Rate object of (1/2)hz -> 2 sec
while not rospy.is_shutdown():      # Endless loop until Ctrl + C
    print "Hello World!"
    rate.sleep()                    # sleep & repeat

# This program creates an endless loop that repeats itself 2 times per second (2Hz) until somebody presses Ctrl + C
# in the Shell