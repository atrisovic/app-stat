all = ""

with open("notexist.txt") as f:
	all = f.read()


import ast

all = ast.literal_eval(all)
result = []
for a in all:
	pom1 = a.split(' ')
	pom2 = pom1[1].split('p')
	if len(pom2) == 1:
		pom2.append("")
	tuple1 = pom1[0], pom2[0], pom2[1]
	result.append(tuple1)


# patches
patches = dict()
for t in result:
	pom = t[0]+' '+t[1]
	if pom not in patches:
		patches[pom] = { t[2] }
	else:
		patches[pom].add(t[2])

import operator

sorted_patches = sorted(patches.items(), key = operator.itemgetter(0))

freq = dict()
for t in result:
	pom = t[0]+' '+t[1]
	if pom not in freq:
		freq[pom] = 1
	else:
		freq[pom] += 1

final = dict()
for f in freq:
	for p in patches:
		if p == f:
			final[p] = p + ' & '+ ' '.join(patches[p]) +' & '+ str(freq[f]) + ' \\\ \hline'

sorted_freq = sorted(freq.items(), key = operator.itemgetter(1), reverse=True)
sorted_final = sorted(final.items(), key = operator.itemgetter(0))

with open("results_notexist.txt", 'w') as f:
	for sp in sorted_patches:
		f.write(sp[0]+' '+' '.join(sp[1])+'\n')
	f.write("\n\n")
	for fr in sorted_freq:
		f.write(fr[0]+' '+str(fr[1])+'\n')
	f.write("\n\n")
	f.write("\\begin{tabular}{| l | l | l |}")
	f.write("\hline")
	for fin in sorted_final:
		f.write(fin[1]+'\n')
	f.write("\hline\n")
	f.write("\end{tabular}")
  
