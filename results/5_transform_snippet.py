def klt_basis(a,N):
    patches=[]
    for _ in range(2000):
        y=rng.integers(a.shape[0]-N+1);x=rng.integers(a.shape[1]-N+1)
        p=a[y:y+N,x:x+N].ravel().astype(float);patches.append(p-p.mean())
    X=np.array(patches);cov=np.cov(X,rowvar=False)
    # Restrict covariance to the subspace orthogonal to the DC vector.
    dc=np.ones(N*N)/N
    Q=np.linalg.qr(np.column_stack([dc,np.eye(N*N)]),mode='reduced')[0][:,1:]
    vals,V=np.linalg.eigh(Q.T@cov@Q);order=np.argsort(vals)[::-1]
    basis=np.column_stack([dc,Q@V[:,order]])
    assert np.allclose(basis.T@basis,np.eye(N*N),atol=1e-9)
    return basis,vals[order]
