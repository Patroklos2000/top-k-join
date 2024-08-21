#Patroklos Pappas 4470
import sys
import heapq
import time

start_time = time.time()

def T(Ltop, Rbottom, Lbottom, Rtop):
	f1=Ltop+Rbottom
	f2=Lbottom+Rtop
	return max(f1,f2)

def Open(file1, file2, mdict, femdict, pq):
	line1 = file1.readline()
	line1 = line1.split(',')
	while line1[8][1:8]=="Married" or int(line1[1])<18:
		line1=file1.readline()
		line1=line1.split(',')
	p1_max = float(line1[25])
	p1_cur = float(line1[25])
	mdict[int(line1[1])] = [{'id': int(line1[0]), 'weight': float(line1[25])}]

	line2 = file2.readline()
	line2 = line2.split(',')
	while line2[8][1:8]=="Married" or int(line2[1])<18:
		line2=file2.readline()
		line2=line2.split(',')
	p2_max = float(line2[25])
	p2_cur = float(line2[25])
	femdict[int(line2[1])] = [{'id': int(line2[0]), 'weight': float(line2[25])}]
	t = T(p1_max, p2_cur, p1_cur, p2_max)

	if int(line2[1]) in mdict:
		heapq.heappush(pq,(float(line1[25])*-1+float(line2[25])*-1, [int(line1[0]),int(line2[0])]))

	return file1, file2, mdict, femdict, p1_max, p1_cur, p2_max, p2_cur, pq

def hrjn(file1, file2, mdict, L2, p1_max, p1_cur, p2_max, p2_cur, pq):
	output = []
	while not output:
		line1 = file1.readline()
		line1 = line1.split(',')
		while line1[8][1:8]=="Married" or int(line1[1])<18:
			line1 = file1.readline()
			line1 = line1.split(',')
		p1_cur = float(line1[25])
		t = T(p1_max, p2_cur, p1_cur, p2_max)
		if int(line1[1]) in mdict:
			mdict[int(line1[1])].append({'id': int(line1[0]), 'weight': float(line1[25])})
		else:
			mdict[int(line1[1])] = [{'id': int(line1[0]), 'weight': float(line1[25])}]
		if int(line1[1]) in femdict:
			for i in femdict[int(line1[1])]:
				heapq.heappush(pq,(i["weight"]*-1+float(line1[25])*-1,[i["id"], int(line1[0])]))
		if len(pq)>0:
			item = heapq.heappop(pq)
			if (item[0]*-1>=t):
				output.append(item)
			else:
				heapq.heappush(pq, item)

		line2 = file2.readline()
		line2 = line2.split(',')
		while line2[8][1:8]=="Married" or int(line1[1])<18:
			line2 = file2.readline()
			line2 = line2.split(',')
		p2_cur = float(line2[25])
		t = T(p1_max, p2_cur, p1_cur, p2_max)
		if int(line2[1]) in femdict:
			femdict[int(line2[1])].append({'id': int(line2[0]), 'weight': float(line2[25])})
		else:
			femdict[int(line2[1])] = [{'id': int(line2[0]), 'weight': float(line2[25])}]
		if int(line2[1]) in mdict:
			for i in mdict[int(line2[1])]:
				heapq.heappush(pq,(i["weight"]*-1+float(line2[25])*-1,[i["id"], int(line2[0])]))
		if len(pq)>0:
			item = heapq.heappop(pq)
			if (item[0]*-1>=t):
				output.append(item)
			else:
				heapq.heappush(pq, item)
	return file1, file2, mdict, femdict, p1_max, p1_cur, p2_max, p2_cur, pq, output


file_name1 = "males_sorted"
file_name2 = "females_sorted"
file1 = open(file_name1)
file2 = open(file_name2)

K = sys.argv[1]
mdict = dict()
femdict = dict()
pq = []

file1, file2, mdict, femdict, p1_max, p1_cur, p2_max, p2_cur, pq = \
Open(file1, file2, mdict, femdict, pq)
for i in range(int(K)):
	file1, file2, mdict, femdict, p1_max, p1_cur, p2_max, p2_cur, pq, output = \
	hrjn(file1, file2, mdict, femdict, p1_max, p1_cur, p2_max, p2_cur, pq)
	print(str(i+1)+". pair: "+str(output[0][1][0])+","+str(output[0][1][1])+
		" score: "+str(output[0][0]*-1))
print("Execution time is %s seconds" % (time.time() - start_time))