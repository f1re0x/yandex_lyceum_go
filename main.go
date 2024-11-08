package main

import (
	"fmt"
	"os"
)

func run() error {
	if len(os.Args) != 4 {
		return fmt.Errorf("неправильное количество аргументов")
	}

	width := os.Args[1]
	height := os.Args[2]
	fillPercent := os.Args[3]

	file, err := os.Create("config.txt")
	if err != nil {
		return err
	}
	defer file.Close()
	fmt.Sprintf("%sx%s %s%%\n", width, height, fillPercent)
	return nil
}

func main() {
	err := run()
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}
