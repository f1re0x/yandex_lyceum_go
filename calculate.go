package main

import (
	"errors"
	"fmt"
	"strconv"
	"strings"
	"unicode"
)

func Calc(expression string) (float64, error) {
	tokens := tokenize(expression)
	if len(tokens) == 0 {
		return 0, errors.New("empty expression")
	}
	return parseExpression(tokens)
}

func tokenize(expression string) []string {
	var tokens []string
	var current strings.Builder

	for _, ch := range expression {
		if unicode.IsSpace(ch) {
			continue
		}
		if unicode.IsDigit(ch) || ch == '.' {
			current.WriteRune(ch)
		} else {
			if current.Len() > 0 {
				tokens = append(tokens, current.String())
				current.Reset()
			}
			tokens = append(tokens, string(ch))
		}
	}
	if current.Len() > 0 {
		tokens = append(tokens, current.String())
	}
	return tokens
}

func parseExpression(tokens []string) (float64, error) {
	var output []float64
	var operators []string

	precedence := map[string]int{
		"+": 1,
		"-": 1,
		"*": 2,
		"/": 2,
	}

	for i := 0; i < len(tokens); i++ {
		token := tokens[i]

		switch token {
		case "+", "-", "*", "/":
			for len(operators) > 0 && precedence[operators[len(operators)-1]] >= precedence[token] {
				result, err := applyOperator(&output, operators[len(operators)-1])
				if err != nil {
					return 0, err
				}
				operators = operators[:len(operators)-1]
				output = append(output, result)
			}
			operators = append(operators, token)

		case "(":
			operators = append(operators, token)

		case ")":
			for len(operators) > 0 && operators[len(operators)-1] != "(" {
				result, err := applyOperator(&output, operators[len(operators)-1])
				if err != nil {
					return 0, err
				}
				operators = operators[:len(operators)-1]
				output = append(output, result)
			}
			if len(operators) == 0 {
				return 0, errors.New("mismatched parentheses")
			}
			operators = operators[:len(operators)-1]

		default:
			value, err := strconv.ParseFloat(token, 64)
			if err != nil {
				return 0, fmt.Errorf("invalid token: %s", token)
			}
			output = append(output, value)
		}
	}

	for len(operators) > 0 {
		result, err := applyOperator(&output, operators[len(operators)-1])
		if err != nil {
			return 0, err
		}
		operators = operators[:len(operators)-1]
		output = append(output, result)
	}

	if len(output) != 1 {
		return 0, errors.New("invalid expression")
	}
	return output[0], nil
}

func applyOperator(output *[]float64, operator string) (float64, error) {
	if len(*output) < 2 {
		return 0, errors.New("not enough values in output")
	}
	b := (*output)[len(*output)-1]
	a := (*output)[len(*output)-2]
	*output = (*output)[:len(*output)-2]

	switch operator {
	case "+":
		return a + b, nil
	case "-":
		return a - b, nil
	case "*":
		return a * b, nil
	case "/":
		if b == 0 {
			return 0, errors.New("division by zero")
		}
		return a / b, nil
	default:
		return 0, fmt.Errorf("invalid operator: %s", operator)
	}
}

func main() {
	expressions := "5 + 3* (2 - 1)"

	result, err := Calc(expressions)
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Printf("%s = %f\n", expressions, result)
	}

}
