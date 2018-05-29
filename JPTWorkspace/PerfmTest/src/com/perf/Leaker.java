package com.perf;

public class Leaker {
    private static boolean makeMore = true;
    public static void done() {
        makeMore = false;
    }
    public static void main(String[] args) throws InterruptedException {
        // make a bunch of them until the garbage collector gets active
        while (makeMore) {
            new Leakee(0).check();
        }
        // sit back and watch the finalizers chew through memory
        while (true) {
            Thread.sleep(1000);
            System.out.println("memory=" +
                    Runtime.getRuntime().freeMemory() + " / " +
                    Runtime.getRuntime().totalMemory());
        }
    }
}