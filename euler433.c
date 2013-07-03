#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <pthread.h>
#include <unistd.h>
#include <time.h>
#include <sys/types.h>

#define ULL(x) ((unsigned long long)x)
#define N 5000000
#define N2 1000

pthread_mutex_t lock;

void sigint_handler(int sig){
  exit(0);
}

unsigned long long euclid_steps(void* xp){
  int x = *(int *)xp;
  int y,s = 0;
  unsigned long long tot = 0;
  for(y = 1; y<= N; y++){
    if(x % y == 0){
      tot+= ULL(1);
    }
    else if(x % y == 1){
      tot+= ULL(2);
    }
    else{
      s = 0;
      int ytmp = y;
      int xtmp = x;
      while(ytmp != 0){ 
        int tmp = xtmp;
        xtmp = ytmp;
        ytmp = tmp % ytmp;
        s++;
      }
      tot += ULL(s);
      s = 0;
    }
  }
  //pthread_mutex_lock(&lock);
  //sum[(*(int *)xp)] = tot;
  //pthread_mutex_unlock(&lock);
  free(xp);
  return tot;
}

unsigned long long s(int n){
  int x,y;
  pthread_t tid[n];
  int es, es2;
  for(x = 1; x <= n; x++){
    int *xp = malloc(sizeof(int));
    *xp = x;
    pthread_create(&tid[x-1], NULL, (void *)euclid_steps, (void *)xp);
  }
  int i;
  unsigned long long tot = 0;
  for(i = 0; i < n; i++){
    unsigned long long t = 0;
    if(pthread_join(tid[i], (void *)&t) != 0){
      printf("PTHREAD JOIN ERROR!");
      exit(0);
    }
    if(tot + ULL(t) < ULL(0)){
      printf("OVERFLOW!\n");
    }
    //printf("%d, %llu\n", i+1, t);
    tot += ULL(t);
  } 
  return tot;
}

int euclid(int x, int y){
  int s = 0;
  if(x % y == 0){
    return 1;
  }
  if(y % x == 0){
    return 2;
  }
  if(x==1)
    return 2;
  if(y + 1 == x)
    return 2;
  if(x + 1 == y)
    return 3;
  while(y != 0){
    int tmp = x;
    x = y;
    y = x % y;
    s++;
  }
  return s;
}

inline int sum(int* l,int n){
  int i;
  int sum = 0;
  for(i = 0; i < n; i++){
    sum += l[i];
  }
  return sum;
}

unsigned long long s2(int n){
  unsigned long long tot = ULL(0);
  int x,y;
  for(x = 1; x <= n; x++){
    int l[x];
    for(y = x+1; y<=2*x; y++){
      l[y%x] = euclid(x,y);
    }
    tot += ULL(sum(l,x))*ULL((N/x)) + ULL(sum(l,N%x+1))-ULL(l[0])-ULL((2*x-1));
  }
  return tot;
}


int main(){
  if(signal(SIGINT, sigint_handler) < 0){
    printf("SIGNAL FAILED!\n");
    exit(0);
  }
  printf("N2: %d\n", N2);
  time_t t1, t2;
  (void) time(&t1);
  unsigned long long total = s2(N2);
  (void) time(&t2);

  printf("total: %llu\n", total);
  printf("time taken: %d\n", (int)(t2 - t1));

  return 0;
}
