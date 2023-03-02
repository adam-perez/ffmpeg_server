'''This is a Flask blueprint for the /videos route'''
from flask import ( abort, Blueprint, render_template )
from video import ( Video )

assets_dir = "assets/"
videos_bp = Blueprint('videos', __name__, url_prefix='/videos')

@videos_bp.route('/<file>/group-of-pictures.json')
def get_i_frames(file: str) -> str:
    '''Return an HTML document containing the video's I frame data'''
    video = None
    try:
        video = Video(assets_dir + file)
    except NotImplementedError:
        return abort(415)  # Unsupported Media Type
    except FileNotFoundError:
        return abort(404)  # Not Found
    try:
        i_frames = video.get_i_frames()
        return render_template('videos/i_frames.html', i_frames=i_frames)
    except RuntimeError:
        return abort(500)  # Internal server error

@videos_bp.route('/<file>/group-of-pictures/<int:index>.mp4')
def get_group_of_pictures(file: str, index: int) -> str:
    '''Return an HTML document of the indexed group of pictures from the video'''
    video = None
    try:
        video = Video(assets_dir + file)
    except NotImplementedError:
        return abort(415)
    except FileNotFoundError:
        return abort(404)
    try:
        data_uri = video.get_group(index)
        return render_template('videos/group_of_pictures.html', data_uri=data_uri, format="mp4")
    except IndexError:
        return abort(422)  # Unprocessable Content
    except RuntimeError:
        return abort(500)

@videos_bp.route('/<file>/group-of-pictures')
def get_all_groups_of_pictures(file: str) -> str:
    '''Return an HTML document of the all the video's groups of pictures'''
    video = None
    try:
        video = Video(assets_dir + file)
    except NotImplementedError:
        return abort(415)
    except FileNotFoundError:
        return abort(404)
    try:
        data_uris = video.get_all_groups()
        return render_template('videos/groups_of_pictures.html', data_uris=data_uris, format="mp4")
    except RuntimeError:
        return abort(500)

# Potential improvements:
# * Accept files from any source, not just assets/
# * Support more than just mp4
