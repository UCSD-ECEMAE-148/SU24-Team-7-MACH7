<div id="top"></div>
<h1 align="center">Autonomous Ticketing Agent</h1>
<br />
<div align="center">
  <a href="https://jacobsschool.ucsd.edu/">
    <img src="images\UCSD-JSOE-LOGO.png" alt="Logo" width="432" height="108">
  </a>

## 

<h3>Team 7 aka MACH7</h3>
<h3>MAE 148 Final Project SU24</h3>
<p>
</p>
<img src="images\CAR.jpg?" width="605" height="501">
</div>

## Table of Contents
  <ol>
    <li><a href="#team-members">Team Members</a></li>
    <li><a href="#abstract">Abstract</a></li>
    <li><a href="#what-we-promised">What We Promised</a></li>
    <li><a href="#accomplishments">Accomplishments</a></li>
    <li><a href="#demonstration">Demonstration</a></li>
    <li><a href="#challenges">Challenges</a></li>
    <li><a href="#robot-design">Robot Design</a></li>
    <li><a href="#electrical-diagram">Electrical Diagram</a></li>
    <li><a href="#references">References</a></li>
    <li><a href="#contacts">Contacts</a></li>
  </ol>
  
## Team Members

<ul>
  <li>Aryan Palaskar - Computer Science</li>
  <li>A.J Olivares - Cognitive Science: Machine Learning</li>
  <li>Edward Lee - Mechanical Engineering</li>
</ul>

## Abstract
The goal of our final project was to...

## What We Promised
### Must Have:
* A working license plate detection model for the camera that can store the individual letters/numbers.
* A script that compares the license plate numbers with a list of valid permits.

### Nice to Have:
* An automated route for the robot to follow using the GPS.
* An obstacle avoidance model using the LiDAR.

## Accomplishments
* We utilized the OAKD camera through the use of a license plate recognition CV model that was developed and posted on Roboflow.
  * We were able to detect the individual numbers/letters on the license plates and store them with about a 90% accuracy.
* We also created a script that compares the license plates with a database of license plates that have proper permits. 
  * It can then alert the user if the license plate does not match or if it’s valid.
* We also created a quick GPS route that can work alongside the license plate detection system.
  * However we didn't have enough time to implement it into ROS2, so we had to run it on DonkeyCar.

## Demonstration
https://github.com/user-attachments/assets/48569c6a-5c45-45ba-9fe2-cc5fc6ea7f71
<p>
</p>

https://github.com/user-attachments/assets/7f2d49a2-581b-4cc4-94c3-61d6a153aa0f

## Challenges
* There were issues on how to get the license plate recognition model and the license plate comparison script onto ROS2.
  * The solution was to just create a ROS2 node that launches alongside the other ROS2 nodes, allowing us to just import our license plates script directly onto ROS2.
* There were also issues on getting the GPS to stay on its path accurately.
  * We were previously inside of the EBU2 courtyard, so the solution was to go away from any buildings in order to prevent the GPS signals from bouncing off the walls. 
 
## Robot Design
<div align="center">
<img src="images\car-cad.png?" width="851" height="386">
</div>

## Electrical Diagram
<div align="center">
<img src="images\electrical-diagram.png?" width="581" height="365">
</div>
 
## References
* [Open ALPR](https://github.com/openalpr/openalpr)
* [Roboflow License Plate Vision Model](https://universe.roboflow.com/sezgin-koc-3z1r3/license-plates-kwudy)

## Contacts
* Aryan Palaskar - apalaskar@ucsd.edu
* A.J Olivares - aaolivares@ucsd.edu
* Edward Lee - edl003@ucsd.edu

