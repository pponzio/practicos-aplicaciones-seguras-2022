package testing.security;

public class ComputePayment {
	
	public static int computeWeeklyPayment(int millihours, int hourlycents) {
		return (millihours * hourlycents + 500) / 1000; // Round to $.01
	}
	
}
