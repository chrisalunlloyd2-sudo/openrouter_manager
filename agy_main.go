package main

import (
	"bufio"
	"bytes"
	"encoding/json"
	"flag"
	"fmt"
	"io"
	"net/http"
	"os"
	"strings"
	"time"
)

const baseURL = "http://localhost:8080/v1"

type Message struct {
	Role    string `json:"role"`
	Content string `json:"content"`
}

type ChatCompletionRequest struct {
	Messages    []Message `json:"messages"`
	MaxTokens   int       `json:"max_tokens"`
	Temperature float64   `json:"temperature"`
}

type ChatCompletionResponse struct {
	Choices []struct {
		Message Message `json:"message"`
	} `json:"choices"`
}

func logInteraction(prompt, response string) {
	logLine := fmt.Sprintf("{\"timestamp\": \"%s\", \"ask\": \"%s\", \"response\": \"%s\"}\n", time.Now().Format(time.RFC3339), strings.ReplaceAll(prompt, "\"", "\\\""), strings.ReplaceAll(response, "\"", "\\\""))
	f, err := os.OpenFile("/data/data/com.termux/files/home/.matrix_ide/logs/agy_master.log", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err == nil {
		f.WriteString(logLine)
		f.Close()
	}
}

func main() {
	promptFlag := flag.String("p", "", "Run a one-shot command headlessly")
	flag.Parse()

	if *promptFlag != "" {
		handleOneShot(*promptFlag)
		return
	}

	interactiveLoop()
}

func handleOneShot(prompt string) {
	resp, err := callLLM(prompt)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		os.Exit(1)
	}
	fmt.Println(resp)
}

func interactiveLoop() {
	fmt.Println("🌌 Custom Antigravity CLI (agy-go) - 32-bit Android")
	fmt.Println("Connected to local llama-server on port 8080")
	fmt.Println("Type /exit to quit.")

	scanner := bufio.NewScanner(os.Stdin)
	for {
		fmt.Print("\n> ")
		if !scanner.Scan() {
			break
		}
		input := scanner.Text()

		if input == "" {
			continue
		}

		if input == "/exit" || input == "/quit" {
			return
		}

		resp, err := callLLM(input)
		if err != nil {
			fmt.Printf("Error: %v\n", err)
		} else {
			fmt.Printf("\n[Danube]: %s\n", resp)
		}
	}
}

func callLLM(userPrompt string) (string, error) {
	requestBody, _ := json.Marshal(ChatCompletionRequest{
		Messages: []Message{
			{Role: "system", Content: "You are a terminal. Output ONLY the bash command. NO prose. NO markdown. NO explanations. If you see a command, repeat it exactly if it solves the task."},
			{Role: "user", Content: userPrompt},
		},
		MaxTokens:   256,
		Temperature: 0.0,
	})

	resp, err := http.Post(baseURL+"/chat/completions", "application/json", bytes.NewBuffer(requestBody))
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()

	body, _ := io.ReadAll(resp.Body)
	var chatResp ChatCompletionResponse
	if err := json.Unmarshal(body, &chatResp); err != nil {
		return "", err
	}

	if len(chatResp.Choices) > 0 {
		text := chatResp.Choices[0].Message.Content
		
		// 1. Check for Markdown blocks
		if strings.Contains(text, "```bash") {
			text = strings.Split(text, "```bash")[1]
			text = strings.Split(text, "```")[0]
		} else if strings.Contains(text, "```") {
			text = strings.Split(text, "```")[1]
			text = strings.Split(text, "```")[0]
		}

		// 2. Fallback: Take the first line that contains common bash tokens
		lines := strings.Split(text, "\n")
		for _, line := range lines {
			trimmed := strings.TrimSpace(line)
			if trimmed == "" { continue }
			// If it looks like a sentence, skip it
			if strings.HasPrefix(trimmed, "The") || strings.HasPrefix(trimmed, "This") || strings.HasPrefix(trimmed, "Here") || strings.HasPrefix(trimmed, "Sure") {
				continue
			}
			if strings.HasPrefix(trimmed, "echo") || strings.HasPrefix(trimmed, "touch") || strings.HasPrefix(trimmed, "mkdir") || strings.HasPrefix(trimmed, "python") || strings.HasPrefix(trimmed, "sqlite3") || strings.HasPrefix(trimmed, "sed") || strings.HasPrefix(trimmed, "cat") || strings.HasPrefix(trimmed, "curl") || strings.HasPrefix(trimmed, "nc") || strings.HasPrefix(trimmed, "ls") {
				text = trimmed
				break
			}
		}

		// 3. Clean remaining template markers
		text = strings.Split(text, "<|")[0]
		text = strings.TrimSpace(text)
		
		logInteraction(userPrompt, text)
		return text, nil
	}

	return "No response from model.", nil
}
