#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <pthread.h>
#include <unistd.h>

#define N 5000000
#define N2 10

pthread_mutex_t lock;
unsigned long long* sum; 

void sigint_handler(int sig){
  int i;
  unsigned long long tot = 0;
  for(i = 0; i < N2; i++)
    tot += sum[i];
  printf("total %llu\n", tot);
  exit(0);
}


void* euclid_steps(void* xp){
  int x = *(int *)xp;
  //pthread_detach(pthread_self());
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
    tot += (unsigned long long)s;
  }
  printf("%lld\n", tot);
  pthread_mutex_lock(&lock);
  sum[(*(int *)xp)] = tot;
  pthread_mutex_unlock(&lock);
  free(xp);
  return NULL;
}

unsigned long long s(int n){
  int x,y;
  pthread_t tid[n];
  int es, es2;
  for(x = 1; x <= n; x++){
    int *xp = malloc(sizeof(int));
    *xp = x;
    pthread_create(&tid[x-1], NULL, euclid_steps, (void *)xp);
  }
  int i;
  for(i = 0; i < n; i++){
    if(pthread_join(tid[i], NULL) != 0){
      printf("PTHREAD JOIN ERROR!");
      exit(0);
    }
  }
  unsigned long long tot = 0;
  for(i = 0; i < n; i++){
    if(sum[i] < (unsigned long long)0){
      printf("BAD SUM: %d, %llu\n",i, sum[i]);
      exit(0);
    }
    if(tot + sum[i] < (unsigned long long)0){
      printf("OVERFLOW\n");
      exit(0);
    }
    else{
      tot += sum[i];
      printf("\t %lld \t %lld\n", sum[i], tot);
    }
  }
  return tot;
}

int main(){
  printf("%llu, %d\n",(unsigned long long)-1, sizeof(unsigned long long));

  pthread_mutex_init(&lock, NULL);

  sum = malloc(N2*sizeof(unsigned long long));

  if(signal(SIGINT, sigint_handler) < 0){
    printf("SIGNAL FAILED!\n");
    exit(0);
  }

  unsigned long long total = s(N2);
  printf("total: %lld\n", total);
  pthread_mutex_destroy(&lock);
  free(sum);
  return 0;
}
