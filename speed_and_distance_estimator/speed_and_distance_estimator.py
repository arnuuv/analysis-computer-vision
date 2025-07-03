from analysis_computer_vision.utils.bbox_utils import measure_distance , get_foot_position
import cv2

class SpeedAndDistance_Estimator():
  def __init__(self):
    self.frame_window = 5
    self.frame_rate = 24
    
    
  def add_speed_and_distance_to_tracks(self,tracks):
    total_distance ={
      
    }
    for object, object_tracks in tracks.items():
      if object == 'ball' or object == 'referee':
        continue
      number_of_frames = len(object_tracks)
      for frame_num in range(0,number_of_frames, self.frame_window):
        last_frame = min(frame_num + self.frame_window, number_of_frames-1)
        
        for track_id, track_info in object_tracks[frame_num].items():
          if track_id not in object_tracks[last_frame]:
            continue
          # Check if 'position_transformed' exists in both frames
          if 'position_transformed' not in object_tracks[frame_num][track_id] or 'position_transformed' not in object_tracks[last_frame][track_id]:
            continue
          start_position = object_tracks[frame_num][track_id]['position_transformed']
          end_position = object_tracks[last_frame][track_id]['position_transformed']
          
          if start_position is None or end_position is None:
            continue
          
          distance_covered = measure_distance(start_position, end_position)
          time_elapsed = (last_frame - frame_num) / self.frame_rate
          speed_meters_per_second = distance_covered / time_elapsed
          speed_km_per_hour = speed_meters_per_second * 3.6
          
          if object not in total_distance:
            total_distance[object] = {}
            
          if track_id not in total_distance[object]:
            total_distance[object][track_id] = 0
          
          total_distance[object][track_id] += distance_covered
          
          
          for frame_num_batch in range(frame_num,last_frame):   
            if track_id not in tracks[object][frame_num_batch]:
              continue
            
            tracks[object][frame_num_batch][track_id]['speed'] = speed_km_per_hour
            tracks[object][frame_num_batch][track_id]['distance'] = total_distance[object][track_id]
              
  def draw_speed_and_distance(self,frames,tracks):
    output_frames =[] 
    for frame_num,frame in enumerate(frames):
      for object, object_tracks in tracks.items():
        if object == 'ball' or object == 'referee':
          continue
        for _,track_info in object_tracks[frame_num].items():
          if "speed" in track_info:
            speed =track_info.get('speed',None)
            distance = track_info.get('distance',None)
            if speed is None or distance is None:
              continue
            bbox = track_info['bbox']
            position = get_foot_position(bbox)
            position = list(position)
            position[1]+=40
            position = tuple(map(int, position))
            
            # Prepare text
            text_speed = f"{speed:.2f} km/h"
            text_distance = f"{distance:.2f} m"
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.5
            thickness = 2
            color_fg = (255, 255, 255)
            color_bg = (0, 0, 0)
            alpha = 0.5  # transparency

            # Calculate text sizes
            (w_speed, h_speed), _ = cv2.getTextSize(text_speed, font, font_scale, thickness)
            (w_dist, h_dist), _ = cv2.getTextSize(text_distance, font, font_scale, thickness)
            width = max(w_speed, w_dist)
            height = h_speed + h_dist + 10

            # Right-align under the player number
            x_right = position[0] + 20  # 20px to the right of center
            y_top = position[1] + 5     # 5px below the number
            rect_topleft = (x_right - width, y_top)
            rect_bottomright = (x_right, y_top + height)

            # Draw semi-transparent rectangle
            overlay = frame.copy()
            cv2.rectangle(overlay, rect_topleft, rect_bottomright, color_bg, -1)
            cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)

            # Draw text (right-aligned)
            cv2.putText(frame, text_speed, (x_right - w_speed, y_top + h_speed), font, font_scale, color_fg, thickness)
            cv2.putText(frame, text_distance, (x_right - w_dist, y_top + h_speed + h_dist + 5), font, font_scale, color_fg, thickness)
      output_frames.append(frame)
    return output_frames
  
  
  