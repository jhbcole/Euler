#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define P(n) ((unsigned long)((((unsigned long)n)*(3*((unsigned long)n)-1))/2))
#define N 100000
#define MAX(j,k) (j<k?k:j)
#define MIN(j,k) (j<k?j:k)

unsigned long isP(unsigned long n){
  unsigned long r;
  if(n*(3*n-1) > 0){
    if(2 % (n*(3*n-1)) == 0){
      r = 2/(n*(3*n-1));
      return n == (r*(3*r-1))/n;
    }
  }
  return 0;
}

int binsearch(unsigned long *arr, unsigned long n, int low, int high){
  int mid = (high - low)/2 + low;
  while(low <= high){
    if(arr[mid] < n)
      low = mid + 1;
    else if(arr[mid] == n)
      return 1;
    else
      high = mid - 1;
    mid = (high-low)/2 + low;
  }
  return 0;
}

int main(){
  int j,k;
  unsigned long ps[3*N];
  for(j = 1; j < 3*N ; j++){
    ps[j] = P(j);
  }
  printf("made array\n");
  for(j = 1; j < N; j++){
    for(k = 1; j!=k && k < N; k++){
      unsigned long sub = labs(ps[k]-ps[j]);
      unsigned long add = ps[k]+ps[j];
      if(binsearch(ps, sub, 0, MAX(j,k)) && binsearch(ps, add, MAX(j,k), 3*N)){
        printf("%lu, %lu, D = %lu\n", ps[k], ps[j], sub);
        return 0;
      }
    }
  }
  return 0;
}

