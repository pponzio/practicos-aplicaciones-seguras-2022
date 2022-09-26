package testing.security;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.Test;

public class TestComputePaymentFixed {

	@Test
	public void test1() {
		int millihours = 1000; // 1 hours
		int hourlycents = 1;   // $0.01/hour
		int res = ComputePaymentFixed.computeWeeklyPayment(millihours, hourlycents);
		// res = 1 cent
		assertEquals(1, res);
	}
	
	@Test
	public void test2() {
		int millihours = 1500; // 1,50 hours
		int hourlycents = 1;   // $0.01/hour
		int res = ComputePaymentFixed.computeWeeklyPayment(millihours, hourlycents);
		// res = 2 cents
		assertEquals(2, res);
	}
	
	@Test
	public void test3() {
		int millihours = 10000; // 10 hours
		int hourlycents = 1000; // $10/hour
		int res = ComputePaymentFixed.computeWeeklyPayment(millihours, hourlycents);
		// res = 10000 cents
		assertEquals(10000, res);
	}
	
	@Test
	public void test4() {
		int millihours = 100000; // 100 hours
		int hourlycents = 20000; // $200/hour
		int res = ComputePaymentFixed.computeWeeklyPayment(millihours, hourlycents);
		// res = 2000000 cents
		assertEquals(2000000, res);
	}	

	@Test
	public void test5() {
		int millihours = 100000; // 100 hours
		int hourlycents = 100000; // $1000/hour
		assertThrows(IllegalArgumentException.class, 
			() -> ComputePaymentFixed.computeWeeklyPayment(millihours, hourlycents));
	}
	
	
}
