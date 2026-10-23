#include <semaphore.h>

void printNumber(int x);
typedef struct {
    int n;
    sem_t zeroTurn;
    sem_t oddTurn;
    sem_t evenTurn;
} ZeroEvenOdd;

ZeroEvenOdd* zeroEvenOddCreate(int n) {
    ZeroEvenOdd* obj = (ZeroEvenOdd*) malloc(sizeof(ZeroEvenOdd));
    obj->n = n;
    sem_init(&obj->zeroTurn, 0, 1);  // zero goes first
    sem_init(&obj->oddTurn, 0, 0);
    sem_init(&obj->evenTurn, 0, 0);
    return obj;
}

// You may call global function `void printNumber(int x)`
// to output "x", where x is an integer.

void zero(ZeroEvenOdd* obj) {
    for (int i = 1; i <= obj->n; i++) {
        sem_wait(&obj->zeroTurn);
        printNumber(0);
        if (i % 2 == 1)
            sem_post(&obj->oddTurn);   // next number is odd
        else
            sem_post(&obj->evenTurn);  // next number is even
    }
}

void even(ZeroEvenOdd* obj) {
    for (int i = 2; i <= obj->n; i += 2) {
        sem_wait(&obj->evenTurn);
        printNumber(i);
        sem_post(&obj->zeroTurn);
    }
}

void odd(ZeroEvenOdd* obj) {
    for (int i = 1; i <= obj->n; i += 2) {
        sem_wait(&obj->oddTurn);
        printNumber(i);
        sem_post(&obj->zeroTurn);
    }
}

void zeroEvenOddFree(ZeroEvenOdd* obj) {
    sem_destroy(&obj->zeroTurn);
    sem_destroy(&obj->oddTurn);
    sem_destroy(&obj->evenTurn);
    free(obj);
}