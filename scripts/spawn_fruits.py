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
	initial_pose.position.z = 0.5
        path = os.environ['HOME']
        f = open(path+'/catkin_ws/src/spawn_models_gazebo/models/crop/fruit/model.sdf','r')
        sdff = f.read()
        spawn_model = rospy.ServiceProxy('gazebo/spawn_sdf_model', SpawnModel)
        spawn_model(name, sdff, "robotos_name_space", initial_pose, "world")
        return 1
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def select_crop(x,y,i):
    total = int(random.randrange(0,10))
    for t in range(i, i+total):
        name = 'fruit'+str(t)
        crop_x = int(x)
        crop_y = int(y)
        spawn_x = int(random.randrange(crop_x-13,crop_x+13))
        spawn_y = int(random.randrange(crop_y-2,crop_y+2))
    	spawn_fruits(name,spawn_x,spawn_y)
    return (i+total)

if __name__ == "__main__":
    
    x = [-36.61,-36.61,-36.61,-36.61,-36.61,-36.61,-36.61,2.77,2.77,
          2.77,2.77,2.77,2.77,35.29,35.29,35.29,35.29,35.29,35.29,35.29]
    y = [-48.12,-32.03,-16.56,-1.48,13.52,29.37,47.18,-39.20,-23.70,-9.04,7.01,21.14,38.62
         -48.20,-31.40,-15.93,0.34,15.25,31.75,47.87]
    seq = 0
    for t in range(0,19):
    	seq = select_crop(x[t],y[t],seq)


