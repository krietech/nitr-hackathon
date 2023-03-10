
import os
import imageio
import moviepy.editor
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
filelocation = askopenfilename()

print('Conversion in progress...')

basename = os.path.basename(filelocation)

filename = os.path.splitext(basename)[0]

video = moviepy.editor.VideoFileClip(filelocation)
audio = video.audio

aud = audio.write_audiofile(filename+".mp3")
print(aud)

print('Conversion Done Successfully!')