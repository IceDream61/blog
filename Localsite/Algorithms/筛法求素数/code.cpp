#include <cstdio>
#include <cmath>
using namespace std;

const int maxnum = 1000;

bool d[maxnum+1];
int primes[maxnum], primeCount; // 这个上界足够了，再小不大能确定如何缩小范围

void init1() {
    for(int i=0;i<=maxnum;++i) d[i]=true;
    d[0]=d[1]=false;
    for(int i=2;i<=sqrt(maxnum);++i)
        if(d[i])
            for(int j=i+i;j<=maxnum;j+=i) d[j]=false;
}
void init2() {
    primeCount=0;
    for(int i=2;i<=maxnum;++i)
        if(d[i]) primes[primeCount++]=i;
}

void print1() {
    for(int i=0;i<=maxnum;++i)
        if(d[i]) printf("%5d", i);
    printf("\n");
}
void print2() {
    for(int i=0;i<primeCount;++i)
        printf("%5d", primes[i]);
    printf("\n");
}

int main() {
    init1();
    print1();
    init2();
    print2();
    return 0;
}
