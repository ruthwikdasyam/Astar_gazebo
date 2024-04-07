# A* Algorithm - 2D + Gazebo
Simulation of turtlebot3 - _waffle_,  in Gazebo using A star Algorithm - Path planning [ENPM661]

## Team Members

Ruthwik Dasyam - ruthwik - 120405563

Zahiruddin Mahammad - zahirmd - 120407796

## Libraries Used
Python Libraries used for A*
 - numpy
 - heapq
 - pygame
 - time 


# Part 1

### Instructions

Directly run the code {a_star_ruthwik_zahiruddin.py} in terminal or in code editor(s) (VScode, PyCharm)

Map Dimensions - _600cm x 200cm_

### Inputs

1. Clearance: 

    - _Clearance value for the obstacles_ - _centimeters_ {int}


_[Note]: The Map gets generated based on the Clearance, it might take upto 5 seconds_

2. Start Point 

    - _Coordinates w.r.t Cartesian frame and orientation w.r.t horizontal axis_

        - _x_ - _millimeters_ {int}

        - _y_ - _millimeters_ {int}

        - _theta_ - _degrees_ {int}

3. Goal Point 
    
    -  _Coordinates w.r.t Cartesian frame_ 

        - _x_ - _millimeters_ {int}

        - _y_ - _millimeters_ {int}


4. RPM - _Left and Right_
    
    - _RPM1 - {int}_ 

    - _RPM2 - {int}_


# Part 2

The Simulation consists of a Turtlebot3 - Waffle Robot in a closed environment

The python executable computes the path and visualizes in Pygame window

**Only after closing the Pygame window, the path is executed in Gazebo**

### Instructions

Create a workspace and src and paste the package "turtlebot3_project3"
```
mkdir -p ~/project3_ws/src
cd ~/project3_ws/src
```

In 1st Terminal - Launch the Simulation using the command below
```
ros2 launch turtlebot3_project3 competition_world.launch.py
```

In 2nd Terminal - Run the python file to compute path and execute it in gazebo
```
ros2 run turtlebot3_project3 p2sim.py
```

### Inputs
1. Clearance: 

    - _Clearance value for the obstacles_ - _centimeters_ {int}


_[Note]: The Map gets generated based on the Clearance, it might take upto 5 seconds_


2. Goal Point 
    
    -  _Coordinates w.r.t Cartesian frame_ 

        - _x_ - _millimeters_ {int}

        - _y_ - _millimeters_ {int}


3. RPM - _Left and Right_
    
    - _RPM1 - {int}_ 

    - _RPM2 - {int}_

## Sample Inputs - Part 2
#### Sample 1:
*  _Clearance_ : 5

* _Goal Point_ :
    - x - 5500
    - y - 1000

* _RPM_ :
    - RPM1 - 37
    - RPM2 - 75

#### Sample 2:
* _Clearance_ : 5

* _Goal Point_ :
    - x - 5500
    - y - 600

* _RPM_ :
    - RPM1 - 40
    - RPM2 - 80





- Wait for the Algorithm to run
- Once Goal Node is found, Backtracking is executed
- The pygame window displays the nodes explored and path from start to end node
- Close the pygame window to exit
- Gazebo will automatically fires up turtlebot and you can see turtlebot following the same path, that is shown




