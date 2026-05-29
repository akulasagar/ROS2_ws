# ROS2_ws

# ROS2 Bootcamp Progress (Day 1 & Day 2)

## Environment Setup

### Installed

* WSL2 Ubuntu 24.04
* ROS2 Jazzy
* VS Code with WSL integration
* Colcon build tools

### Workspace Structure

~/ros2_ws

src/

robot_interfaces/

counter_pkg/

turtle_controller/

---

# Day 1 – ROS2 Mechanics

## Concepts Learned

### Node

A node is an executable process that performs a specific task in ROS2.

Examples:

* Publisher Node
* Subscriber Node
* TurtleSim Node

### Topic

A topic is a communication channel between nodes.

Examples:

* /counter
* /robot_status
* /turtle1/cmd_vel

### Message

A message is the data exchanged between nodes.

Examples:

* std_msgs/Int32
* geometry_msgs/Twist
* RobotStatus

---

## Counter Publisher/Subscriber

Implemented:

* Int32 Counter Publisher
* Int32 Counter Subscriber

Flow:

Publisher
↓
Topic (/counter)
↓
Subscriber

---

## Custom Message

Created custom message:

RobotStatus.msg

Fields:

float32 battery_pct

string mode

int32 error_code

Example:

battery_pct: 95.0
mode: AUTO
error_code: 0

---

## RobotStatus Publisher

Publishes RobotStatus messages continuously.

Example Output:

Battery=95.0
Mode=AUTO
Error=0

---

## RobotStatus Subscriber

Receives RobotStatus messages and displays them.

---

## QoS Experiments

### Reliable + Keep All

Characteristics:

* No message loss
* Stores all messages

Use Case:

* Mission logs
* Critical telemetry

---

### Best Effort + Keep Last (Depth 1)

Characteristics:

* Fast
* Can drop messages

Use Case:

* Camera streams
* LiDAR data

---

### Reliable + Transient Local

Characteristics:

* New subscribers receive last stored messages

Use Case:

* Robot configuration
* Static map information

---

# Day 2 – URDF and Motion Control

## URDF Robot

Created Differential Drive Robot:

Links:

* base_link
* left_wheel
* right_wheel
* caster

Joints:

* Wheel joints
* Caster joint

Visualized in online URDF viewer.

---

## Joint Types

### Continuous Joint

* Unlimited rotation
* Used for wheels

Example:
Robot wheel

### Revolute Joint

* Limited rotation
* Has angle limits

Example:
Robot arm joint

---

# TurtleSim

Started TurtleSim:

ros2 run turtlesim turtlesim_node

Topics Observed:

/turtle1/cmd_vel
/turtle1/pose
/turtle1/color_sensor

---

## Twist Message

Used:

geometry_msgs/Twist

Important Fields:

linear.x
angular.z

Meaning:

linear.x → forward/backward speed

angular.z → rotational speed

---

# Manual Motion Test

Command:

ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0}, angular: {z: 1.0}}"

Result:

Turtle moved in circular motion.

---

# Draw Square Node

Package:

turtle_controller

Node:

draw_square.py

Logic:

Move Forward
↓
Turn Left
↓
Repeat 4 Times

Result:

Turtle drew a square.

---

# Draw Circle Node

Node:

draw_circle.py

Logic:

linear.x = 2.0

angular.z = 1.0

Result:

Turtle continuously drew a circle.

---

# Workspace Build

Build:

cd ~/ros2_ws

source /opt/ros/jazzy/setup.bash

colcon build --symlink-install

Source Workspace:

source ~/ros2_ws/install/setup.bash

---

# Demo Commands

## Verify Packages

ros2 pkg list | grep -E "robot_interfaces|counter_pkg|turtle_controller"

---

## Run RobotStatus Publisher

ros2 run counter_pkg robot_status_publisher

---

## Run RobotStatus Subscriber

ros2 run counter_pkg robot_status_subscriber

---

## Start TurtleSim

ros2 run turtlesim turtlesim_node

---

## Run Square Demo

ros2 run turtle_controller draw_square

---

## Run Circle Demo

ros2 run turtle_controller draw_circle

---

# Current Status

Day 1 Completed

* Publishers/Subscribers
* Custom Messages
* QoS Experiments

Day 2 Completed

* URDF Robot
* TurtleSim Motion Control
* Square Motion
* Circle Motion

Ready for Day 3: NestJS ↔ ROS2 Bridge
