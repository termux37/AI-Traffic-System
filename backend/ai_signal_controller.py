import json

LANE_FILE = "data/lane_data.json"

with open(LANE_FILE, "r") as f:
    lanes = json.load(f)

ns = lanes["north"] + lanes["south"]
ew = lanes["east"] + lanes["west"]

print("--------------------")
print("North+South :", ns)
print("East+West   :", ew)
print("--------------------")

if ns >= ew:
    print("AI Decision : NORTH SOUTH GREEN")
else:
    print("AI Decision : EAST WEST GREEN")