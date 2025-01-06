package services

import (
	"backend/internal/clients"
	"io"
)

// AnalyzePose processes the image and calls the AI service
func AnalyzePose(file io.Reader) (map[string]interface{}, error) {
	// 調用 AI 微服務
	result, err := clients.AnalyzePose(file)
	if err != nil {
		return nil, err
	}

	return result, nil
}
