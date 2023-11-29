from moviepy.editor import *
from os import path

current_directory = os.path.dirname(os.path.realpath(__file__))

def makeRuningLine(text, size=(100, 100), duration=3, textColor='white', backgroundColor=[0, 0, 0]):
    

    textVideo = TextClip(text, color=textColor, fontsize=size[0] / 10,).set_duration(duration)
    textSize = textVideo.size
    textVideo = textVideo.set_position(lambda t: (size[0] - t * (size[0] + textSize[0]) / duration, (size[1] / 2) - (textSize[1] / 2)))
    backgroundVideo = ColorClip(size=size, color=backgroundColor, duration=duration)
    runingLine = CompositeVideoClip([backgroundVideo, textVideo])
    return runingLine

def saveVideo(video, path=current_directory, fps=60):
    video.write_videofile('{}\\Runing line.mp4'.format(path), fps)


if __name__ == '__main__':
    text = input('Введите текст:\n')
    video = makeRuningLine(text)
    saveVideo(video)

