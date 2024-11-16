import moviepy.editor
from tkinter.filedialog import *

vid= askopenfilename()
video= moviepy.editor.VideoFileClip("C:\Python_AK\Ak.mp4")

aud = video.audio
aud.write_audiofile("Akash_Demo.mp3")

print("Video Has Been Converted")