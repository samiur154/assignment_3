# Third_assignment_RT1

Introduction
================================

Development of a software architecture for the control of a mobile robot. General idea to control a mobile robot in the gazebo area by different methods. The following ways to do this are divided into three parts:

1. Use the coordinates entered by the user 
2. Driving robots with keyboards
3. Drive robots through user, avoid going against obstacles
Developed code written in ros area in python language, it is possible to develop similar codes with the same concept in C++ language.

Materials and Methods
=========================

To make the following codes work on your system, you need to install the slam_gmapping package form: https://github.com/CarmineD8/slam_gmapping .You have to use the version adapted for your type of ros there are two types: 1.Kinetic and 2.Noetic in my case the second was used. The package can be downloaded from the following repository or by using fork directly in your ros workspace.

Actionlib stack was used in the developed code. Therefore you have to install actionlib in your repository, in case of lack of installation you can receive errors of type lack of attribution in the SimpleActionCliente or any type of attribution error on actionlib stack. For actionlib installation package to have more information can be found on: http://wiki.ros.org/actionlib.

Installing and running
----------------------
Once it was ready all the following cases you can download or fork, the repository in your workspace. At this stage to start the simulation you have to do:

1. Use: 
```
 $catkin_make
```
To compile the new packages installed on workspace, remember to use catkin_make in the workspace root file

2. Start two launch files:
```
$roslaunch final_assignment simulation_gmapping.launch
$roslaunch final_assignment move_base.launch
```
Practically with the first launch file you start the Gazebo and rviz simulator and you can see robots within the Gazebo and with second launch file you use to know the map and obstacles that is used to send goal to the robot.

Now then visualize this map in your system:
![photo_2022-01-26_11-50-54](https://user-images.githubusercontent.com/80394968/151150507-fb636911-7eff-4a1c-8d6b-32914645cd42.jpg)

It can happen to run the following launch files many times and finding an error on the operating system part (in my case linux) log file disk is full, because the directory that contains the cache file has a limited size so it can cause this. You can solve the following problem by doing:
```
$rosclean purge
```
Clears all cache files created by the system. Be careful in some cases it can also delete the cache important files so used only in case of need.

3. To make the first part work:
```
$rosrun final_assignment find_target.py
```
After following this command you will see in the terminal window asking you to enter the coordinates to search by the robot. The robot has 30 seconds timeout to find the target, if there is it before the task ends and asks for new coordinates otherwise the task fails and asks the user to enter new coordinates to reach.

4. To make second part work:
```
$rosrun final_assignment keyboard.py
```
The user can guide the robot in the Gazebo area with the keyboard, all the necessary instructions are reported in the terminal window. User must view a screen like this:
![photo_2022-01-26_11-56-49](https://user-images.githubusercontent.com/80394968/151151753-6be09f8f-6fc7-4b94-9e5d-114f78c9aae0.jpg)

5. To make third part work:
```
$roslaunch final_assignment assignment3.launch
```
For this part I used a launch file because there are more than one node to follow at the same time. The first node to guide with the keyboard the second node so as not to go against obstacles and the third node in case of finding a wall begins to follow it and not touch it even if the user forces him to go towards the wall.

Remember for this part a konsole opens in the system to guide the robot. If you have not installed konsole package you may have errors on execution of the program. To install it you can do: 
```
$sudo apt-get update
$sudo apt-get install konsole
```
Dynamic graph of what’s going on in the system

![photo_2022-01-26_19-06-21](https://user-images.githubusercontent.com/80394968/151221363-f6d84de5-d43d-46db-ab85-bd5434a9b2ae.jpg)

Flowchart(General idea behind the program)
----------------------
Structure of the first part
![Immagine 2022-01-26 202719](https://user-images.githubusercontent.com/80394968/151232902-d5e477ba-b2c5-4b06-aea0-e8fb43b75c78.jpg)

Structure of the second and third part
![Immagine 2022-01-26 202822](https://user-images.githubusercontent.com/80394968/151233142-af56c67a-9ed2-47b2-88bd-e73f8d451c0e.jpg)

