
class Timer {
    constructor() {
        this.start = -1;
        this.arrays = []
    }

    trigger() {
        note = Date.now();
        this.arrays.push( note - this.start );
        this.start = note
    }

    double get_total() {
        sum = 0;
        for (i in this.arrays) {
            sum += i;
        }
        return sum;
    }
    
}
