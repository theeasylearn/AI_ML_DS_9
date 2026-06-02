import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data
cricket_polar_data = {
    "position": [
        "Straight Long Off", "Long Off", "Deep Extra Cover", "Deep Cover", "Cover Point",
        "Deep Point", "Backward Point", "Deep Backward Point", "Third Man", "Gully",
        "Slips", "Wicket Keeper", "Leg Slip", "Fine Leg", "Square Leg",
        "Deep Square Leg", "Mid-Wicket", "Deep Mid-Wicket", "Long On", "Straight Long On"
    ],
    "degree": [5, 25, 50, 70, 90, 90, 110, 110, 135, 145, 165, 180, 195, 225, 270, 270, 300, 300, 335, 355],
    "distance": [70, 70, 70, 70, 25, 70, 25, 70, 70, 10, 12, 20, 12, 70, 25, 70, 25, 70, 70, 70]
}

df = pd.DataFrame(cricket_polar_data)

# Convert degrees to radians for matplotlib
theta = np.deg2rad(df['degree'])
r = df['distance']

# Create the polar plot
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': 'polar'})

# Plot the points
ax.scatter(theta, r, s=80, color='red', zorder=3)

# Add labels for each position


# Customize the plot to look like a cricket field
ax.set_theta_zero_location('N')      # North = 0° (Straight)
ax.set_theta_direction(-1)           # Clockwise (standard cricket orientation)

ax.set_rmax(75)
ax.set_rticks([20, 40, 60, 75])      # Inner circle, 30-yard, boundary
ax.set_rlabel_position(0)

ax.grid(True, alpha=0.3)
ax.set_title("Cricket Fielding Positions - Polar View", 
             pad=30, fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()