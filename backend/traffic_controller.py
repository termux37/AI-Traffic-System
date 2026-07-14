import traci
import time


SUMO_CONFIG = "sumo/simulation.sumocfg"


sumo_cmd = [
    "sumo-gui",
    "-c",
    SUMO_CONFIG
]


print("Starting SUMO...")
traci.start(sumo_cmd)


step = 0


while step < 500:

    traci.simulationStep()


    vehicles = traci.vehicle.getIDList()


    print("====================")
    print("Simulation Time:", step)

    print("Vehicles:", len(vehicles))


    for vehicle in vehicles:

        road = traci.vehicle.getRoadID(vehicle)
        speed = traci.vehicle.getSpeed(vehicle)
        waiting = traci.vehicle.getWaitingTime(vehicle)

        print(
            vehicle,
            "| Road:",
            road,
            "| Speed:",
            round(speed,2),
            "| Waiting:",
            waiting
        )


    step += 1

    time.sleep(0.1)


traci.close()

print("Simulation Finished")