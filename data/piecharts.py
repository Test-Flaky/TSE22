# -*- coding: utf-8 -*-
"""piecharts.ipynb

### Data for pie charts

|  | GO | PYTHON | JAVA | JS | Σ |
| --- | --- | --- | --- | --- | --- |
| False Positives | 42 | 85 | 52 | 90 | 269 |
| Duplicate | 2 | 5 | 3 | 13 | 23 |
| Problem Hard To Classify | 65 | 71 | 57 | 93 | 286 |
| Solution Hard To Classify | 26 | 16 | 11 | 15 | 68 |
| Ignored Test | 9 | 2 | 3 | 1 | 15 |
| Inspected | 100 | 101 | 101 | 88 | 390 |
| Not Inspected | 56 | 20 | 73 | 0 | 149 |
| Sum | 300 | 300 | 300 | 300 | 1200 |
|  |  |  |  |  | 458 |
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

#colors
colors = ['#ff9999','#cf6394','#99ff99','#ffcc99', '#ffe45e', '#ade4df', '#53b7d2']

labels = ['False Positive', 'Duplicate', 'Prob. Hard to Classify', 'Sol. Hard To Classify', 'Ignored Test', 'Inspected', 'Not Inspected']
explode = (0, 0, 0, 0, 0, 0.15, 0)

#GO
sizes = [42, 2, 65, 26, 9, 100, 56]
fig, ax = plt.subplots()
ax.pie(sizes, colors = colors, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')  
plt.tight_layout()
#ax.set_title("GO")
plt.show()

#Java
sizes = [52, 3, 57, 11, 3, 101, 73]
fig, ax = plt.subplots()
ax.pie(sizes, colors = colors, explode=explode, labels=labels, autopct='%.0f%%', shadow=True, startangle=90)
ax.axis('equal')  
plt.tight_layout()
#ax.set_title("Java")
plt.show()

#JS
sizes = [90, 13, 93, 15, 1, 88, 0]
fig, ax = plt.subplots()
ax.pie(sizes, colors = colors, explode=explode, labels=labels, autopct='%.0f%%', shadow=True, startangle=90)
ax.axis('equal')  
plt.tight_layout()
#ax.set_title("JavaScript")
plt.show()

#Python
sizes = [85, 5, 71, 16, 2, 101, 20]
fig, ax = plt.subplots()
ax.pie(sizes, colors = colors, explode=explode, labels=labels, autopct='%.0f%%', shadow=True, startangle=90)
ax.axis('equal')  
plt.tight_layout()
#ax.set_title("Python")
plt.show()

"""
Bar graph (one for each language) showing in each bar (from highest to lowest) the most prevalent causes of flakiness. **(SOLUÇÃO)**


---

| Solution | Go | Java | JavaScript | Python | Σ |
| --- | --- | --- | --- | --- | --- |
| PD - Correct Directories | 7 | 9 | 20 | 21 | 57 |
| AW - Add/modify waitFor | 13 | 16 | 13 | 5 | 47 |
| AW - Add/modify sleep | 14 | 9 | 2 | 6 | 31 |
| N - Add/modify waitFor | 9 | 6 | 8 | 4 | 27 |
| TOD - Setup/cleanup state | 4 | 6 | 6 | 9 | 25 |
| UC - Not Specific Ordering | 4 | 3 | 6 | 10 | 23 |
| TCT - Increase Timeout | 6 | 7 | 6 | 4 | 23 |
| RL - Release resource | 8 | 6 | 4 | 4 | 22 |
| C - Other | 7 | 8 | 3 | 2 | 20 |
| C - Add/modify waitFor | 6 | 5 | 3 | 3 | 17 |
| T - Avoid Time Imprecision | 1 | 4 | 2 | 7 | 14 |
| C - Protect regions | 7 | 2 | 1 | 3 | 13 |
| C - Change condition | 2 | 6 | 4 | 1 | 13 |
| FPO - Revise assertions | 0 | 4 | 1 | 7 | 12 |
| AW - Reorder execution | 2 | 1 | 3 | 5 | 11 |
| N - Add/modify Mocks | 4 | 4 | 1 | 2 | 11 |
| R - Control the Seed | 3 | 2 | 3 | 2 | 10 |
| R - No Math.Random | 1 | 2 | 1 | 1 | 5 |
| TST - Split Test Suite | 2 | 0 | 0 | 1 | 3 |
| PD - Add/modify tests | 0 | 0 | 0 | 3 | 3 |
| TOD - Remove Dependency | 0 | 0 | 0 | 1 | 1 |
| TST - Skip Non-Initialized Part | 0 | 0 | 1 | 0 | 1 |
| TRR - Calibrate assertion | 0 | 1 | 0 | 0 | 1 |
| Σ |100 | 101 | 88 | 101 | 390 |
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {'Go': [7, 13, 14, 9, 4, 4, 6, 8, 7, 6, 1, 7, 2, 0, 2, 4, 3, 1, 2, 0, 0, 0, 0],
        'Java': [9, 16, 9, 6, 6, 3, 7, 6, 8, 5, 4, 2, 6, 4, 1, 4, 2, 2, 0, 0, 0, 0, 1],
        'JavaScript': [20, 13, 2, 8, 6, 6, 6, 4, 3, 3, 2, 1, 4, 1, 3, 1, 3, 1, 0, 0, 0, 1, 0],
        'Python':[21, 5, 6, 4, 9, 10, 4, 4, 2, 3, 7, 3, 1, 7, 5, 2, 2, 1, 1, 3, 1, 0, 0],
        'Luo et al.':[0, 1, 2, 0, 3, 0, 0, 0, 5, 0, 0, 4, 6, 0, 7, 0, 0, 0, 0, 0, 6, 0, 0],
        'Moritz et al.':[12, 1, 0, 0, 0, 0, 6, 0, 13, 2, 15, 7, 5, 0, 9, 0, 0, 13, 15, 10, 3, 13, 4],
        'Fix': ['PD - Correct Directories', 'AW - Add/modify waitFor', 'AW - Add/modify sleep', 'N - Add/modify waitFor', 'TOD - Setup/cleanup state', 
                'UC - Not Specific Ordering', 'TCT - Increase Timeout', 'RL - Release resource', 'C - Other', 'C - Add/modify waitFor', 
                'T - Avoid Time Imprecision', 'C - Protect regions', 'C - Change condition', 'FPO - Revise assertions', 'AW - Reorder execution', 
                'N - Add/modify Mocks', 'R - Control the Seed', 'R - Replaced Math.Random', 'TST - Split Test Suite', 'PD - Add/modify tests', 
                'TOD - Remove Dependency', 'TST - Skip Non-Initialized Part', 'TRR - Calibrate assertion']
       }
df = pd.DataFrame(data,columns=['Fix','Go','Java','JavaScript','Python','Luo et al.'])

"""# Go"""

df.sort_values('Go',inplace=True, ascending=False)
# Plot a bar chart
df.plot(x='Fix', y='Go', color='Grey', kind="bar", xlabel=" ", fontsize = 'large')

counter = df.groupby('Go')['Luo et al.'].value_counts().unstack()

plt.savefig("GO.pdf", dpi=300, bbox_inches='tight')

df.sort_values('Go',inplace=True, ascending=False)
ax = df.plot.barh(x='Fix', y='Go', color='#ff9999')

#Mhanging name and size of label y
ax.set_ylabel(' ', fontdict={'fontsize':14})

"""# Java"""

df.sort_values('Java',inplace=True, ascending=False)
# Plot a bar chart
df.plot(x='Fix', y='Java', color='Grey', kind="bar", xlabel=" ", fontsize = 'large')

plt.savefig("JAVA.pdf", dpi=300, bbox_inches='tight')

df.sort_values('Java',inplace=True, ascending=False)
ax = df.plot.barh(x='Fix', y='Java', color='#ff9999')

ax.set_ylabel(' ', fontdict={'fontsize':14})

"""# Phyton"""

df.sort_values('Python',inplace=True, ascending=False)
# Plot a bar chart
df.plot(x='Fix', y='Python', color='Grey', kind="bar", xlabel=" ", fontsize = 'large', yticks=np.arange(0, 24, 2))

plt.savefig("PYTHON.pdf", dpi=300, bbox_inches='tight')

"""# JavaScript"""

df.sort_values('JavaScript',inplace=True, ascending=False)
# Plot a bar chart
df.plot(x='Fix', y='JavaScript', color='Grey', kind="bar", xlabel=" ", fontsize = 'large', yticks=np.arange(0, 20, 2))

plt.savefig("JAVASCRIPT.pdf", dpi=300, bbox_inches='tight')

"""Bar graph (one for each language) showing in each bar (from highest to lowest) the most prevalent causes of flakiness. **(PROBLEMA)**
_________________________________________________________________________

|  # | Problem | Go | Java | JavaScript | Python | Σ |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Async Wait | 31 | 28 | 20 | 17 | 96 |
| 2 | Concurrency | 31 | 25 | 12 | 11 | 79 |
| 3 | Platform Dependency | 8 | 9 | 21 | 30 | 68 |
| 4 | Network | 31 | 10 | 16 | 10 | 67 |
| 5 | Test Order Dependency | 5 | 6 | 7 | 10 | 28 |
| 5 | Resource Leak | 9 | 8 | 7 | 4 | 28 |
| 7 | Unordered Collections | 4 | 4 | 6 | 12 | 26 |
| 8 | Time | 4 | 6 | 3 | 10 | 23 |
| 9 | Test Case Timeout | 6 | 6 | 6 | 4 | 22 |
| 10 | Randomness | 4 | 4 | 4 | 3 | 15 |
| 11 | Floating Point Operations | 0 | 4 | 1 | 7 | 12 |
| 12 | Too Restrictive Range | 0 | 5 | 0 | 0 | 5 |
| 13 | Test Suite Timeout | 2 | 0 | 1 | 1 | 4 |
|  | Σ | 135 | 115 | 104 | 119 | 473 |
|  | Hard to classify | 65 | 57 | 93 | 71 | 286 |

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data1 = {'Go': [31, 31, 8, 31, 5, 9, 4, 4, 6, 4, 0, 0, 2],
        'Java': [28, 25, 9, 10, 6, 8, 4, 6, 6, 4, 4, 5, 0],
        'JavaScript': [20, 12, 21, 16, 7, 7, 6, 3, 6, 4, 1, 0, 1],
        'Python':[17, 11, 30, 10, 10, 4, 12, 10, 4, 3, 7, 0, 1],
        'Fix': ['Async Wait', 'Concurrency', 'Platform Dependency', 'Network', 'Test Order Dependency',  'Resource Leak', 'Unordered Collections', 'Time', 'Test Case Timeout', 'Randomness', 
                'Floating Point Operations', 'Too Restrictive Range', 'Test Suite Timeout']
       }
df1 = pd.DataFrame(data1,columns=['Fix','Go','Java','JavaScript','Python'])

"""# GO"""

df1.sort_values('Go',inplace=True, ascending=False)

# Plot a bar chart
fig = df1.plot(x='Fix', y='Go', color='Grey', kind="bar", xlabel=" ", yticks=np.arange(0, 35, 5), fontsize = 'large', width = 0.4)
plt.savefig("Go1.pdf",  dpi=300, bbox_inches='tight')

"""# JAVA"""

df1.sort_values('Java',inplace=True, ascending=False)
# Plot a bar chart
df1.plot(x='Fix', y='Java', color='Grey', kind="bar", xlabel=" ", yticks=np.arange(0, 35, 5), fontsize = 'large', width = 0.4) 

plt.savefig("Java1.pdf", dpi=300, bbox_inches='tight')

"""#Python"""

df1.sort_values('Python',inplace=True, ascending=False)
# Plot a bar chart
df1.plot(x='Fix', y='Python', color='Grey', kind="bar", xlabel=" ", yticks=np.arange(0, 35, 5), fontsize = 'large', width = 0.4)

plt.savefig("Python1.pdf", dpi=300, bbox_inches='tight')

"""# JavaScript"""

df1.sort_values('JavaScript',inplace=True, ascending=False)

# Plot a bar chart
df1.plot(x='Fix', y='JavaScript', color='Grey', kind="bar", xlabel=" ", yticks=np.arange(0, 25, 5), fontsize = 'large', width = 0.4) 
# Tamanho das fontes (xx-small, x-small, small, medium, large, x-large, xx-large)

plt.savefig("JavaScript1.pdf", dpi=300, bbox_inches='tight')
