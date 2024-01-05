package greetings

import "fmt"

// Hello returns a greeting message containing the provided name.
func Hello(name string) (string, error) {
    if name == "" {
        return "", fmt.Errorf("empty name")
    }
    message := fmt.Sprintf("Hello, %s!", name)
    return message, nil
}
