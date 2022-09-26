package testing.security;

public class ComputePaymentFixed {
	
	private static final int MAX_MILLIHOURS = 100000; // 100 hours
	private static final int MAX_HOURLYCENTS = 20000; // $200/hour
	
	public static int computeWeeklyPayment(int millihours, int hourlycents) {
		if (millihours > MAX_MILLIHOURS ||
				hourlycents > MAX_HOURLYCENTS)
			throw new IllegalArgumentException();
		
		return (millihours * hourlycents + 500) / 1000; // Round to $.01
	}
	
	
}
