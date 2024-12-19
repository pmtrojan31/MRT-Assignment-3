from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([

        ExecuteProcess(
            cmd=['ign', 'gazebo', 'Desktop/gazebo/models/simple_rover/simple_rover.sdf'],
            output='screen',
            shell=True
        ),

        # Launch ROS 2 bridge for /cmd_vel topic
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=['/model/simple_rover/cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist'],
            output='screen'
        ),

        # If instead of manually publishing velocity commands on the terminal, if a dedicated node is needed simply uncomment the following code

        # Node(
        #     package='my_diff_drive',
        #     executable='velocity_publisher',
        #     output='screen'
        # )
    ])
