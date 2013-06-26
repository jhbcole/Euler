#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

long long sum = 0;
long long s2 = 0;


void sigint_handler(int sig){
  printf("s2 %llu, sum %llu\n", s2, sum);
  exit(0);
}


int euclid_steps(int x, int y, int s){
  if(y == 0)
    return s;
  else
    return euclid_steps(y, x % y, s+1);
}

s(int n){
  int x,y;
  for(x = 1; x <= n; x++){
    for(y = 1; y <= n; y++){
      int es = euclid_steps(x,y,0);
      if(sum + es < 0){
        s2++;
        sum = 0;
      }
      else
        sum += es;
    }
    printf("%d\n",x);
  }
}

int main(){
  if(signal(SIGINT, sigint_handler) < 0){
    printf("SIGNAL FAILED!\n");
    exit(0);
  }
  s(5000000);
  printf("S2: %llu, SUM: %llu\n", s2, sum);
  return 0;
}
