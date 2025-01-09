package clients

import (
	"bytes"
	"encoding/json"
	"errors"
	"io"
	"mime/multipart"
	"net/http"
	"time"
)

// AIClient struct for the AI service client
type AIClient struct {
	BaseURL string
	Timeout time.Duration
}

// NewAIClient initializes the AI client
func NewAIClient(baseURL string, timeout time.Duration) *AIClient {
	return &AIClient{
		BaseURL: baseURL,
		Timeout: timeout,
	}
}

// AnalyzePose sends an image to the AI service for analysis
func (c *AIClient) AnalyzePose(image io.Reader, filename string) (map[string]interface{}, error) {
	// Prepare multipart form data
	body := &bytes.Buffer{}
	writer := multipart.NewWriter(body)
	part, err := writer.CreateFormFile("image", filename)
	if err != nil {
		return nil, err
	}
	_, err = io.Copy(part, image)
	if err != nil {
		return nil, err
	}
	writer.Close()

	// Send POST request
	client := &http.Client{Timeout: c.Timeout}
	req, err := http.NewRequest("POST", c.BaseURL+"/analyze", body)
	if err != nil {
		return nil, err
	}
	req.Header.Set("Content-Type", writer.FormDataContentType())

	resp, err := client.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	// Check for non-200 status codes
	if resp.StatusCode != http.StatusOK {
		return nil, errors.New("failed to analyze pose: " + resp.Status)
	}

	// Parse JSON response
	var result map[string]interface{}
	err = json.NewDecoder(resp.Body).Decode(&result)
	if err != nil {
		return nil, err
	}

	return result, nil
}
