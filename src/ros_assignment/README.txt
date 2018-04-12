************************************************
***********HOW TO VIEW/RUN PROJECTS*************
************************************************
          ******NOTE******
#Setting up file source
1. After downloading the project from github, open terminal and go to the directory where it is downloaded.
2. Define source by typing in "source devel/setup.bash" in the terminal window.
3. Follow the instructions below to run programs in the file.
          ****Solution****
#1. Capture an image from the webcam and convert it to grayscale.
# Run image to grayscale converter by typing the following command
roslaunch ros_assignment image.launch

#2. Create interesting fractals using turtlesim.
# Run fractale by typing the following command
roslaunch ros_assignment fractale.launch

#3. Communicate messages between ROS and blender.
# Run blender controlled turtle by typing the following command
roslaunch ros_assignment blender.launch

#4. Make the second turtle follow or chase the first one using PID motion.
# Run chasing turtle simulation by typing the following command
roslaunch ros_assignment chase.launch

#5. Create GUI Application to drive turtle.
# Run GUI controlled turtle simulation by typing the following command
roslaunch ros_assignment gui.launch

************************************************
************************************************
************************************************

************************************************
***********DETAIL USAGE AFTER LAUNCH************
************************************************
          ****Picture Converting****
1. Grayscale image will be displayed on the right with webcam image on the left.
2.
          ****Fractale****
1. After lauching 'fractale.launch', press "CTRL+C" to close or end simulation.
2. Press <up>,<down>,<left> or <right> to change color.
          ****Blender****
1. After launching 'blender.launch', Blender and turtlesim will open.
2. Drag the object in blender window in the x-axis(Green line) to move the turtle.
3. Drag the object in blender window in the z-axis(Blue line) to rotate the turtle.
4. Drag the object in blender window in the all-axis to move and rotate the turtle.
          ****Turtle Chase****
1. After launching 'chase.launch', a
          ****GUI****
1. Clicking the button "Random" will make the turtlesim move at a random spped and direction.
2. Clicking the button "Stop" will freeze the turtlesim in the pose when the button was press.
3. Clicking the button "Forward" will make the turtlesim move in a straight line at zero degree rotation(in the direction it is facing).
4. Clicking the button "Backward" will make the turtlesim move in a straight line at 180 degree rotation(in opposite direction).
5. Clicking the button "Left" will make the turtlesim rotate anti-clockwise around the axis of its own center.
6. Clicking the button "Right" will make the turtlesim rotate clockwise around the axis of its own center.
7. Clicking the button "Left1" will make the turtlesim rotate anti-clockwise around the axis of two units from its own center.
8. Clicking the button "Right1" will make the turtlesim rotate clockwise around the axis of two units from its own center.
9. Clicking the button "Cancle/Exit" will close the gui app
