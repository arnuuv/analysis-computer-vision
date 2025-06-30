# Football Computer Vision Project

This project uses Ultralytics YOLO and Supervision for object detection and tracking in football (soccer) videos. It processes input videos to detect players, referees, and the ball, annotates them, and outputs both annotated videos and cropped player images.

## Features

- Detects and tracks players, referees, and the ball in football videos
- Annotates players with red ellipses and their track IDs
- Annotates referees with yellow ellipses and their track IDs
- Annotates the ball with a green triangle
- Crops and saves images of detected players
- Robust handling of file paths and Python imports

## Project Structure

```
football-cval/
  analysis_computer_vision/
    development_and_analysis/   # Jupyter notebooks for analysis
    input_videos/              # Place your input videos here
    main.py                    # Main script (run as a module)
    models/                    # Model weights (excluded from git)
    output_videos/             # Annotated videos and cropped images
    runs/                      # YOLO run outputs (excluded from git)
    stub/                      # (Describe if used)
    trackers/                  # Tracking code
    training/                  # Training scripts/configs
    utils/                     # Utility functions
    yolo_inference.py          # YOLO inference logic
    Readme.md                  # This file
```

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd football-cval
   ```
2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   (Make sure `ultralytics` and `supervision` are included in `requirements.txt`)

3. **Download YOLO model weights:**
   - Place them in `analysis_computer_vision/models/` (this folder is git-ignored)

## Running the Project

- Always run scripts as modules from the project root for correct imports and paths:
  ```bash
  python -m analysis_computer_vision.main
  ```
- Input videos should be placed in `analysis_computer_vision/input_videos/`.
- Output videos and cropped images will be saved in `analysis_computer_vision/output_videos/`.

## Using Jupyter Notebooks

- Notebooks are in `analysis_computer_vision/development_and_analysis/`.
- Set the working directory to the project root or use absolute paths like `analysis_computer_vision/output_videos/cropped_image_1.jpg` when loading files.

## Git Best Practices

- Large files (model weights, output videos, etc.) are excluded via `.gitignore`.
- To remove already-tracked large files:
  ```bash
  git rm --cached <file>
  git commit -m "Remove large file from git tracking"
  ```

## Troubleshooting

- **Import errors:**
  - Use absolute imports (e.g., `from analysis_computer_vision.utils.bbox_utils import ...`).
  - Run scripts as modules from the project root.
- **File not found errors:**
  - Double-check file paths are relative to the project root.
  - Ensure input/output directories exist.
- **Jupyter notebook issues:**
  - Check the current working directory with `import os; os.getcwd()`.
  - Use full relative paths from the project root.

## Annotation Logic

- **Players:** Red ellipse + track ID
- **Referees:** Yellow ellipse + track ID
- **Ball:** Green triangle above the ball

## Cropping & Saving Player Images

- Cropped images are saved in `output_videos/`.
- Code handles both list and dict bounding box formats, ensures indices are integers, and creates the output directory if needed.

## License

See `LICENSE` for details.

---

For further questions or issues, please open an issue or contact the maintainer.
