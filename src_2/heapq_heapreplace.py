import heapq
from heapq_showtree import show_tree
from heapq_heapdata import data

heapq.heapify(data)
print 'start:'
show_tree(data)

for n in [0, 13]:
    smallest = heapq.heapreplace(data, n)
    print 'replace %2d with %2d:' % (smallest, n)
    show_tree(data)

# Output:
# <==================================================================
# start:
# 
#                  4                  
#         9                 19        
#     10       11   
# ------------------------------------
# 
# replace  4 with  0:
# 
#                  0                  
#         9                 19        
#     10       11   
# ------------------------------------
# 
# replace  0 with 13:
# 
#                  9                  
#         10                19        
#     13       11   
# ------------------------------------
# ==================================================================>
    
