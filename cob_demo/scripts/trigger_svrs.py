#!/usr/bin/env python

from std_srvs.srv import Trigger
import rospy
from simple_script_server import *
sss = simple_script_server()
from std_msgs.msg import ColorRGBA
from cob_light.srv import *
from cob_light.msg import *

def setLightCyan_cb(req):
    sss.set_light("light_base","cyan")
    sss.set_light("light_torso","cyan")
    return
    
def setLightRed_cb(req):
    sss.set_light("light_base","red")
    sss.set_light("light_torso","red")
    return
    
def setLightGreen_cb(req):
    sss.set_light("light_base","green")
    sss.set_light("light_torso","green")
    return
    
def setLightCyanCircle_cb(req):
    rospy.wait_for_service('/light_torso/set_light')

    try:
      set_light_torso = rospy.ServiceProxy("/light_torso/set_light",SetLightMode)
      light_mode = LightMode()
      cyan_color = ColorRGBA()
      cyan_color.r = 0.0
      cyan_color.g = 1.0
      cyan_color.b = 0.5
      cyan_color.a = 0.4
      light_mode.colors.append(cyan_color)
      light_mode.mode = 7
      resp = set_light_torso(light_mode)
      print resp
      return
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e


def setMimicLaughing_cb(req):
    sss.set_mimic("laughing")
    return
    
def setMimicAsking_cb(req):
    sss.set_mimic("asking")
    return
    
def setMimicYes_cb(req):
    sss.set_mimic("yes")
    return
    
def setMimicBlinkingRight_cb(req):
    sss.set_mimic("blinking_right")
    return
    
def playSound_cb(req):
    sss.play("R2D2")
    return
    
def trigger_srvs():
    rospy.init_node('trigger_srvs')
    s = rospy.Service('/demo/setLightCyan', Trigger, setLightCyan_cb)
    s = rospy.Service('/demo/setLightRed', Trigger, setLightRed_cb)
    s = rospy.Service('/demo/setLightGreen', Trigger, setLightGreen_cb)
    s = rospy.Service('/demo/setLightCyanCircle', Trigger, setLightCyanCircle_cb)
    s = rospy.Service('/demo/setMimicLaughing', Trigger, setMimicLaughing_cb)
    s = rospy.Service('/demo/setMimicAsking', Trigger, setMimicAsking_cb)
    s = rospy.Service('/demo/setMimicYes', Trigger, setMimicYes_cb)
    s = rospy.Service('/demo/setMimicBlinkingRight', Trigger, setMimicBlinkingRight_cb)
    s = rospy.Service('/demo/playSound', Trigger, playSound_cb)
    print "Ready"
    rospy.spin()

if __name__ == "__main__":
    trigger_srvs()
