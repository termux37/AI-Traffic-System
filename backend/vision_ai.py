import os
import cv2
import json
import shutil
from ultralytics import YOLO

print("================================")
print(" AI Vision System Starting ")
print("================================")

# --------------------------
# Load YOLO
# --------------------------

model = YOLO("yolov8n.pt")

print("YOLO Loaded Successfully")

CAMERAS = [
    "north",
    "south",
    "east",
    "west"
]

vehicle_classes = {
    "car",
    "bus",
    "truck",
    "motorcycle"
}

os.makedirs("vision_input", exist_ok=True)
os.makedirs("detections", exist_ok=True)

lane_data = {}


def process_camera(camera_name):

    source = f"camera_feed/{camera_name}.jpg"
    destination = f"vision_input/{camera_name}.jpg"

    if not os.path.exists(source):
        print(f"{camera_name}: Image not found")
        return 0

    shutil.copy2(source, destination)

    image = cv2.imread(destination)

    if image is None:
        print(f"{camera_name}: Failed to read image")
        return 0

    results = model(
        image,
        device=0,
        verbose=False
    )

    annotated = results[0].plot()

    cv2.imwrite(
        f"detections/{camera_name}_detected.jpg",
        annotated
    )

    count = 0

    for box in results[0].boxes:

        cls = int(box.cls[0])

        name = model.names[cls]

        if name in vehicle_classes:
            count += 1

    print(f"{camera_name}: {count} vehicles")

    return count


# --------------------------
# Process all cameras
# --------------------------

for camera in CAMERAS:

    lane_data[camera] = process_camera(camera)


# --------------------------
# Save JSON
# --------------------------

with open(
    "data/lane_data.json",
    "w"
) as f:

    json.dump(
        lane_data,
        f,
        indent=4
    )

print("\nLane data saved successfully.")