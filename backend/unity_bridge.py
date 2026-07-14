import traci
import json
import time
import os


# ===============================
# SUMO CONFIGURATION
# ===============================

SUMO_CONFIG = "sumo/simulation.sumocfg"


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