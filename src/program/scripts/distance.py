#!/usr/bin/python 
import rospy
from apriltag_ros.msg import AprilTagDetectionArray
from std_msgs.msg import Float64

def callback(data):
    if len(data.detections)>0:
        rospy.loginfo(data.detections[0].id[0])
        cm=(data.detections[0].pose.pose.pose.position.z)*100
        rospy.loginfo(cm)
    else:
        rospy.loginfo("nodata")

        


def take():
    rospy.init_node('line')
    rospy.Subscriber("tag_detections",AprilTagDetectionArray,callback)
    rospy.spin()

if __name__=='__main__':
    take()