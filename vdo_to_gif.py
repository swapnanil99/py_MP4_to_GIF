from moviepy.editor import *

video = VideoFileClip("vdo.mp4").subclip(0, 10)  # Adjust the start and end times as needed
video.write_gif("output.gif", fps=10)  # Adjust the fps as needed