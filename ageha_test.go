package ageha_test

import (
	"fmt"
	"testing"

	"github.com/IceyWu/ageha-go"
)

func TestGreet(t *testing.T) {
	for _, name := range []string{"Lev Wu", "世界"} {
		t.Run(name, func(t *testing.T) {
			if got, want := ageha.Greet(name), "Hello, "+name+"!"; got != want {
				t.Fatalf("Greet(%q) = %q, want %q", name, got, want)
			}
		})
	}
}

func ExampleGreet() {
	fmt.Println(ageha.Greet("Lev Wu"))
	// Output: Hello, Lev Wu!
}
