#include <pthread.h>
#include <semaphore.h>
#include <stdlib.h>

typedef struct {
    int *buf;
    int capacity, head, tail, count;
    sem_t emptySlots;       
    sem_t fullSlots;           
    pthread_mutex_t lock;     
} BoundedBlockingQueue;

BoundedBlockingQueue* boundedBlockingQueueCreate(int capacity) {
    BoundedBlockingQueue* obj = malloc(sizeof(BoundedBlockingQueue));
    obj->buf = malloc(sizeof(int) * capacity);
    obj->capacity = capacity;
    obj->head = obj->tail = obj->count = 0;
    sem_init(&obj->emptySlots, 0, capacity);
    sem_init(&obj->fullSlots, 0, 0);
    pthread_mutex_init(&obj->lock, NULL);
    return obj;
}

void boundedBlockingQueueEnqueue(BoundedBlockingQueue* obj, int element) {
    sem_wait(&obj->emptySlots);              
    pthread_mutex_lock(&obj->lock);
    obj->buf[obj->tail] = element;
    obj->tail = (obj->tail + 1) % obj->capacity;
    obj->count++;
    pthread_mutex_unlock(&obj->lock);
    sem_post(&obj->fullSlots);                 
}

int boundedBlockingQueueDequeue(BoundedBlockingQueue* obj) {
    sem_wait(&obj->fullSlots);                
    pthread_mutex_lock(&obj->lock);
    int val = obj->buf[obj->head];
    obj->head = (obj->head + 1) % obj->capacity;
    obj->count--;
    pthread_mutex_unlock(&obj->lock);
    sem_post(&obj->emptySlots);               
    return val;
}

int boundedBlockingQueueSize(BoundedBlockingQueue* obj) {
    pthread_mutex_lock(&obj->lock);
    int n = obj->count;
    pthread_mutex_unlock(&obj->lock);
    return n;
}

void boundedBlockingQueueFree(BoundedBlockingQueue* obj) {
    sem_destroy(&obj->emptySlots);
    sem_destroy(&obj->fullSlots);
    pthread_mutex_destroy(&obj->lock);
    free(obj->buf);
    free(obj);
}