# ROS 2 Jazzy & TurtleBot3 Gazebo Control 

This provides an overview of ROS 2 and Gazebo simulation concepts, details the communication topics used to execute the `test.py` script with a TurtleBot3 robot.

---

## 1. Overview of ROS 2 & Gazebo Sim

### Core ROS 2 Middleware Concepts
* **Nodes**: Independent execution units (processes) that perform specific tasks.
* **Topics**: Data buses used by nodes to share information via a publisher-subscriber model.
* **Publishers**: Nodes use these to send data onto a topic.
* **Subscribers**: Nodes use these to listen to a topic and trigger callback functions when new data arrives.
* **Spinning**: The execution mechanism that keeps nodes alive and processes incoming messages.

---

## 2. Simulation Topics & Message Types

| Topic Name | Message Type | Direction | Description |
| :--- | :--- | :--- | :--- |
| `/cmd_vel` | `geometry_msgs/msg/TwistStamped` | **Published** by `test.py` | Sends linear and angular velocity commands to the robot. ROS Jazzy uses **TwistStamped** (includes timestamp header) for synchronization. |
| `/odom` | `nav_msgs/msg/Odometry` | **Subscribed** by `test.py` | Provides the robot's real-time position `(x, y)` and orientation (3D quaternion). |

---
## 3. Project Workflow
* Create a ROS 2 workspace.
* Implement the node in test.py.
* Configure setup.py and package.xml.
* Build the workspace using colcon.
* Source the generated workspace.
* Execute the node using ros2 run.
* Launch Gazebo for simulation if required.
