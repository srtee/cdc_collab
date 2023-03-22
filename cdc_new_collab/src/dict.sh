echo "#ID case voltage seed" > dict.txt; python dictify.py | sort -k 2,2 -k 3,3 -k 4,4 >> dict.txt
