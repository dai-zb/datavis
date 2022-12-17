import json
import os
import numpy as np

from src.datavis import from_cfg

x = np.linspace(0, 5 * np.pi, 1000)
y1 = np.sin(x)
y2 = np.sin(2 * x)

where1 = (y1 > y2).tolist()  # numpy to list
where2 = (y1 < y2).tolist()  # numpy to list

current_py = os.path.split(__file__)[1]
current_name = os.path.splitext(current_py)
cfg_name = current_name[0] + ".json"
file_name = current_name[0] + "=.png"

with open(cfg_name, "r", encoding="utf-8") as f:
    cfg = json.load(f)

if __name__ == '__main__':
    plot, _ = from_cfg(cfg, x=x, y1=y1, y2=y2, where1=where1, where2=where2)
    plot.save(file_name)
