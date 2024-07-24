package _189test

import (
	"reflect"
	"testing"
)

func Test189(t *testing.T) {
	tests := [][]int{
		{3}, {1, 2, 3, 4, 5, 6, 7}, {5, 6, 7, 1, 2, 3, 4},
		{2}, {-1, -100, 3, 99}, {3, 99, -1, -100},
	}
	for i := 0; i < len(tests); i += 3 {
		ret := rotateArray(tests[i][0], tests[i+1])
		if !reflect.DeepEqual(ret, tests[i+2]) {
			t.Fatalf("case %d fails: %v\n", i, ret)
		}
	}
}
