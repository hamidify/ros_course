#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def publisher():
	pub = rospy.Publisher('NumberGenerator',String, queue_size=10)
	rospy.init_node('publisher', anonymous=True)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		hello_str = 'Hello World %s' % rospy.get_time()
		rospy.loginfo(hello_str)
		pub.publish(hello_str)
		rate.sleep()

if __name__ == '__main__':
	try:
		publisher()
	except rospy.ROSInturruptEException:
		pass


