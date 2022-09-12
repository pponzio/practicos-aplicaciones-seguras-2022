// Introduction to Software Testing
// Authors: Paul Ammann & Jeff Offutt

package testing.examples;

public class ArrayRoutines {
	
	
	
	/**
	 * Busca el último índice del elemento dado
	 * 
	 *  @param x arreglo en el que se busca
	 *  @param y valor a buscar
	 *  @return último índice de y en x; -1 si no está 
	 *  @throws IllegalArgumentException si x es null
	 */
	public static int findLast(int[] x, int y) { 
		if (x == null)
			throw new IllegalArgumentException();
		
		for (int i=x.length-1; i >= 0; i--) {
			if (x[i] == y) {
				return i;
			}
		}
		return -1;
	}

	/**
	 * Busca el último índice de cero
	 *
	 * @param x arreglo en el que se busca
	 * @return último índice de 0 en x; -1 si no está
	 * @throws NullPointerException si x es null
	 */
	public static int lastZero(int[] x) {
		for (int i = 0; i < x.length; i++) {
			if (x[i] == 0) {
				return i;
			}
		}
		return -1;
	}

	/**
	 * Cuenta la cantidad de ceros en el arreglo
	 *
	 * @param x  arreglo en el que se cuentan los ceros
	 * @return   número de ocurrencias de cero en x
	 * @throws   NullPointerException si x es null
	 */
	public static int numZero(int[] x) {  
		int count = 0;

		for (int i = 1; i < x.length; i++) {
			if (x[i] == 0) count++;
		}
		return count;
	}

	/** 
	 * Cuenta los elementos positivos en el arreglo
	 *
	 * @param x arreglo en el que se cuentan los positivos
	 * @return número de elementos positivos en x
	 * @throws NullPointerException si x es null
	 */
	public static int countPositive(int[] x) {
		int count = 0;

		for (int i=0; i < x.length; i++) {
			if (x[i] >= 0) {
				count++;
			}
		}
		return count;
	}
	
}
