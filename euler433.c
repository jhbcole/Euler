#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <pthread.h>

#define N 5000000

int* sum; 

void sigint_handler(int sig){
  int i;
  unsigned long long tot = 0;
  for(i = 0; i < N; i++)
    tot += sum[i];
  printf("total %llu\n", tot);
  exit(0);
}


void* euclid_steps(void* xp){
  int x = *(int *)xp;
  pthread_detach(pthread_self());
  int y,s = 0,tot = 0;
  for(y = 1; y<= N; y++){
    int ytmp = y;
    int xtmp = x;
    while(ytmp != 0){
      int tmp = xtmp;
      xtmp = ytmp;
      ytmp = tmp % ytmp;
      s++;
    }
    tot += s;
  }
  sum[x] = tot;
  free(xp);
  return NULL;
}

unsigned long long s(int n){
  int x,y;
  pthread_t tid;
  int es, es2;
  for(x = 1; x <= n; x++){
    int *xp = malloc(sizeof(int));
    *xp = x;
    pthread_create(&tid, NULL, euclid_steps, (void *)xp);
  }
  int i;
  unsigned long long tot = 0;
  for(i = 0; i < N; i++)
    tot += sum[i];
  return tot;
}

int main(){
  sum = calloc(5000000,sizeof(int));
  if(signal(SIGINT, sigint_handler) < 0){
    printf("SIGNAL FAILED!\n");
    exit(0);
  }
  unsigned long long total = s(10);
  printf("total: %llu\n", total);
  return 0;
}
