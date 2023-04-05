import requests
from moviepy.editor import *

image_url = 'https://static.wikia.nocookie.net/terminator/images/7/7f/More-Terminator-Films-In-The-Works-Could-Arnold-Be-On-Board.jpg/revision/latest?cb=20111225220120'
sound_url = 'http://soundfxcenter.com/movies/terminator/8d82b5_Terminator_Hasta_la_Vista_Baby_Sound_Effect.mp3'
image_file = 'terminator_image.jpg'
sound_file = 'terminator_sound.mp3'

r = requests.get(image_url)
with open(image_file, 'wb') as f:
    f.write(r.content)

r = requests.get(sound_url)
with open(sound_file, 'wb') as f:
    f.write(r.content)
video_file = 'terminator_clip.mp4'

# Load the image and sound into moviepy clips
image_clip = ImageClip(image_file).set_duration(2)
sound_clip = AudioFileClip(sound_file).set_duration(2)

# Combine the image and sound clips
video_clip = CompositeVideoClip([image_clip.set_pos('center')]).set_audio(sound_clip)

# Write the video clip to a file
video_clip.write_videofile(video_file, fps=10)
