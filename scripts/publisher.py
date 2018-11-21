#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from random import randint,choice
import string
def generateRandomResult():
	result = randint(0,101)
	return result

def generateRandomletter():
	return choice(string.ascii_uppercase) 


def publisher():
	pub = rospy.Publisher('NumberGenerator', String, queue_size=10)
	rospy.init_node('publisher', anonymous=True)
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
		studeent_name = generateRandomletter()
		result = generateRandomResult()
		# hello_str = 'Hello World %s' % rospy.get_time()
		# rospy.loginfo(hello_str)
		# pub.publish(hello_str)
		rospy.loginfo(result)
		pub.publish(str(result))
		rate.sleep()

if __name__ == '__main__':
	try:
		publisher()
	except rospy.ROSInterruptException:
		pass


