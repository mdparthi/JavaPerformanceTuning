package com.perf;

public class BadEquals {
	
	protected String name;

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}


	public BadEquals(String name) {
		super();
		this.name = name;
	}
	
	@Override
	public boolean equals(Object obj) {
		if(obj instanceof BadEquals) {
			if(this.name == ((BadEquals) obj).getName()) {
				System.out.println("in equals true");
				return true;
			}
		}
		return false;
	}
	
}
