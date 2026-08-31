'''
### Real-World Example: Cricket Player Performance Clustering
**Scenario:** A cricket franchise wants to group all-rounders into distinct tactical profiles (such as aggressive lower-order hitters versus defensive anchor all-rounders) to build a balanced squad for a tournament.
#### Input Features
* **$X_1$:** Batting Strike Rate (runs scored per 100 balls faced)
* **$X_2$:** Bowling Economy Rate (runs conceded per over bowled)
---
### Dataset
| Player ID | Batting Strike Rate ($X_1$) | Bowling Economy Rate ($X_2$) |
| --- | --- | --- |
| **PL1** | 145.5 | 9.2 |
| **PL2** | 150.0 | 8.8 |
| **PL3** | 138.5 | 9.5 |
| **PL4** | 160.2 | 8.9 |
| **PL5** | 115.0 | 6.2 |
| **PL6** | 120.5 | 5.8 |
| **PL7** | 118.0 | 6.5 |
| **PL8** | 122.2 | 6.0 |
| **PL9** | 132.0 | 7.5 |
| **PL10** | 128.5 | 7.8 |
'''
#import library 
import numpy as np 
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt 

