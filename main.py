from utils import read_video, save_video
from trackers import Tracker

def main():
  #Read the video
  video_frames = read_video("input_videos/08fd33_4.mp4")
  #initialize tracker
  tracker = Tracker('models/best.pt')
  tracks = tracker.get_object_tracks(video_frames, read_from_stub=True, stub_path='stub/track_stubs.pkl')
  
  
  #Save the video
  save_video(video_frames, "output_videos/output_video.avi")


if __name__ == "__main__":
  main()