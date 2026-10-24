class DiningPhilosophers {
    mutex forks[5];
public:
    DiningPhilosophers() {
    }

    void wantsToEat(int philosopher,
                    function<void()> pickLeftFork,
                    function<void()> pickRightFork,
                    function<void()> eat,
                    function<void()> putLeftFork,
                    function<void()> putRightFork) {
		int left = philosopher;
        int right = (philosopher+1) % 5;

        int first = min(left, right);
        int second = max(left, right);

        lock_guard<mutex> a(forks[first]);
        lock_guard<mutex> b(forks[second]);
        pickLeftFork();
        pickRightFork();
        eat();
        putLeftFork();
        putRightFork();
    }
};