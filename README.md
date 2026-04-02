# Drone Attack Simulation Laboratory: Detection and Automated Interception of Hostile UAV Swarms

This project details the design, implementation, and evaluation of a Drone Attack Simulation Laboratory. The project creates a safe, cost-effective computational environment to study hostile Unmanned Aerial Vehicle (UAV) swarm behavior and test defensive countermeasures. Using an object-oriented Python architecture and Matplotlib, the simulation models multi-drone approach vectors, establishes a monitored radar zone with probabilistic signal noise, and implements heuristic interception protocols. The laboratory provides a controlled, deterministic virtual environment for analyzing detection rates, interception efficiency, and overall defense capability against asymmetric aerial threats.

## Key Features

- **Swarm Behavior Simulation**: Models up to 15 autonomous drones approaching a protected target on a 100x100 grid.
- **Distance-Based Radar Monitoring**: Implements a 40-unit range radar with Gaussian signal noise (Detection Error = 0.05).
- **Heuristic Interception Protocols**: Features an active defense system with a 20-unit defense radius and a capacity of 3 engagements per simulation tick.
- **Linear Prediction Tracking**: Implements a model that estimates future drone positions based on carrying velocity vectors (vx, vy).
- **Performance Analytics**: Generates automated plots for Detection Rate, Interception Efficiency, and Breach Count.


## System Architecture

The simulation is built using a modular, object-oriented design:

- **SwarmEngine**: The central controller that manages the simulation lifecycle.
- **Drone**: Represents individual autonomous units with kinematic properties.
- **Radar**: Handles threat detection logic and probabilistic sensor noise.
- **DefenseStrategy**: Implements interception algorithms (Active vs. Zone defense).
- **Visualization**: Manages the Matplotlib-based real-time animation.

## Mathematical Foundation

- **Detection**: Uses Euclidean distance metrics to identify threats within radar range.
- **Noise Model**: Applies a uniform probability distribution to simulate sensor signal degradation.
- **Interception Priority**: Threats are prioritized based on their proximity to the target using a heuristic sorting algorithm.

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- NumPy
- Matplotlib

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/malek-al-edresi/simulates-drone-approaching-project.git
   cd simulates-drone-approaching-project
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: Ensure numpy and matplotlib are installed manually if requirements.txt is not present)*

## Usage

To run the main simulation with the default configuration:

```bash
python main.py
```

### Configuration
Simulation parameters such as radar range, drone speed, and swarm size can be modified in `config.py`.

## Project Structure

- `main.py`: Entry point for the simulation.
- `config.py`: Global configuration and parameter definitions.
- `simulation/`: Core logic for swarm movement and environment handling.
- `detection/`: Radar and sensor implementation.
- `defense/`: Interception strategies and engagement logic.
- `visualization/`: Animation and graphing utilities.
- `photo/`: Directory for stored simulation snapshots and analytics results.
- `Doc/`: Project documentation and reports.

## Academic Context

This project is developed as part of a Senior Simulation Engineering course. It maps to the following Course Learning Outcomes:
- **CLO-1**: Technical & Management Skills (Demonstrated through modular Python development and automated reporting).
- **CLO-2**: Real-World Problem Solving (Demonstrated through probabilistic modeling of sensor noise and resource-constrained defense).
