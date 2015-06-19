#!/usr/bin/env python

from std_srvs.srv import Trigger
import rospy
from simple_script_server import *
sss = simple_script_server()

def setLightCyan_cb(req):
    sss.set_light("light_base","cyan")
    sss.set_light("light_torso","cyan")
    return
    
def setMimicHappy_cb(req):
    sss.set_mimic("happy")
    return
    
def playSound_cb(req):
    sss.play()
    return
    
def trigger_srvs():
    rospy.init_node('trigger_srvs')
    s = rospy.Service('/demo/setLightCyan', Trigger, setLightCyan_cb)
    s = rospy.Service('/demo/setMimicHappy', Trigger, setMimicHappy_cb)
    s = rospy.Service('/demo/playSound', Trigger, playSound_cb)
    print "Ready"
    rospy.spin()

if __name__ == "__main__":
    trigger_srvs()
