#https://gemini.google.com/share/73caaafb8fcb
import matplotlib.pyplot as plt 
import numpy as np 
import numpy as np
import pandas as pd
#dictionary 
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
#convert data frame
df = pd.DataFrame(cricket_polar_data)
plt.polar(df['degree'],df['distance'])
plt.tight_layout()
plt.show()
