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
_Link_ - https://github.com/ruthwikdasyam/A_Star_Project_32.git

### Instructions

Directly run the code {p1_ruthwik_zahir.py} in terminal or in code editor(s) (VScode, PyCharm)


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


## Sample Input :

* _Clearance_ : 5
* _Start Point_ :    x -> 1000;
                    y -> 1000;
                    theta -> 30
* _Goal Point_ :   x -> 5500;
                   y -> 600
* _RPM_ :   RPM1 -> 40;
            RPM2 -> 80

# Part 2

_Link_ - https://github.com/ruthwikdasyam/Astar_gazebo.git

The Simulation consists of a Turtlebot3 - Waffle Robot in a closed environment in Gazebo

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

### Steps
1. Input Clearance: 

    - _Clearance value for the obstacles_ - _centimeters_ {int}

_[Note]: Wait for the map to get generated

2. Input Goal Point
   
    -  _Coordinates w.r.t Cartesian frame_  
        - _x_ - _millimeters_ {int}
        - _y_ - _millimeters_ {int}


4. Input RPM - _Left and Right_
    - _RPM1 - {int}_ 
    - _RPM2 - {int}_

## Sample Inputs :
#### Sample 1:
*  _Clearance_ : 5
* _Goal Point_ :    
    - x -> 5500
    - y -> 1000
* _RPM_ :  
    - RPM1 -> 37
    - RPM2 -> 75

#### Sample 2:
* _Clearance_ : 5
* _Goal Point_ :   
    - x -> 5500
    - y -> 600
* _RPM_ :  
    - RPM1 -> 40
    - RPM2 -> 80


- Wait for the A star to complete path finding
- Once Goal Node is found, Backtracking is executed
- The pygame window displays the nodes explored and path from start to end node
- CLOSE the pygame window eith x button at the top right corner of the window to EXIT
- GAZEBO will automatically fires up turtlebot and you can see turtlebot following the same path, and Stops after reaching the Goal
  

#### _[Important Note]_
* The angular velocities computed are multiplied by a consant p_angular
* This is to compensate the algorithm, Simulation performance differences
* The constant is based on the Systems Real time factor, and Performance capabilities
* Based on our hardware, and Real time factor (1), The p_linear is 1, and p_angular is set to 1.05
* Hence, this p_linear and p_angular are to be adjusted based on system

    [In the submitted video, the "_Real Time Factor is 1_"]





