''''This file defines a class for handling video processing.'''
import ffmpeg
import json
import os.path
import re

class Video:
    '''The Video class extracts frame info and groups of pictures from videos.'''
    def __init__(self, file: str) -> None:
        '''
        Raises a NotImplementedError if the file type is unsupported.

        Raises a FileNotFoundError if the file can't be found.
        '''
        if re.search("^.*.mp4$", file, flags=re.IGNORECASE) is None:
            raise NotImplementedError
        if not os.path.isfile(file):
            raise FileNotFoundError
        self.file = file

    def get_i_frames(self) -> str:
        '''
        Return the video's I frames as a formatted JSON string.

        Raises a RuntimeError if the process fails.
        '''
        frames = ffmpeg.get_frames(self.file)
        i_frames = list(filter(ffmpeg.is_i_frame, frames))
        i_frames_json = json.dumps(i_frames, indent=4)
        return i_frames_json

    def get_all_groups(self) -> list[str]:
        '''
        Return all the groups of pictures as a list of data URIs.
        
        Raises a RuntimeError if the process fails.
        '''
        frames = ffmpeg.get_frames(self.file)
        i_frames = list(filter(ffmpeg.is_i_frame, frames))
        data_uris = []
        for i, curr_frame in enumerate(i_frames):
            next_frame = i_frames[i+1] if i < len(i_frames)-1 else frames[-1]
            data_uri = ffmpeg.get_group(self.file, curr_frame, next_frame)
            data_uris.append(data_uri)
        return data_uris

    def get_group(self, index: int) -> str:
        '''
        Return the group of pictures at the given index as a data URI.
        Index refers to a zero-indexed I frame that begins a group of pictures.

        Raises a RuntimeError if the process fails.
        '''
        frames = ffmpeg.get_frames(self.file)
        i_frames = list(filter(ffmpeg.is_i_frame, frames))
        if index < 0 or index >= len(i_frames):
            raise IndexError
        curr_frame = i_frames[index]
        next_frame = i_frames[index+1] if index < len(i_frames)-1 else frames[-1]
        data_uri = ffmpeg.get_group(self.file, curr_frame, next_frame)
        return data_uri

# Potential improvements:
# * Cache the groups of pictures and frames instead of processing them every time
# * Support more than just mp4
