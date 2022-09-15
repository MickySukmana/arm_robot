import sys
import math
from launch import LaunchDescription
import launch.actions
import launch_ros.actions

ax1 = 0
ax2 = 0
ax3 = 0

for arg in sys.argv:
    if arg.startswith("ax1:="):
        ax1 = float(arg.split(":=")[1])
	
    if arg.startswith("ax2:="):
        ax2 = float(arg.split(":=")[1])

    if arg.startswith("ax3:="):
        ax3 = float(arg.split(":=")[1])

ax1 = ax1 * (math.pi/180)
ax2 = ax2 * (math.pi/180)
ax3 = ax3 * (math.pi/180)

def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
            package='arm_robot',
            executable='control.py',
            output='screen',
            arguments=[str(ax1), str(ax2), str(ax3)]),
    ])
