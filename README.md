# Satellite_task_output
# example-scripts

Script for print output for every host in a RedHat satellite job.

# What does code do

If you use the remote execution for many host and you want print for every host the job output this script is your solution :-)

# What versions does it work on

This script has been tested and works on:

* Satellite 6.2

# Prerequisites

* Python >= 2.4
* A login user to Satellite

# How to run your code

~~~
./task_output.py -u admin -n satellite.example.com -p password --id <JOB ID>cla
~~~

# Example Output

~~~
Hostname;Output
servera;RHEL 6/7 Exit status: 0
serverb;RHEL 6/7 Exit status: 0
serverc;RHEL 6/7 Exit status: 0
serverd;RHEL 6/7 Exit status: 0
~~~

# Known issues

