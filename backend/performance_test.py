import traci
import csv


CONFIG = "sumo/simulation.sumocfg"


def count(edge):

    total = 0

    for v in traci.vehicle.getIDList():

        if traci.vehicle.getRoadID(v) == edge:
            total += 1

    return total



def run_simulation(mode):


    traci.start(
        [
        "sumo",
        "-c",
        CONFIG
        ]
    )


    total_wait = 0
    total_cars = 0


    for step in range(1000):

        traci.simulationStep()


        vehicles = traci.vehicle.getIDList()


        for car in vehicles:

            total_wait += traci.vehicle.getWaitingTime(car)

            total_cars += 1


        if mode == "AI":


            north=count("-E0")
            south=count("E2")
            east=count("-E1")
            west=count("E3")


            ns = north + south
            ew = east + west


            if ns > ew:

                traci.trafficlight.setPhase(
                    "J0",
                    0
                )

            else:

                traci.trafficlight.setPhase(
                    "J0",
                    2
                )


    traci.close()


    average_wait = (
        total_wait /
        max(total_cars,1)
    )


    return average_wait,total_cars




print("Running NORMAL traffic...")


normal_wait,normal_cars = run_simulation(
    "NORMAL"
)


print("Running AI traffic...")


ai_wait,ai_cars = run_simulation(
    "AI"
)


improvement = (

    (normal_wait-ai_wait)
    /
    normal_wait
    *
    100

)


with open(
    "data/results.csv",
    "w",
    newline=""
) as file:


    writer=csv.writer(file)


    writer.writerow(
        [
        "Mode",
        "Average Waiting",
        "Vehicle Samples"
        ]
    )


    writer.writerow(
        [
        "Normal",
        normal_wait,
        normal_cars
        ]
    )


    writer.writerow(
        [
        "AI",
        ai_wait,
        ai_cars
        ]
    )



print("========================")

print("RESULTS")

print("========================")


print(
"Normal Waiting:",
round(normal_wait,2)
)


print(
"AI Waiting:",
round(ai_wait,2)
)


print(
"Improvement:",
round(improvement,2),
"%"
)