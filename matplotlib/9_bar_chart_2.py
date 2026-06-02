import matplotlib.pyplot as plt 
ipl_teams = [
    "Mumbai Indians", 
    "Chennai Super Kings", 
    "Kolkata Knight Riders", 
    "Rajasthan Royals", 
    "Sunrisers Hyderabad", 
    "Gujarat Titans", 
    "Royal Challengers Bengaluru", 
    "Deccan Chargers"
]

# Corresponding title wins for each team
title_wins = [5, 5, 3, 1, 1, 1, 1, 1]
# Hex codes representing the primary identity of each franchise
ipl_bar_colors = [
    "#004BA0", # Mumbai Indians (Blue)
    "#FFFF00", # Chennai Super Kings (Yellow)
    "#3A225D", # Kolkata Knight Riders (Purple)
    "#EA1B85", # Rajasthan Royals (Pink)
    "#FF822A", # Sunrisers Hyderabad (Orange)
    "#1B2133", # Gujarat Titans (Navy Blue)
    "#EC1C24", # Royal Challengers Bengaluru (Red)
    "#00B7F1"  # Deccan Chargers (Sky Blue)
]

plt.barh(ipl_teams,title_wins,height=0.5,color=ipl_bar_colors)

plt.xlabel('No of title win')
plt.ylabel('Team Name')
plt.show();
