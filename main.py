from moviepy.editor import *
from moviepy.editor import VideoFileClip, clips_array, vfx
import os
import threading

def edit_video(name_file):
    video = VideoFileClip(name_file).subclip()
    video = video.rotate(0.3)
    video = video.fx(vfx.mirror_x)
    # Make the text. Many more options are available.
    txt_clip = ( TextClip("@hoangks5",fontsize=20,color='white')
                .set_position(('left','bottom'))
                .set_duration(10) )
    result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
    result.write_videofile('./VideoEdit/'+name_file,fps=90) # Many options...



def edit_all_video():
    list_video = []
    os.chdir('./')
    list = os.listdir()
    for accs in list:
        try:
            if accs.split('.')[1] == 'mp4':
                list_video.append(accs)
        except:
            pass
    th = []
    for name_file in list_video:
        th.append(threading.Thread(target=edit_video,args={name_file,}))
    
    for ths in th:
        ths.start()
        
edit_all_video()