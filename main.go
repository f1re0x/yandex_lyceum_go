package main

import (
	"fmt"
)

func findStudentByID(id int, students map[int]string) (string, error) {
	name, found := students[id]
	if !found {
		return "", fmt.Errorf("студент с id %d не найден", id)
	}
	return name, nil
}

func main() {
	students := map[int]string{
		1: "Иванов",
		2: "Петров",
		3: "Сидоров",
	}

	id := 6
	name, err := findStudentByID(id, students)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Printf("Студент с ID %d: %s\n", id, name)
	}
}
