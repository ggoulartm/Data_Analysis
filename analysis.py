#/bin/python3

import matplotlib.pyplot as plt

entrada = open("bacteria.fasta").read()
saida = open("bacteria.html","w")


cont = {}

for a in ['A','T','C','G']:
	for b in ['A','T','C','G']:
		cont[a+b]=0

entrada.replace("\n","")

for par in range(len(entrada)-1):
	cont[entrada[par]+entrada[par+1]]+=1

#HTML

i = 1

for result in cont:
	transp = cont[k]/max(cont.values())
	saida.write("<div style='width:100px; border:1px solid; height:100px; float:left; background-color:rgba(0,0,0,"+str(transp)+")'>+str(k)+</div>")
	if i%4==0:
		saida.write("<div style='clear:both'></div>")
	i+=1
saida.close()




