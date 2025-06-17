from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import ThisLaunchFileDir
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='autonomous',
            executable='latcher',
            name='latched_map_republisher'
        ),
        IncludeLaunchDescription(
            PathJoinSubstitution([
                FindPackageShare('autonomous'),
                'launch',
                'map.launch.py'
            ])
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', PathJoinSubstitution([FindPackageShare('autonomous'), 'config', 'rviz_config.rviz'])],
        )
    ])