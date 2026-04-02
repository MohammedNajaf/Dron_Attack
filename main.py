import os
import random
import numpy as np
import matplotlib.pyplot as plt
from config import Config
from simulation.swarm import SwarmEngine
from visualization.animation import create_animation
from visualization.plots import generate_performance_plots

def main():
    # Initialize reproducibility
    random.seed(42)
    np.random.seed(42)
    
    print("="*40)
    print(f"🚁 INITIALIZING: {Config.TITLE}")
    print("="*40)
    
    # Defense strategy can be 'active' or 'zone'
    engine = SwarmEngine(defense_strategy='active')
    engine.generate_scenario(Config.MAX_DRONES)
    
    print(f"[ SYSTEM ] Booted Defense Network.")
    print(f"[ SENSOR ] Radar Range: {Config.RADAR_RANGE}")
    print(f"[ WEAPON ] Defense Radius: {Config.DEFENSE_RADIUS}")
    print(f"[ INTELL ] Incoming swarm size: {Config.MAX_DRONES} Drones\n")

    print("Executing spatiotemporal simulation...")
    
    if os.environ.get('MPLBACKEND') == 'Agg':
        # Headless mode: run the simulation loop manually to collect metrics
        for _ in range(Config.FRAMES):
            engine.step()
            if engine.env.target_health <= 0:
                break
    else:
        # Interactive mode: use FuncAnimation which drives the engine.step()
        fig, ani = create_animation(engine, frames=Config.FRAMES)
        plt.show()

    # Generate Performance Analytics Plots
    generate_performance_plots(engine.metrics)

    # Calculate overall analytics
    efficiency = 0
    if engine.metrics['detected'] > 0:
        efficiency = (engine.metrics['intercepted'] / engine.metrics['detected']) * 100

    print("\n" + "="*40)
    print("📊 POST-SIMULATION CAPABILITY REPORT")
    print("="*40)
    print(f"Total Drones Invading: {engine.metrics['spawned']}")
    print(f"Total Drones Tracked:  {engine.metrics['detected']}")
    print(f"Total Neutralized:     {engine.metrics['intercepted']}")
    print(f"Total Target Breaches: {engine.metrics['reached_target']}")
    print(f"Target Final Health:   {engine.env.target_health} / {Config.TARGET_HEALTH}")
    print(f"\nSystem Efficiency Rating: {efficiency:.1f}%")
    print("="*40) 

if __name__ == "__main__":
    main()
