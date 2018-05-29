package com.perf.thread;

public class Shared {

	synchronized void method1(Shared s2){
		System.out.println("in method 1 starting");
		
		try {
			Thread.sleep(1000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		
		s2.method2(this);		
		System.out.println(" end of method 1");
	}
	
	synchronized void method2(Shared s1){
		System.out.println("in method 2 starting");
		
		try {
			Thread.sleep(1000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		
		s1.method1(this);		
		System.out.println(" end of method 2");
	}
}
