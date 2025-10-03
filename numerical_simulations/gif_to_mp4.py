#gif to mp4
import moviepy as mp
class Converter:
    def __init__(self,gif_path:str, video_path:str):
        """
        origin: file path for the gif file:
        destiny: file path for the mp4 file:
        
        """
        
        clip = mp.VideoFileClip(gif_path)
        clip.write_videofile(video_path)

