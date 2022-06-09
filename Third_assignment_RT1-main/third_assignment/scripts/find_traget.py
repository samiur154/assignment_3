#!/usr/bin/env python3
from time import sleep
import rospy
import actionlib
from geometry_msgs.msg import Pose
from move_base_msgs.msg import MoveBaseAction 
from move_base_msgs.msg import MoveBaseGoal
import time

def movebase_clinet():
    # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('/move_base',MoveBaseAction)
    # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    # Gets goal position from user
    goal.target_pose.pose.position.x = float(input("Enter x position: "))
    goal.target_pose.pose.position.y = float(input("Enter y position: "))
    # No rotation of the mobile base frame w.r.t. map frame
    goal.target_pose.pose.orientation.w = 1.0
    # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()
    # Sends the goal to the action server.
    client.send_goal(goal)	
    print("Timeout strat. Hurry up!!!")
    Timeout = client.wait_for_result(timeout=rospy.Duration(30))
    # detects if the target is reached before timeout
    if Timeout:
         print("I arrived")
         time.sleep(2)
         return client.get_result()
    else:
         print("Oops I couldn't make it in time!")
         time.sleep(2)
         client.cancel_all_goals()
         
def main():
    rospy.init_node('movebase_client')
    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
            movebase_clinet()

if __name__ == '__main__':
    main()
