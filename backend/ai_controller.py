import json
import os

print("================================")
print(" AI Traffic Controller ")
print("================================")

LANE_FILE = "data/lane_data.json"

if not os.path.exists(LANE_FILE):
    print("lane_data.json not found!")
    exit()

with open(LANE_FILE, "r") as f:
    lane_data = json.load(f)

# --------------------------
# Waiting Bonus
# --------------------------

waiting_bonus = {
    "north": 0,
    "south": 0,
    "east": 0,
    "west": 0
}

priority = {}

print("\nLane Status\n")

for lane in lane_data:

    score = lane_data[lane] + waiting_bonus[lane]

    priority[lane] = score

    print(
        f"{lane.upper():<6}"
        f" Vehicles={lane_data[lane]}"
        f"  Bonus={waiting_bonus[lane]}"
        f"  Priority={score}"
    )

winner = max(priority, key=priority.get)

print("\n=========================")
print("GREEN SIGNAL:")
print(winner.upper())
print("=========================")