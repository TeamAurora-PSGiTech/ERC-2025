from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import ThisLaunchFileDir


def generate_launch_description():
    return LaunchDescription([
        IncludeLaunchDescription(
            PathJoinSubstitution([
                FindPackageShare('rtabmap_launch'),
                'launch',
                'rtabmap.launch.py'
            ]),
            launch_arguments={
                    "localization": "true",
                    "use_sim_time": "true",
                    "depth_topic": "/front_cam/zed_node/depth",
                    "rgb_topic": "/front_cam/zed_node/rgb/image_rect_color",
                    "camera_info_topic": "/front_cam/zed_node/camera_info",
                    "approx_sync": "true",
                    "rtabmap_args": "--delete_db_on_start --Mem/IncrementalMemory true --Mem/STMSize 50",
            }.items()
        )
    ])