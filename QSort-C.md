# Algorithm: QSort
# Language: C

``` c
void QSort(int[] A, int l, int r) {
	if(l>r) return;
	int x=A[(l+r)>>1], i=l, j=r;
	while(1) {
		while(A[i]<x) ++i;
		while(A[j]>x) --j;
		if(i>j) break;
		int t=A[i]; A[i]=A[j]; A[j]=t;
		++i; --j;
	}
	QSort(A,l,j); QSort(A,i,r);
}
```