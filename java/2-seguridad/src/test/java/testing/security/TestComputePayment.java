package testing.security;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.Test;

public class TestComputePayment {

	
	@Test
	public void test1() {
		int millihours = 1000; // 1 hours
		int hourlycents = 1; // $0.01/hour
		int res = ComputePayment.computeWeeklyPayment(millihours, hourlycents);
		// res = 1 cent
		assertEquals(1, res);
	}
	
	@Test
	public void test2() {
		int millihours = 1500; // 1,50 hours
		int hourlycents = 1; // $0.01/hour
		int res = ComputePayment.computeWeeklyPayment(millihours, hourlycents);
		// res = 2 cents
		assertEquals(2, res);
	}
	
	@Test
	public void test3() {
		int millihours = 10000; // 10 hours
		int hourlycents = 1000; // $10/hour
		int res = ComputePayment.computeWeeklyPayment(millihours, hourlycents);
		// res = 10000 cents
		assertEquals(10000, res);
	}
	
	@Test
	public void test4() {
		int millihours = 100000; // 100 hours
		int hourlycents = 20000; // $200/hour
		int res = ComputePayment.computeWeeklyPayment(millihours, hourlycents);
		// res = 2000000 cents
		assertEquals(2000000, res);
	}
	
	@Test
	public void test5() {
		int millihours = 100000; // 100 hours
		int hourlycents = 100000; // $1000/hour
		// res = 100000 * 100000 
		// res = 10000000000 / 1000 
		// res = 10000000
		int res = ComputePayment.computeWeeklyPayment(millihours, hourlycents);
		assertEquals(10000000, res);
	}
	
	
		
	@Test
	public void test6() {
		System.out.println("10000000000");
		System.out.println(100000 * 100000);
		System.out.println((100000 * 100000 + 500) / 1000);
		System.out.println(Integer.MAX_VALUE);
		int max_millihours = 100000; // 100 hours
		int max_hourlycents = 20000; // $200/hour
		System.out.println(max_millihours * max_hourlycents);
	}
	
}
