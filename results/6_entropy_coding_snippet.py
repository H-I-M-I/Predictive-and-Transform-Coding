def huffman(counts):
    heap=[(int(c),i,i) for i,c in enumerate(counts) if c];heapq.heapify(heap);serial=len(counts)
    while len(heap)>1:
        ca,_,a=heapq.heappop(heap);cb,_,b=heapq.heappop(heap)
        heapq.heappush(heap,(ca+cb,serial,(a,b)));serial+=1
    codes={}
    def walk(node,s):
        if isinstance(node,int):codes[node]=s or '0'
        else:walk(node[0],s+'0');walk(node[1],s+'1')
    walk(heap[0][2],'');return codes
