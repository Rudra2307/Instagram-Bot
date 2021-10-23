# Instgram Bot

<h3 align="center">Tool for scheduling posts on sepcific interval using Facbook Creator Studio</h3>

<br /><br />
<div align="center">
Click to play on youtube

[![IMAGE ALT TEXT](http://img.youtube.com/vi/6A0drbJcC8A/0.jpg)](https://youtu.be/6A0drbJcC8A "Video Title")

</div>

<iframe width="560" height="315" src="https://www.youtube.com/embed/6A0drbJcC8A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Installation
Python 3.9.6
Selenium (version satisfing yout chrome or firefox version)
## Create File Structure
Images and videos that are not compatible to post as normal post and vidoes will be automatically
transfed to story and reels folder.
> Note: `replace your path` in required files.
- post (pics & videos to be uplodes should be kept here)
- posted 
- reels
- story
- (other files eg. insta.py, video.py)
## Run
Install the packages

```sh
pip install -r requirements.txt
```
To start program run insta.py files
```sh
python insta.py
```
## About Files
- description.py - Contains hashtags arrays and generates description
- insta.py - main/index file 
- posted.py - transfers posted pic's to folder named posted
- schedual.py - scheduling logic can be edited here <br> &emsp;&emsp;&emsp;&emsp; &emsp; -x = x + datetime.timedelta(hours=2, minutes=0) change hours and mintues (now+2hrs)
- video.py - checks if video is supporting intagrams ratio
