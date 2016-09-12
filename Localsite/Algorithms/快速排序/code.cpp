#include <cstdio>
using namespace std;

int mid(int a, int b, int c) {
    // version 3
    bool tab=a<b, tac=a<c, tbc=b<c;
    return (tab^tac)?a:((tac^tbc)?c:b);

    // version 2
    // bool tab=a<b, tac=a<c, tbc=b<c;
    // if(!tab && !tac && !tbc) return b;
    // if(!tab && !tac && tbc) return c;
    // if(!tab && tac && tbc) return a;
    // if(tab && !tac && !tbc) return a;
    // if(tab && tac && !tbc) return c;
    // if(tab && tac && tbc) return b;
    // return b; // 剩余两种情况是不可能的，但有相等数的情况我没细考虑，因此随便返回一个

    // version 1
    // if(a<b && b<c || a>b && b>c) return b;
    // if(a<c && c<b || a>c && c>b) return c;
    // return a;
}

void swap(int &x, int &y) {
    // version 3
    if(&x==&y) return;
    x^=y^=x^=y;

    // version 2
    // if(&x==&y) return;
    // x^=y;
    // y^=x;
    // x^=y;

    // version 1
    // int t=x; x=y; y=t;
}

void qsort(int a[], int l, int r) {
    if(l>=r) return;
    for(int i=l,j=r,x=mid(a[l],a[r],a[(l+r)>>1]);;swap(a[l++],a[r--])) {
        while(a[l]<x) ++l;
        while(a[r]>x) --r;
        if(l>r) { qsort(a,l,j); qsort(a,i,r); return; }
    }
}

int main() {
    int a[10]={3,7,1,4,6,9,2,5,8,6};
    for(int i=0;i<10;++i) printf("%d ",a[i]); printf("\n");
    qsort(a,0,9);
    for(int i=0;i<10;++i) printf("%d ",a[i]); printf("\n");
    return 0;
}
