package services

import (
	"backend/internal/clients"
	"io"
)

type AnalyzeService struct {
	Client *clients.AIClient
}

func NewAnalyzeService(client *clients.AIClient) *AnalyzeService {
	return &AnalyzeService{Client: client}
}

// AnalyzePose 處理圖像並調用 AI 微服務
func (s *AnalyzeService) AnalyzePose(file io.Reader, filename string) (map[string]interface{}, error) {
	// 調用 AI 微服務
	result, err := s.Client.AnalyzePose(file, filename)
	if err != nil {
		return nil, err
	}

	return result, nil
}
