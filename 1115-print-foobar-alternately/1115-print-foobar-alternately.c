#include <semaphore.h>

typedef struct {
    int n;
    sem_t fooTurn;
    sem_t barTurn;
} FooBar;

// Function declarations. Do not change or remove this line
void printFoo();
void printBar();

FooBar* fooBarCreate(int n) {
    FooBar* obj = (FooBar*) malloc(sizeof(FooBar));
    obj->n = n;
    sem_init(&obj->fooTurn, 0, 1);
    sem_init(&obj->barTurn, 0, 0);
    return obj;
}

void foo(FooBar* obj) {
    
    for (int i = 0; i < obj->n; i++) {
        sem_wait(&obj->fooTurn);
        // printFoo() outputs "foo". Do not change or remove this line.
        printFoo();
        sem_post(&obj->barTurn);
    }
}

void bar(FooBar* obj) {
    
    for (int i = 0; i < obj->n; i++) {
        sem_wait(&obj->barTurn);
        // printBar() outputs "bar". Do not change or remove this line.
        printBar();
        sem_post(&obj->fooTurn);
    }
}

void fooBarFree(FooBar* obj) {
    sem_destroy(&obj->barTurn);
    sem_destroy(&obj->fooTurn);
    free(obj);
}