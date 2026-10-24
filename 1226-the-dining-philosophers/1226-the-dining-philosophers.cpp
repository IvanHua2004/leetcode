#include <mutex>
#include <functional>
#include <algorithm>
using namespace std;

class DiningPhilosophers {
    mutex forks[5];

public:
    DiningPhilosophers() {}

    void wantsToEat(int philosopher,
                    function<void()> pickLeftFork,
                    function<void()> pickRightFork,
                    function<void()> eat,
                    function<void()> putLeftFork,
                    function<void()> putRightFork) {
        int left  = philosopher;
        int right = (philosopher + 1) % 5;

        // Always lock the lower-numbered fork first, so there is no circular wait
        int first  = min(left, right);
        int second = max(left, right);

        lock_guard<mutex> a(forks[first]);
        lock_guard<mutex> b(forks[second]);

        pickLeftFork();
        pickRightFork();
        eat();
        putLeftFork();
        putRightFork();
    }   // lock_guards release both forks here
};