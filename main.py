from analysis_computer_vision.utils import read_video, save_video
from analysis_computer_vision.trackers import Tracker

def main():
  #Read the video
  video_frames = read_video("analysis_computer_vision/input_videos/08fd33_4.mp4")
  #initialize tracker
  tracker = Tracker('analysis_computer_vision/models/best.pt')
  tracks = tracker.get_object_tracks(video_frames, read_from_stub=True, stub_path='analysis_computer_vision/stub/track_stubs.pkl')
  
  #Draw output
  ##Draw object tracks
  output_video_frames = tracker.draw_annotations(video_frames,tracks)
  
  #Save the video
  save_video(output_video_frames, "analysis_computer_vision/output_videos/output_video.avi")

if __name__ == "__main__":
  main()
  
#check commit