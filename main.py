from analysis_computer_vision.utils import read_video, save_video
from analysis_computer_vision.trackers import Tracker
import cv2
from analysis_computer_vision.team_assigner.team_assigner import TeamAssigner
from analysis_computer_vision.player_ball_assigner.player_ball_assigner import PlayerBallAssigner

def main():
  #Read the video
  video_frames = read_video("analysis_computer_vision/input_videos/08fd33_4.mp4")

  #initialize tracker
  tracker = Tracker('analysis_computer_vision/models/best.pt')
  tracks = tracker.get_object_tracks(video_frames, read_from_stub=True, stub_path='analysis_computer_vision/stub/track_stubs.pkl')

  #interpolate ball positions
  tracks['ball'] = tracker.interpolate_ball_positions(tracks['ball'])
  
  
      
  #assign player teams
  team_assigner = TeamAssigner()
  team_assigner.assign_team_color(video_frames[0],tracks['players'][0])
  
  for frame_num, player_track in enumerate(tracks['players']):
    for player_id,track in player_track.items():
      team =team_assigner.get_player_team(video_frames[frame_num],track["bbox"],player_id)
      tracks['players'][frame_num][player_id]['team'] = team
      tracks['players'][frame_num][player_id]['team color'] = team_assigner.team_colors[team]
    
    
    
  #Draw output
  ##Draw object tracks
  output_video_frames = tracker.draw_annotations(video_frames,tracks)
  
  #Save the video
  save_video(output_video_frames, "analysis_computer_vision/output_videos/output_video.avi")

if __name__ == "__main__":
  main()
  
#check commit