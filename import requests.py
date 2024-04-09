import os
import requests
from moviepy.editor import *

class TerminatorClipCreator:
    def __init__(self, image_url, sound_url, output_file):
        self.image_url = image_url
        self.sound_url = sound_url
        self.output_file = output_file
        self.temp_dir = 'temp_files'
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)

    def download_file(self, url, filename):
        response = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(response.content)

    def create_clip(self):
        image_file = os.path.join(self.temp_dir, 'terminator_image.jpg')
        sound_file = os.path.join(self.temp_dir, 'terminator_sound.mp3')

        self.download_file(self.image_url, image_file)
        self.download_file(self.sound_url, sound_file)

        image_clip = ImageClip(image_file).set_duration(2)
        sound_clip = AudioFileClip(sound_file).set_duration(2)

        video_clip = CompositeVideoClip([image_clip.set_position('center')]).set_audio(sound_clip)

        video_clip.write_videofile(self.output_file, fps=10, codec='libx264', audio_codec='aac')

if __name__ == "__main__":
    image_url = 'https://static.wikia.nocookie.net/terminator/images/7/7f/More-Terminator-Films-In-The-Works-Could-Arnold-Be-On-Board.jpg/revision/latest?cb=20111225220120'
    sound_url = 'http://soundfxcenter.com/movies/terminator/8d82b5_Terminator_Hasta_la_Vista_Baby_Sound_Effect.mp3'
    output_file = 'terminator_clip.mp4'

    creator = TerminatorClipCreator(image_url, sound_url, output_file)
    creator.create_clip()
