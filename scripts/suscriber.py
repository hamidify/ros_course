#!/usr/bin/env python
import rospy
from std_msgs.msg import String
total = 90

def calculateTotal(result):
	global total 
	rospy.loginfo(total)
	total = total + int(result)

def printInfo():
	print("Publisher is down")

def callback(data):
	calculateTotal(data.data)
	rospy.loginfo(rospy.get_caller_id() + "I got %s", data.data)

def subscriber():
	total = 0
	rospy.init_node('subscriber', anonymous=True)
	sub = rospy.Subscriber('NumberGenerator', String,callback)
	rospy.on_shutdown(printInfo)

	# while sub.get_num_connections() == 0:
	# 	print("heere",sub.get_num_connections(), rospy.is_shutdown())
	# 	rospy.signal_shutdown ("publisher closed");
	rospy.spin()

if __name__ == '__main__':
	subscriber()
