# Table of Contents
1. [Introduction](#introduction)
2. [Installing dependencies](#installing-dependencies)
   1. [Windows](#windows)
   2. [Linux](#linux)
4. [Running the server](#running-the-server)
5. [Making requests](#making-requests)
   1. [Get I frames](#get-i-frames)
   2. [Get group of pictures](#get-group-of-pictures)
   3. [Get all groups of pictures](#get-all-groups-of-pictures)

## Introduction
This is a Flask-based HTTP server for processing videos that won't clog your hard drive.

You can ask it to display a video's frame data, or split it into smaller scenes. It does it all, _without_ creating any files.

## Installing dependencies
This project depends on [FFmpeg](https://ffmpeg.org/), [Python](https://www.python.org/) and [Flask](https://flask.palletsprojects.com).

#### Windows

To install FFmpeg, first [download pre-built versions of ffmpeg and ffprobe for Windows](https://ffmpeg.org/download.html).
Then, unzip them and add their location to your PATH.

To install Python and Flask, first [download the Python 3 Windows installer](https://www.python.org/downloads/).
Run it, and opt to add Python to your PATH.
Then, open a terminal and run:
```powershell
pip install flask
```

#### Linux
Open a terminal and run:
```bash
sudo apt-get install ffmpeg
sudo apt-get install python3
pip install flask
```

## Running the server
Open a terminal and run:
```
flask --app server run
```

If everything's ok, you should see:
```
* Serving Flask app 'server'
* Debug mode: off
* Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

## Making requests
Open a browser to the location the server is running on, in this case [`http://127.0.0.1:5000`](http://127.0.0.1:5000), and append any of the following URLs.

`{file}` can be replaced with any mp4 video in `./src/assets/`.

### Get I frames
__URL:__ `/videos/{file}/group-of-pictures.json`

__Example:__ [`http://127.0.0.1:5000/videos/ftl.mp4/group-of-pictures.json`](http://127.0.0.1:5000/videos/ftl.mp4/group-of-pictures.json)

__Response:__ A web page displaying the I frame data from the video.

### Get group of pictures
__URL:__ `/videos/{file}/group-of-pictures/{index}.mp4`

__Example:__ [`http://127.0.0.1:5000/videos/ftl.mp4/group-of-pictures/0.mp4`](http://127.0.0.1:5000/videos/ftl.mp4/group-of-pictures/0.mp4)

__Response:__ A web page displaying the group of pictures at the given index of the video. `{index}` refers to the list position of the I frame that starts the group.

### Get all groups of pictures
__URL:__ `/videos/{file}/group-of-pictures`.

__Example:__ [`http://127.0.0.1:5000/videos/ftl.mp4/group-of-pictures`](http://127.0.0.1:5000/videos/ftl.mp4/group-of-pictures)

__Response:__ A web page displaying all of the groups of pictures from the video.
