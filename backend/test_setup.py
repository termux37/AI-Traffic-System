import traci

traci.start(["sumo-gui", "-c", "sumo/simulation.sumocfg"])

print(traci.trafficlight.getIDList())
logic = traci.trafficlight.getAllProgramLogics("J0")

print(logic)
traci.close()