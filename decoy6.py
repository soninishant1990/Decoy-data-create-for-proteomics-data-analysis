#!/usr/bin/python
#NKS Program for decoy file generation
#28-12-2018
#seq =input('enter fasta seq file name: ')
with open("humanprotein.fasta", 'r') as fh:
#fh = open(seq,'r')
	line =fh.readline()
	meta = ' '
	seq = ' '
	i =0
	while line:
		line = line.rstrip('\n')
		if '>' in line:
			seq = seq[::-1]
			print(seq)
			#print(seq.split('\n ', 60))
			seq =' '
			meta = line
			print(meta)
		elif '>' not in line:
			seq = seq + line
		#seq = seq[::-1]
		#print(seq)
		line = fh.readline()
	seq = seq[::-1]
	print(seq)
#file = open("output.fasta","w")
#file.write(line)
#file.close()