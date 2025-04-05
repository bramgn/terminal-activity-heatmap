import os
from datetime import datetime
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import calplot

# Set a nicer default font
plt.rcParams['font.family'] = 'DejaVu Sans'

# Load and parse shell history
history_file = "~/.bash_history"
dates = []

with open(os.path.expanduser(history_file), 'r') as f:
    lines = f.readlines()

current_date = None
for line in lines:
    line = line.strip()
    if line.startswith("#"):
        try:
            timestamp = int(line[1:])
            current_date = datetime.fromtimestamp(timestamp).date()
        except:
            continue
    elif current_date:
        dates.append(current_date)

# Count occurrences per date
date_counts = Counter(dates)
date_series = pd.Series(date_counts)
date_series.index = pd.to_datetime(date_series.index)

# Create the calendar heatmap
fig, ax = calplot.calplot(
    date_series,
    cmap="YlGn",
    suptitle="Terminal Activity Calendar Heatmap",
    colorbar=True,
    fillcolor="lightgray"
)

# Save to file
output_path = os.path.expanduser("heatmap.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"✅ Saved heatmap to: {output_path}")
