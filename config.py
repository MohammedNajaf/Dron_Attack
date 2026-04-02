import numpy as np

class Config:
    TITLE = "Drone Attack Simulation Laboratory: Detection and Automated Interception of Hostile UAV Swarms"
    DESCRIPTION = (
        "This project details the design, implementation, and evaluation of a Drone Attack Simulation Laboratory. "
        "The project creates a safe, cost-effective computational environment to study hostile Unmanned Aerial Vehicle (UAV) swarm behavior and test defensive countermeasures. "
        "Using an object-oriented Python architecture and Matplotlib, the simulation models multi-drone approach vectors, establishes a monitored radar zone with probabilistic signal noise, and implements heuristic interception protocols. "
        "The laboratory provides a controlled, deterministic virtual environment for analyzing detection rates, interception efficiency, and overall defense capability against asymmetric aerial threats."
    )

    # Standardized System Parameters
    GRID_SIZE = (100, 100)
    TARGET_POSITION = np.array([50.0, 50.0])
    RADAR_RANGE = 40.0
    DEFENSE_RADIUS = 20.0
    DETECTION_ERROR = 0.05
    MAX_INTERCEPTIONS_PER_TICK = 3
    TARGET_RADIUS = 5.0
    TARGET_HEALTH = 100
    FRAMES = 300
    INTERVAL = 50
    DRONE_SPEED_BASE = 0.5
    MAX_DRONES = 15

