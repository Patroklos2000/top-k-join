import sys
import heapq
import time

start_time = time.time()

file_name1 = "males_sorted"
file_name2 = "females_sorted"
file1 = open(file_name1)
file2 = open(file_name2)
line1 = file1.readline()
line2 = file2.readline()

K = sys.argv[1]
males_dict = dict()
pq = []

while line1:
	line1 = line1.split(',')
	while line1[8][1:8]=="Married" or int(line1[1])<18:
		line1=file1.readline()
		if line1:
			line1=line1.split(',')
		else:
			break
	if not line1:
		break
	if int(line1[1]) in males_dict:
		males_dict[int(line1[1])].append({'id': int(line1[0]), 'weight': float(line1[25])})
		line1 = file1.readline()
		continue
	males_dict[int(line1[1])] = [{'id': int(line1[0]), 'weight': float(line1[25])}]
	line1 = file1.readline()


while line2:
	line2 = line2.split(',')
	while line2[8][1:8]=="Married" or int(line2[1])<18:
		line2=file2.readline()
		if line2:
			line2=line2.split(',')
		else:
			break
	if not line2:
		break
	if int(line2[1]) in males_dict:
		for i in males_dict[int(line2[1])]:
			heapq.heappush(pq,(i["weight"]*-1+float(line2[25])*-1, i["id"], int(line2[0])))
	line2 = file2.readline()


for i in range(int(K)):
	item = heapq.heappop(pq)
	print(str(i+1)+". pair: "+str(item[1])+","+str(item[2])+" score: "+str(item[0]*-1))

print("Execution time is %s seconds" % (time.time() - start_time))