from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        #DeclareLaunchArgument(
        #    name='scanner', default_value='scanner',
        #    description='Namespace for sample topics'
        #),
        #Node(
        #    package='pointcloud_to_laserscan', executable='dummy_pointcloud_publisher',
        #    remappings=[('cloud', [LaunchConfiguration(variable_name='scanner'), '/cloud'])],
        #    parameters=[{'cloud_frame_id': 'cloud', 'cloud_extent': 2.0, 'cloud_size': 500}],
        #    name='cloud_publisher'
        #),
        #Node(
        #    package='tf2_ros',
        #    executable='static_transform_publisher',
        #    name='static_transform_publisher',
        #    arguments=[
        #        '--x', '0', '--y', '0', '--z', '0',
        #        '--qx', '0', '--qy', '0', '--qz', '0', '--qw', '1',
        #        '--frame-id', 'map', '--child-frame-id', 'cloud'
        #    ]
        #),
        Node(
            package='pointcloud_to_laserscan', executable='pointcloud_to_laserscan_node',
            remappings=[('cloud_in', '/rs_top/camera/depth/color/points'),
                        ('footprint', '/published_footprint'),
                        ('scan', '/scan_pcl')],
            parameters=[{
                'target_frame': 'base_link',
                'transform_tolerance': 0.01,
                'min_height': 0.15,
                'max_height': 0.5,
                'angle_min': -0.872665,  # -M_PI/2
                'angle_max':  0.872665,  # M_PI/2
                'angle_increment': 0.0087,  # M_PI/360.0
                'scan_time': 0.3333,
                'range_min': 0.5,
                'range_max': 1.5,
                'use_inf': False,
                'inf_epsilon': 1.0
            }],
            name='pointcloud_to_laserscan',
            #prefix=['xterm -e gdb -ex run --args'],
        )
    ])
