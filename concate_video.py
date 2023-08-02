from moviepy.editor import VideoFileClip, clips_array, concatenate_videoclips
import os

def vertically_concatenate_videos(video_paths, output_path):
    # Load all the video clips
    video_clips = [VideoFileClip(path) for path in video_paths]

    # Make sure all videos have the same dimensions and duration
    min_duration = min(clip.duration for clip in video_clips)
    video_clips = [clip.subclip(0, min_duration) for clip in video_clips]

    # Concatenate the videos horizontally
    final_clip = clips_array([[clip] for clip in video_clips], bg_color=(0, 0, 0))

    # Save the concatenated video
    final_clip.write_videofile(output_path, codec="libx264")
    
def horizontally_concatenate_videos(video_paths, output_path):
    # Load all the video clips
    video_clips = [VideoFileClip(path) for path in video_paths]

    # Make sure all videos have the same dimensions and duration
    min_duration = min(clip.duration for clip in video_clips)
    video_clips = [clip.subclip(0, min_duration) for clip in video_clips]

    # Concatenate the videos horizontally
    final_clip = concatenate_videoclips(video_clips, method="compose")

    # Save the concatenated video
    final_clip.write_videofile(output_path, codec="libx264")

if __name__ == "__main__":
    # Input 1: List of file paths containing videos
    video_root1 = '/media/ywh/1/yanweihao/dataset/sjtu/image/train'
    video_root2 = '/media/ywh/1/yanweihao/projects/uda/BiSeNet-uda/outputs/CityScapes_SJTU_BiSeNet_20kunsup_focal_0.8_0.05/pred_train_10k/pred_color'
    video_root3 = '/media/ywh/1/yanweihao/projects/uda/BiSeNet-uda/outputs/CityScapes_SJTU_BiSeNet_20kunsup_focal_0.8_0.05_paste_mode_Single_1/pred_train_10k/pred_color'
    video_roots = [video_root1, video_root2, video_root3]
    target_sceens = ['sjtu1.mp4', 'sjtu2.mp4', 'sjtu7.mp4', 'sjtu9.mp4']
    # target_sceens = ['sjtu7.mp4', 'sjtu9.mp4']
    for target_sceen in target_sceens:
        video_paths = [os.path.join(video_root, target_sceen) for video_root in video_roots]

        # Input 2: Path to save the result video
        output_path = os.path.join(video_root3, target_sceen.replace('.mp4', '_concat.mp4')) 

        horizontally_concatenate_videos(video_paths, output_path)
