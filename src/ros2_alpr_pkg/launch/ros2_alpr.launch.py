from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros2_alpr_pkg',
            executable='ros2_alpr',
            output='screen'),
    ])
