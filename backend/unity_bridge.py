from matplotlib.pylab import rint

import traci
import json
import time
import os


# ===============================
# SUMO CONFIGURATION
# ===============================

SUMO_CONFIG = "sumo/simulation.sumocfg"
LANE_FILE = "data/lane_data.json"

# Start SUMO

traci.start(
    [
        "sumo-gui",
        "-c",
        SUMO_CONFIG,

        # slow simulation for Unity
        "--step-length",
        "0.1"
    ]
)


print("==============================")
print(" SUMO -> UNITY BRIDGE STARTED ")
print("==============================")


step = 0


# ===============================
# MAIN LOOP
# ===============================

while True:


    # Move SUMO one step

    traci.simulationStep()

    # ===============================
    # AI TRAFFIC SIGNAL CONTROLLER
    # ===============================

    # Create variables only once
    if step == 0:

        current_green = 0          # 0 = North/South, 2 = East/West
        green_timer = 0

        MIN_GREEN = 15             # seconds
        MAX_GREEN = 45             # seconds

    try:

        with open(LANE_FILE, "r") as f:
            lanes = json.load(f)

        ns = lanes["north"] + lanes["south"]
        ew = lanes["east"] + lanes["west"]

        green_timer += 0.1

        # ----------------------------------------
        # Maximum Green Time
        # ----------------------------------------

        if green_timer >= MAX_GREEN:

            if current_green == 0:

                current_green = 2

            else:

                current_green = 0

            traci.trafficlight.setPhase("J0", current_green)

            green_timer = 0

            print("Maximum Green Reached")
            print("Switching Signal")

        # ----------------------------------------
        # Minimum Green Time Passed
        # ----------------------------------------

        elif green_timer >= MIN_GREEN:

            # Priority Difference

            if current_green == 0:

                # East-West much larger?

                if ew > ns * 1.30:

                    current_green = 2

                    traci.trafficlight.setPhase("J0", 2)

                    green_timer = 0

                    print("AI -> EAST/WEST GREEN")

            else:

                # North-South much larger?

                if ns > ew * 1.30:

                    current_green = 0

                    traci.trafficlight.setPhase("J0", 0)

                    green_timer = 0

                print("AI -> NORTH/SOUTH GREEN")

    except Exception as e:

        print("AI Controller:", e)


    cars = []


    vehicle_ids = (
        traci.vehicle.getIDList()
    )


    # ===============================
    # READ VEHICLES
    # ===============================

    for vehicle in vehicle_ids:


        x, y = (
            traci.vehicle.getPosition(
                vehicle
            )
        )


        angle = (
            traci.vehicle.getAngle(
                vehicle
            )
        )


        speed = (
            traci.vehicle.getSpeed(
                vehicle
            )
        )



        cars.append(
            {

                "id": vehicle,

                "x": x,

                "y": y,

                "angle": angle,

                "speed": speed

            }
        )



    # ===============================
    # TRAFFIC LIGHT DATA
    # ===============================


    traffic_light = {}


    try:


        state = (
            traci
            .trafficlight
            .getRedYellowGreenState(
                "J0"
            )
        )


        traffic_light = {

            "id": "J0",

            "state": state

        }


    except:

        pass



    # ===============================
    # FINAL DATA PACKET
    # ===============================


    data = {

        "cars": cars,

        "traffic_light": traffic_light

    }



    # ===============================
    # SAFE JSON WRITE
    # ===============================


    try:


        with open(
            "unity/temp.json",
            "w"
        ) as file:


            json.dump(
                data,
                file,
                indent=4
            )


        os.replace(
            "unity/temp.json",
            "unity/traffic_data.json"
        )



    except PermissionError:


        print(
            "Unity reading JSON - skipped frame"
        )



    # ===============================
    # DEBUG
    # ===============================


    print(

        "STEP:",
        step,

        "| VEHICLES:",
        len(vehicle_ids)

    )


    step += 1


    # Match Unity refresh

    time.sleep(0.1)