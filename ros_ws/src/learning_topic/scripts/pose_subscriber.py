#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 如果运行出现问题：https://askubuntu.com/questions/896860/usr-bin-env-python3-r-no-such-file-or-directory

########################################################################
####          Copyright 2020 GuYueHome (www.guyuehome.com).          ###
########################################################################

# 该例程将订阅/turtle1/pose话题，消息类型turtlesim::Pose

import rospy
from turtlesim.msg import Pose

# 回调函数应该经可能简短，不能做嵌套循环、延时等操作，否则会影响接收其他消息
def poseCallback(msg):
    rospy.loginfo("Turtle pose: x:%0.6f, y:%0.6f", msg.x, msg.y)

def pose_subscriber():
	# ROS节点初始化
    rospy.init_node('pose_subscriber', anonymous=True)

	# 创建一个Subscriber，订阅名为/turtle1/pose的topic，注册回调函数poseCallback
    # 如果有消息到达，ROS就会调用poseCallback函数将消息传递给该回调函数
    rospy.Subscriber("/turtle1/pose", Pose, poseCallback)

	# 循环等待回调函数
    rospy.spin()

if __name__ == '__main__':
    pose_subscriber()


