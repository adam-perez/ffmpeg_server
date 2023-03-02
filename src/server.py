''''This is a web server that handles requests for processing videos.'''
from flask import Flask
from routes.videos import videos_bp

app = Flask(__name__)
app.register_blueprint(videos_bp)
