package testing.examples;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.Test;


public class TestFindLast {

	@Test
	void findLastTest1() {
		int [] arr = {1, 2, 3, 4};
		int y = 4;
		int res = ArrayRoutines.findLast(arr, y);
		assertEquals(3, res);
	}
	
	@Test
	void findLastTest5() {
		int [] arr = null;
		int y = 1;
		assertThrows(IllegalArgumentException.class,
				() -> ArrayRoutines.findLast(arr, y));
	}
	
	@Test
	void findLastTest2() {
		int [] arr = {1, 2, 3, 4};
		int y = 5;
		int res = ArrayRoutines.findLast(arr, y);
		assertEquals(-1, res);
	}
	
	
	@Test
	void findLastTest4() {
		int [] arr = {1, 2, 3};
		int y = 1;
		int res = ArrayRoutines.findLast(arr, y);
		assertEquals(0, res);
	}


	
	
}
