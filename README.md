# sloth-bruteforce
This is a python script that will generate possible password combinations of up to 8 characters. It will take many thousands of years to complete on a standard home computer and require permanent storage of approximately 13.6 petabytes.

Using the string ``abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=!@#$%^&*()_+`~`` this script uses nested loops to display and write to a plaintext file named `pwdlist.txt` every possible password combination in order.
Yes, this is largely useless, because it doesn't even include every special character on a standard US QWERTY keyboard. Maybe I'll update it someday. ...when it finishes running.

I have included the current iteration of pwdlist.txt, when I realized how long it was going to take and force-quit the script. It is some thirteen million lines long and over 120 MB at present. I may also update that someday.

If you have access to a botnet or a supercomputer, maybe we can make this thing happen a little sooner.

Fear not! After it is done running, the script will close itself, freeing up valuable processing power for the robot overlords that shall rule the barren waste of a planet after our demise.

This script is fully open source and distributed under the Unilicense.
If you successfully complete the operation of it, feel free to shoot me a message.
