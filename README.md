# husarion_ugv_ros

![Fork](https://img.shields.io/badge/repo-forked-blue)

> ⚠️ This is a **fork** of [husarion/husarion_ugv_ros](https://github.com/husarion/husarion_ugv_ros), using the `ros2` branch.  

This fork contains the complete codebase for **ERC-2025** development.

---

## Quick Start

### 1. Create Workspace

Clone this repo into your ROS workspace:

```bash
git clone https://github.com/TeamAurora-PSGiTech/ERC-2025.git
```

### 2. Configure Environment

This repository supports both **real robot** and **simulation** modes. Set the build type accordingly:

Real robot:
```bash
export HUSARION_ROS_BUILD_TYPE=hardware
```

Simulation:
```bash
export HUSARION_ROS_BUILD_TYPE=simulation
```

### 3. Build

```bash
vcs import . < husarion_ugv/${HUSARION_ROS_BUILD_TYPE}_deps.repos

sudo rosdep init
rosdep update --rosdistro $ROS_DISTRO
rosdep install --from-paths . -y -i

colcon build --symlink-install --packages-up-to husarion_ugv --cmake-args -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=OFF

source install/setup.bash
```

---

## Repository Structure

| Directory       | Description                            |
|-----------------|----------------------------------------|
| `/husarion_ugv_*` | Forked directories from upstream repo  |
| `/models`       | Contains all the ML models used        |
| `/autonomous` | Contains scripts and launch files for autonomous nav |
---

## Autonomous Mode

Step 0: Build the package
```bash
colcon build --packages-select autonomous --symlink-install
```

Step 1: Start simulation using the command
```bash
ros2 launch husarion_ugv_gazebo simulation.launch.py use_rviz:=False
```

Step 2: launch map and rviz with the command
```bash
ros2 launch autonomous nav.launch.py
```

Step 3: Launch navigation with
```bash
ros2 launch nav2_bringup navigation_launch.py use_sim_time:=true params_file:=autonomous/config/nav2_params.yaml
```
Step 4: Set goal pose and see navigating

---