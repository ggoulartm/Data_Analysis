#/bin/python3

import matplotlib.pyplot as plt

entrada = open("bacteria.fasta").read()
saida = open("bacteria.html","w")


cont = {}

for a in ['A','T','C','G']:
	for b in ['A','T','C','G']:
		cont[a+b] = 0

entrada = entrada[77:]
entrada = entrada.replace("\n","")

for k in range(len(entrada)-1):
	aux=entrada[k]+entrada[k+1]
	cont[aux] += 1

#HTML

i = 1
for result in cont:
	transp = cont[result]/max(cont.values())
	saida.write("<div style='width:100px; border:1px solid; height:100px; float:left; background-color:rgba(0,0,0,"+str(transp)+")'>"+str(result)+"</div>")
	if i%4==0:
		saida.write("<div style='clear:both'></div>")
	i+=1
saida.close()




