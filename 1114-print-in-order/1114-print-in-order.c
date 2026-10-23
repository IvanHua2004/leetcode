#include <semaphore.h>

typedef struct {
    // User defined data may be declared here.
    sem_t first_done; 
    sem_t second_done;
} Foo;

// Function Declaration, do not remove
void printFirst();
void printSecond();
void printThird();

Foo* fooCreate() {
    Foo* obj = (Foo*) malloc(sizeof(Foo));
    sem_init(&obj->first_done, 0, 0); 
    sem_init(&obj->second_done, 0, 0);
    // Initialize user defined data here.
    return obj;
}

void first(Foo* obj) {
    
    // printFirst() outputs "first". Do not change or remove this line.
    printFirst();
    sem_post(&obj->first_done); 
}

void second(Foo* obj) {
    sem_wait(&obj->first_done); 
    // printSecond() outputs "second". Do not change or remove this line.
    printSecond();
    sem_post(&obj->second_done); 
}

void third(Foo* obj) {
    sem_wait(&obj->second_done); 
    // printThird() outputs "third". Do not change or remove this line.
    printThird();
}

void fooFree(Foo* obj) {
    // User defined data may be cleaned up here.
    sem_destroy(&obj->first_done); 
    sem_destroy(&obj->second_done); 
}