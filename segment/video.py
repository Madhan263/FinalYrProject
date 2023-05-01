# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 16:22:02 2023

@author: admin
"""

import os
import subprocess

# specify the path to the saved video file
video_path = 'F:/yolov7-segmentation-main/runs/predict-seg/exp25/roadd.mp4'

# play the video using the default media player on the system
if os.name == 'nt':  # for Windows
    os.startfile(video_path)
else:  # for Unix-like systems
    subprocess.call(['xdg-open', video_path])
