#include <pthread.h>
#include <semaphore.h>
#include <stdlib.h>

typedef struct {
    sem_t hSem;            // slots for hydrogen in the current molecule (2)
    sem_t oSem;            // slots for oxygen in the current molecule (1)
    pthread_mutex_t lock;
    int count;             // atoms released so far in the current molecule
} H2O;

void releaseHydrogen();
void releaseOxygen();

H2O* h2oCreate() {
    H2O* obj = (H2O*) malloc(sizeof(H2O));
    sem_init(&obj->hSem, 0, 2);
    sem_init(&obj->oSem, 0, 1);
    pthread_mutex_init(&obj->lock, NULL);
    obj->count = 0;
    return obj;
}

// Called after each atom is released; the 3rd atom opens the next molecule.
static void atomDone(H2O* obj) {
    pthread_mutex_lock(&obj->lock);
    obj->count++;
    if (obj->count == 3) {
        obj->count = 0;
        sem_post(&obj->hSem);
        sem_post(&obj->hSem);
        sem_post(&obj->oSem);
    }
    pthread_mutex_unlock(&obj->lock);
}

void hydrogen(H2O* obj) {
    sem_wait(&obj->hSem);
    // releaseHydrogen() outputs "H". Do not change or remove this line.
    releaseHydrogen();
    atomDone(obj);
}

void oxygen(H2O* obj) {
    sem_wait(&obj->oSem);
    // releaseOxygen() outputs "O". Do not change or remove this line.
    releaseOxygen();
    atomDone(obj);
}

void h2oFree(H2O* obj) {
    sem_destroy(&obj->hSem);
    sem_destroy(&obj->oSem);
    pthread_mutex_destroy(&obj->lock);
    free(obj);
}