def entropy(a):
    _, counts=np.unique(a,return_counts=True); p=counts/counts.sum()
    return float(-np.sum(p*np.log2(p)))
