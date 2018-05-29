package com.perf;

class Leakee {
    public void check() {
        if (depth > 2) {
            Leaker.done();
        }
    }
    private int depth;
    public Leakee(int d) {
        depth = d;
    }
    protected void finalize() {
        new Leakee(depth + 1).check();
        new Leakee(depth + 1).check();
    }
}