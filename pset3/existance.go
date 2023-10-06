package main

import "fmt"

const testRange = 1000000

func main() {
	for a := 2; a < testRange; a++ {
	outer:
		for b := 2; b < testRange; b++ {
			if a == b {
				break
			}
			for n := 1; n < testRange*10; n++ {
				if gcd(a, n) != 1 && gcd(b, n) != 1 {
					break outer
				}
			}
			fmt.Println(a, b)
		}
	}
}

func gcd(a, b int) int {
	r := a % b
	if r == 0 {
		return b
	}
	return gcd(b, r)
}
