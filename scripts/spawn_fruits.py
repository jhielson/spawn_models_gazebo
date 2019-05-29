#!/usr/bin/env python

#
#  Jhielson M. Pimentel
#  spawn several models on Gazebo
#

import rospy
import os
import random
from gazebo_msgs.srv import SpawnModel
from geometry_msgs.msg import Pose

def spawn_fruits(name,x,y):
    rospy.wait_for_service('gazebo/spawn_sdf_model')
    try:
	initial_pose = Pose()
	initial_pose.position.x = x
	initial_pose.position.y = y
	initial_pose.position.z = 0.8
        path = os.environ['HOME']
        f = open(path+'/catkin_ws/src/spawn_models_gazebo/models/crop/fruit/model.sdf','r')
        sdff = f.read()
        spawn_model = rospy.ServiceProxy('gazebo/spawn_sdf_model', SpawnModel)
        spawn_model(name, sdff, "robotos_name_space", initial_pose, "world")
        return 1
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def select_crop(x,y,i):
    total = int(random.randrange(1,5))
    for t in range(i, i+total):
        name = 'fruit'+str(t)
        crop_x = x
        crop_y = y
        spawn_x = random.uniform(crop_x-13,crop_x+13)
        spawn_y = random.uniform(crop_y-0,crop_y+0)
    	spawn_fruits(name,spawn_x,spawn_y)
    return (i+total)

if __name__ == "__main__":
    
    x = [-27.85,3.74,35.02]
    y = [-24.93,-23.00,-24.79]
    seq = 0
    for t in range(0,15):
    	seq = select_crop(x[0],y[0],seq)
        y[0] = y[0] + 3.7

    for t in range(0,14):
        if t != 6:
            seq = select_crop(x[1],y[1],seq)
        y[1] = y[1] + 3.7

    for t in range(0,15):
        seq = select_crop(x[2],y[2],seq)
        y[2] = y[2] + 3.7


