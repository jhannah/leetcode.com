package _80test

import (
	"reflect"
	"testing"
)

func Test80(t *testing.T) {
	tests := [][]int{
		{1, 1, 1, 2, 2, 3},
		{0, 0, 1, 1, 1, 1, 2, 3, 3},
	}
	results := [][]int{
		{5}, {1, 1, 2, 2, 3},
		{7}, {0, 0, 1, 1, 2, 3, 3},
	}
	for i := 0; i < len(tests); i++ {
		ret1, ret2 := removeDuplicates(tests[i])
		if ret1 != results[i*2][0] {
			t.Fatalf("case %d fails: %v\n", i, ret1)
		}
		if !reflect.DeepEqual(ret2, results[i*2+1]) {
			t.Fatalf("case %d fails: %v != %v\n", i, ret2, results[i*2+1])
		}
	}
}
