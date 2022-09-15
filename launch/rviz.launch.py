import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource

import xacro


def generate_launch_description():

    pkg_path = os.path.join(get_package_share_directory('arm_robot'))
    xacro_file = os.path.join(pkg_path,'description','robot.urdf.xacro')
    robot_description_config = xacro.process_file(xacro_file)
    rviz_config_path = os.path.join(pkg_path, 'rviz','default.rviz')
    launch_rsp_path = os.path.join(pkg_path, 'launch','rsp.launch.py')

    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    launch_rsp_path
                )
    )	
    start_rviz2 = Node(package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config_path]
    )
	
    start_joint_state_publisher_gui = Node(package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen'
    )
	
    return LaunchDescription([
        rsp,
        start_rviz2,
        start_joint_state_publisher_gui
    ])
