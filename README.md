# Arm Robot simulation with ROS2 and Gazebo.
  
this package requires ros2_control, ros2_controllers and gazebo_ros2_control package to be used. 
  
to see the model on rviz use:
```
ros2 launch arm_robot rviz.launch.py
```
to run the simulation on gazebo use:
```
ros2 launch arm_robot launch_sim.launch.py
```
you can move the angle(in degrees) of each axis using this command:
```
ros2 launch arm_robot control.launch.py ax1:=0 ax2:=0 ax3:=0
```
![alt text](https://github.com/MickySukmana/arm_robot/blob/main/img/lr.png?raw=true)
