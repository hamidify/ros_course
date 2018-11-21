#!/usr/bin/env python
import rospy
from std_msgs.msg import String
total = 0
no_of_results = 0
def calculateTotal(result):
	global total 
	global no_of_results 
	total = total + int(result.data)
	no_of_results = no_of_results + 1
	rospy.loginfo("I recieved %s and the total is %s ",result.data, total)

def printInfo():
	print("Subscriber is shut down!")
	print("Number of results recived is ",no_of_results)
	print("The aveerage from the collected results is ", total / no_of_results )


def subscriber():
	rospy.init_node('subscriber', anonymous=True)
	sub = rospy.Subscriber('NumberGenerator', String, calculateTotal)
	rospy.on_shutdown(printInfo)
	rospy.spin()

if __name__ == '__main__':
	subscriber()
