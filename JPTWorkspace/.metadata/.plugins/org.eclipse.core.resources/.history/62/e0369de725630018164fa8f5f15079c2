package com.perf;

import java.util.ArrayList;

public class MemoryLeak {
	
	static ArrayList<BadEquals>  list = new ArrayList<BadEquals>(10000);
	static long total = 0;
	
	public static void main(String[] args) {
		
		boolean val = true;
		int i=0;
		while(val) {
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
