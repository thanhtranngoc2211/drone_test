package main

import (
    "fmt"
    "example.com/greetings"
)

func main() {
    // Get a greeting message and print it.
    message, err := greetings.Hello("Gladys")

    if err != nil {
        fmt.Println("Error:", err)
    } else {
        fmt.Println(message)
    }
}
