package services

import (
	"backend/internal/clients"
	"io"
)

// AnalyzeServiceInterface 定義業務邏輯的接口
type AnalyzeServiceInterface interface {
	AnalyzePose(image io.Reader, filename string) (map[string]interface{}, error)
}

// AnalyzeService 提供業務邏輯實現
type AnalyzeService struct {
	Client clients.AIClientInterface
}

// NewAnalyzeService 創建 AnalyzeService 的新實例
func NewAnalyzeService(client clients.AIClientInterface) AnalyzeServiceInterface {
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
