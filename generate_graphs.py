import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs('photo', exist_ok=True)

# 1. Detected Aircraft Over Time
frames = np.arange(0, 300, 10)
detected = np.clip(np.cumsum(np.random.poisson(0.5, len(frames))), 0, 15)

plt.figure(figsize=(8, 5))
plt.plot(frames, detected, marker='o', color='purple', linestyle='-', linewidth=2)
plt.title('Cumulative Drone Detections Over Time', fontsize=14, fontweight='bold')
plt.xlabel('Simulation Frame', fontsize=12)
plt.ylabel('Number of Detected Drones', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('photo/detected_over_time.png', dpi=300)
plt.close()

# 2. Interception Rate (Zone vs Active)
strategies = ['Zone Defense', 'Active Interception']
intercepted = [8, 14]
total = [15, 15]

x = np.arange(len(strategies))
width = 0.35

fig, ax = plt.subplots(figsize=(8, 5))
rects1 = ax.bar(x - width/2, total, width, label='Total Spawns', color='gray', alpha=0.7)
rects2 = ax.bar(x + width/2, intercepted, width, label='Intercepted', color='red', alpha=0.9)

ax.set_ylabel('Drone Count', fontsize=12)
ax.set_title('Impact of Defense Algorithms on Interception Rates', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(strategies, fontsize=11)
ax.legend()

plt.tight_layout()
plt.savefig('photo/interception_rate.png', dpi=300)
plt.close()

# 3. Radar Noise Distribution
noise_levels = np.random.normal(5, 1.5, 1000)
plt.figure(figsize=(8, 5))
plt.hist(noise_levels, bins=30, color='teal', alpha=0.7, edgecolor='black')
plt.title('Radar Noise Probabilistic Distribution', fontsize=14, fontweight='bold')
plt.xlabel('Noise Magnitude (Meters)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.axvline(x=5, color='red', linestyle='dashed', linewidth=2, label='Mean Noise')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('photo/radar_noise.png', dpi=300)
plt.close()

print("Mockup graphs generated successfully.")

