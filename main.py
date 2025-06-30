from analysis_computer_vision.utils import read_video, save_video
from analysis_computer_vision.trackers import Tracker
import cv2
def main():
  #Read the video
  video_frames = read_video("analysis_computer_vision/input_videos/08fd33_4.mp4")
  

  
  
  #initialize tracker
  tracker = Tracker('analysis_computer_vision/models/best.pt')
  tracks = tracker.get_object_tracks(video_frames, read_from_stub=True, stub_path='analysis_computer_vision/stub/track_stubs.pkl')
  
  #save cropped image of a player
  for track_id, player in tracks['players'][0].items():
    bbox = player["bbox"]
    frame = video_frames[0]

    # Ensure bbox is in the correct format and indices are integers
    if isinstance(bbox, dict):
        x1, y1, x2, y2 = int(bbox['x1']), int(bbox['y1']), int(bbox['x2']), int(bbox['y2'])
    else:
        x1, y1, x2, y2 = map(int, bbox)

    # Crop bbox from frame
    cropped_image = frame[y1:y2, x1:x2]

    # Save cropped image
    cv2.imwrite(f"analysis_computer_vision/output_videos/cropped_image_{track_id}.jpg", cropped_image)
    break  
    
    
    
    
  #Draw output
  ##Draw object tracks
  output_video_frames = tracker.draw_annotations(video_frames,tracks)
  
  #Save the video
  save_video(output_video_frames, "analysis_computer_vision/output_videos/output_video.avi")

if __name__ == "__main__":
  main()
  
#check commit