package main

import "testing"

func TestSum(t *testing.T) {
	tests := map[string]struct {
		a        int
		b        int
		expected int
	}{
		"simple sum": {
			a:        2,
			b:        3,
			expected: 5,
		},
		"zero sum": {
			a:        0,
			b:        0,
			expected: 0,
		},
		"negative sum": {
			a:        -2,
			b:        3,
			expected: 1,
		},
		"large numbers": {
			a:        1000,
			b:        2000,
			expected: 3000,
		},
	}

	for name, test := range tests {
		t.Run(name, func(t *testing.T) {
			actual := Sum(test.a, test.b)
			if actual != test.expected {
				t.Errorf("Sum(%d, %d) = %d, want %d", test.a, test.b, actual, test.expected)
			}
		})
	}
}
