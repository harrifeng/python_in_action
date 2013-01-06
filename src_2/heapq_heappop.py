import heapq
from heapq_showtree import show_tree
from heapq_heapdata import data
print 'random :', data
heapq.heapify(data)
print 'heapified :'
show_tree(data)
print 

for i in xrange(2):
    smallest = heapq.heappop(data)
    print 'pop %3d:' % smallest
    show_tree(data)

# Output:
# <==================================================================
# random : [19, 9, 4, 10, 11]
# heapified :
# 
#                  4                  
#         9                 19        
#     10       11   
# ------------------------------------
# 
# 
# pop   4:
# 
#                  9                  
#         10                19        
#     11   
# ------------------------------------
# 
# pop   9:
# 
#                  10                 
#         11                19        
# ------------------------------------
# ==================================================================>
    
