from moviepy.editor import *
from moviepy.editor import VideoFileClip, clips_array, vfx

def edit_video(name_file,username):
    video = VideoFileClip(name_file).subclip()
    video = video.rotate(0.3)
    video = video.fx(vfx.mirror_x)
    # Make the text. Many more options are available.
    txt_clip = ( TextClip("@"+username,fontsize=20,color='white')
                .set_position(('left','bottom'))
                .set_duration(10) )
    result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
    result.write_videofile('./VideoEdit/'+name_file,fps=90) # Many options...

edit_video('SnapTik_7078648353558433058.mp4','hoangks5')

def 