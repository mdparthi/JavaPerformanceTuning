package com.perf;

import java.util.ArrayList;

public class MemoryLeak {
	
	static ArrayList<BadEquals>  list = new ArrayList<BadEquals>(10000);
	static long total = 0;
	
	public static void main(String[] args) {
		
		boolean val = true;
		int i=0;
		while(val) {
			System.out.println(" Enter " + i);
			BadEquals badEquals = new BadEquals(""+i);
			if(!list.contains(badEquals)) {
				list.add(badEquals);
			}
			
			total++;
			i++;
			
			if(i>10000) {
				i=0;
			}
			
		}
		
	}
}
