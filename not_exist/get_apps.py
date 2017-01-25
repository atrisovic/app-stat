from lbproductions.models import Production
from projects.models import Project
from datetime import datetime

import re
import json

with open('simulation.txt') as f:
    data = json.load(f)

pattern = r"(DaVinci-\S{2,10}|Brunel-\S{2,10}|LHCb-\S{2,10}|Gauss-\S{2,10}|Moore-\S{2,10}|Boole-\S{2,10})<br/?>"
myre = re.compile(pattern)

notexist = []
for d in data:
    s = d["ProDetail"]
    apps = myre.findall(str(s))
    apps_str = ' '.join(apps)
    
    for app in apps:
        name = app.split('-')
        try:
            p = Project.nodes.get(name=name[0].upper(), version=name[1])
        except Project.DoesNotExist:
	    notexist.append(name[0] + ' ' + name[1])

with open('notexist.txt', 'w') as f:
	f.write(str(notexist))
  
