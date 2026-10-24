#include <semaphore.h>

typedef struct {
    // User defined data may be declared here.
    sem_t hydrogen;
    sem_t oxygen;
    sem_t oxyTurn;
} H2O;

void releaseHydrogen();

void releaseOxygen();

H2O* h2oCreate() {
    H2O* obj = (H2O*) malloc(sizeof(H2O));
    
    // Initialize user defined data here.
    sem_init(&obj->hydrogen, 0, 2);
    sem_init(&obj->oxygen, 0, 0);
    sem_init(&obj->oxyTurn, 0, 1);
    return obj;
}

void hydrogen(H2O* obj) {
    sem_wait(&obj->hydrogen);
    // releaseHydrogen() outputs "H". Do not change or remove this line.
    releaseHydrogen();
    sem_post(&obj->oxygen);
}

void oxygen(H2O* obj) {
    sem_wait(&obj->oxyTurn);
    sem_wait(&obj->oxygen);
    sem_wait(&obj->oxygen);
    // releaseOxygen() outputs "O". Do not change or remove this line.
    releaseOxygen();
    sem_post(&obj->hydrogen);
    sem_post(&obj->hydrogen);
    sem_post(&obj->oxyTurn);
}

void h2oFree(H2O* obj) {
    // User defined data may be cleaned up here.
    sem_destroy(&obj->oxygen);
    sem_destroy(&obj->hydrogen);
    free(obj);
}