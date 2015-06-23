cmake_minimum_required(VERSION 2.8.3)
project(cob_demo)
find_package(catkin REQUIRED)
## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  cob_script_server
  smach
  smach_ros
  rospy
  cob_bringup
  cob_command_gui
  cob_dashboard
  std_srvs
  cob_light
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES hmi_scenario_states
#  CATKIN_DEPENDS other_catkin_pkg
#  DEPENDS system_lib
)

## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination
install(PROGRAMS 
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
