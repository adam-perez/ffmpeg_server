''''
This file contains functions for processing videos with ffmpeg and ffprobe
'''
import binascii
import json
import subprocess

def get_frames(file: str) -> list[dict[str, str]]:
    '''
    Return a list of frames objects from the video using ffprobe.

    Raises a `RuntimeError` if the process fails.
    '''
    try:
        result = subprocess.run(["ffprobe",
                                 "-i", file,
                                 "-print_format", "json", "-show_frames"],
                                 stdout=subprocess.PIPE,
                                 check=True)

        return json.loads(result.stdout.decode("utf-8"))["frames"]
    except subprocess.CalledProcessError as err:
        raise RuntimeError from err

def get_group(file: str, start_frame: dict[str, str], end_frame: dict[str, str]) -> str:
    '''
    Return a base64 encoded data URI string to be the source of an HTML5 video.

    Raises a `RuntimeError` if the process fails.
    '''
    try:
        start_time = start_frame["pts_time"]
        end_time = end_frame["pts_time"]
        duration = str(float(end_time) - float(start_time))
        result = subprocess.run(["ffmpeg",
                                 "-ss", start_time, "-t", duration, "-i", file,
                                 "-movflags", "frag_keyframe+empty_moov", "-f", "mp4", "pipe:1"],
                                 stdout=subprocess.PIPE,
                                 check=True)

        return binascii.b2a_base64(result.stdout).decode("ascii")
    except subprocess.CalledProcessError as err:
        raise RuntimeError from err

def is_i_frame(frame: dict[str, str]) -> bool:
    '''Return whether or not the object is an I frame'''
    return "pict_type" in frame and frame["pict_type"] == "I"

# Potential improvements:
# * Define frame data type and update function signatures to match
# * Support more than just mp4
