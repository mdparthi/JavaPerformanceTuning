package com.perf;

public class FibTest {

	public static void main(String[] args) {
		FibTest fibTest = new FibTest();
		fibTest.doTest();
	}
	
	public void doTest() {
		long fib = 0;
		long then = System.currentTimeMillis();
		for(int i=0;i<60;i++){
			fib = fibImplNew(i);
			System.out.println("Fib No: " + fib);
		}
		long now = System.currentTimeMillis();
		
		System.out.println("Elapsed time : " + (now-then));
	}
	
	public long fibImpl(int n) {
		if(n==0) return 0;
		if(n==1) return 1;
		
		long retval = fibImpl(n-2) + fibImpl(n-1);
		
		return retval;					
	}
	
	public long fibImplNew(int n) {
		if(n==0) return 0;
		if(n==1) return 1;
		long n1=0, n2=1, n3=1;
		for(int i=2;i<n;++i) {
			n3=n1+n2;
			n1=n2;
			n2=n3;
		}
		return n3;
					
	}
	
}
