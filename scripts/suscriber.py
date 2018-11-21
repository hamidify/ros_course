#!/usr/bin/env python
import rospy
from std_msgs.msg import String
def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heared %s", data.data)

def subscriber():
	rospy.init_node('subscriber', anonymous=True)
	rospy.Subscriber('NumberGenerator', String,callback)
	rospy.spin()

if __name__ == '__main__':
	subscriber()
