This repository contains 2 algorithms to find the top-k pairs of 2 sorted files. The files used by the algorithms are males_sorted and females_sorted

The first algorithm is called Hash Rank Join Operator (HRJN) and its details are described in page 6 here: ([https://cs.uwaterloo.ca/~ilyas/papers/rank_join2.pdf])
Execution examples:
python3 hrjn.py 10
python3 hrjn.py 30
python3 hrjn.py 100

The second algorithm is a simple top-k algorithm thats reads the 2 files as a whole and puts them into a heap.
Execution examples:
python3 simple_top-k.py 10
python3 simple_top-k.py 30
python3 simple_top-k.py 100
