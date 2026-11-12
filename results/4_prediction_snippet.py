def predict(a,kind):
    a=a.astype(np.int16); p=np.zeros_like(a)
    p[0,1:]=a[0,:-1];p[1:,0]=a[:-1,0]
    L=a[1:,:-1];T=a[:-1,1:];TL=a[:-1,:-1]
    if kind=='left': p[1:,1:]=L
    elif kind=='average': p[1:,1:]=np.rint((L+T)/2).astype(np.int16)
    else: p[1:,1:]=np.where(TL>=np.maximum(L,T),np.minimum(L,T),np.where(TL<=np.minimum(L,T),np.maximum(L,T),L+T-TL))
    return p
