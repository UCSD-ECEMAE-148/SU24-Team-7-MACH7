import rclpy
from roboflowoak import RoboflowOak
import cv2
import time
import numpy as np
import os
from openalpr import Alpr
from argparse import ArgumentParser

# import the Node module from ROS2 Python library
from rclpy.node import Node

# Plate recognition function (from test.py)
def recognize_plate(image_path, country="us", config="/home/projects/openalpr/config/openalpr.conf.defaults", runtime_data="/home/projects/openalpr/runtime_data"):
    alpr = None
    recognized_plates = []
    try:
        alpr = Alpr(country, config, runtime_data)

        if not alpr.is_loaded():
            print("Error loading OpenALPR")
        else:
            alpr.set_top_n(7)
            alpr.set_default_region("wa")
            alpr.set_detect_region(False)
            jpeg_bytes = open(image_path, "rb").read()
            results = alpr.recognize_array(jpeg_bytes)

            i = 0
            for plate in results['results']:
                i += 1

                if plate['candidates']:
                    candidate = plate['candidates'][0]
                    recognized_plates.append(candidate['plate'])
                    prefix = "-"
                    if candidate['matches_template']:
                        prefix = "*"
                    print("   %12s" % (candidate['plate']))

    finally:
        if alpr:
            alpr.unload()
    return recognized_plates

# Main function for plate detection and recognition (from ros2_alpr.py)
def main(args=None):
    # initialize the ROS communication
    rclpy.init(args=args)

    # Print a message to the terminal and create output directory
    output_dir = "output_images"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load valid plates from a file
    with open('/home/projects/ros2_ws/src/plates.txt', 'r') as file:
        valid_plates = [line.strip() for line in file.readlines()]

    i = 0
    # Instantiating an object (rf) with the RoboflowOak module
    rf = RoboflowOak(
        model="number-plate-detection-xglm4", confidence=0.05, overlap=0.5,
        version="3", api_key="uowRFxjzrfBQKpl6ZweO", rgb=True,
        depth=True, device=None, blocking=True
    )

    # Running the model and displaying the video output with detections
    while True:
        t0 = time.time()
        result, frame, raw_frame, depth = rf.detect()
        predictions = result["predictions"]

        for prediction in predictions:
            margin = 30
            x = int(prediction.x - prediction.width / 2) - margin
            y = int(prediction.y - prediction.height / 2) - margin
            width = int(prediction.width) + (2 * margin)
            height = int(prediction.height) + (2 * margin)
            cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)
            cropped_frame = raw_frame[y:y + height, x:x + width]

            if cropped_frame.size > 0:
                image_path = os.path.join(output_dir, f"cropped_frame_{i}.png")
                cv2.imwrite(image_path, cropped_frame)
               # time.sleep(1)
                i += 1
                recognized_plates = recognize_plate(image_path)
                for plate in recognized_plates:
                    if plate in valid_plates:
                        print(f"Valid plate detected: {plate}", flush=True)
                    else:
                        print(f"Invalid plate detected: {plate}", flush=True)

        max_depth = np.amax(depth)
        cv2.imshow("frame", frame)

        # How to close the OAK inference window / stop inference: CTRL+q or CTRL+c
        if cv2.waitKey(1) == ord('q'):
            break

    # Shutdown the ROS communication
    rclpy.shutdown()

if __name__ == '__main__':
    main()

