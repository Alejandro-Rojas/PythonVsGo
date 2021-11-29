package main

import (
	"fmt"
	"math/rand"
	"time"
)

//Buuble Sort
func BubbleSort(array []int) []int {
	start_time := time.Now()
	for i := 0; i < len(array)-1; i++ {
		for j := 0; j < len(array)-i-1; j++ {
			if array[j] > array[j+1] {
				array[j], array[j+1] = array[j+1], array[j]
				end_time := time.Now()
				elapsed := end_time.Sub(start_time)
				d2 := time.Duration(elapsed)
				fmt.Println("time: ", d2)
			}

		}
	}
	return array
}

// helper to find large number in the Radix Sort
func largestNum(array2 []int) int {
	largestNum := 0

	for i := 0; i < len(array2); i++ {
		if array2[i] > largestNum {
			largestNum = array2[i]
		}
	}
	return largestNum
}

// Radix Sort
func radixSort(array2 []int) []int {
	start_time := time.Now()
	largestNum := largestNum(array2)
	size := len(array2)
	significantDigit := 1
	semiSorted := make([]int, size)
	for largestNum/significantDigit > 0 {
		bucket := [10]int{0}
		for i := 0; i < size; i++ {
			bucket[(array2[i]/significantDigit)%10]++
		}
		for i := 1; i < 10; i++ {
			bucket[i] += bucket[i-1]
		}
		for i := size - 1; i >= 0; i-- {
			bucket[(array2[i]/significantDigit)%10]--
			semiSorted[bucket[(array2[i]/significantDigit)%10]] = array2[i]
		}
		for i := 0; i < size; i++ {
			array2[i] = semiSorted[i]
		}

		significantDigit *= 10
		end_time := time.Now()
		elapsed := end_time.Sub(start_time)
		d2 := time.Duration(elapsed)
		//fmt.Println("\tSorting: "+strconv.Itoa(significantDigit)+"'s place", array2)
		fmt.Println("radixSort time: ", d2)

	}

	return array2
}

func init() {
	rand.Seed(time.Now().UnixNano())
}

func RangeInt(min int, max int, n int) []int {
	arr := make([]int, n)
	var r int
	for r = 0; r <= n-1; r++ {
		arr[r] = rand.Intn(max) + min
	}
	return arr
}

func main() {
	rand.Seed(time.Now().UnixNano())
	array := RangeInt(0, 5000, 10)
	//array := []int{54, 26, 93, 17, 77, 31, 44, 55, 20}
	rand.Shuffle(len(array), func(i, j int) { array[i], array[j] = array[j], array[i] })
	fmt.Println("bubbleSort time:", BubbleSort(array))
	println("-----------------------------------------------------------------------------------------")
	array2 := RangeInt(0, 5000, 10)
	rand.Shuffle(len(array2), func(i, j int) { array[i], array[j] = array[j], array[i] })
	fmt.Println("radixSort time seconds: ", radixSort(array2))
}
