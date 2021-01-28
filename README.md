#scheduled night / day wallpaper changer for windows
Schedule main.py script (instructions [here](https://www.jcchouinard.com/python-automation-using-task-scheduler/)) to randomly select and set if time is after dawn a wallpaper from folder night or else day.
<br>
How it works:
- request public ip address
- request latitude / longitude from ip address
- request dawn time at this lat / lng
- check current time and set wallpaper accordingly randomly selected from the day or night folder