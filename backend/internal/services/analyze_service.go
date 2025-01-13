package services

import (
	"backend/internal/clients"
	"errors"
	"mime/multipart"
)

// AnalyzeServiceInterface 定義業務邏輯的接口
type AnalyzeServiceInterface interface {
	ProcessFile(file *multipart.FileHeader) (map[string]interface{}, error)
}

type AnalyzeService struct {
	Client clients.AIClientInterface
}

// NewAnalyzeService 創建 AnalyzeService 的新實例
func NewAnalyzeService(client clients.AIClientInterface) AnalyzeServiceInterface {
	return &AnalyzeService{Client: client}
}

// ProcessFile 處理文件並調用 AI 微服務
func (s *AnalyzeService) ProcessFile(file *multipart.FileHeader) (map[string]interface{}, error) {
	// 打開文件
	openedFile, err := file.Open()
	if err != nil {
		return nil, errors.New("failed to open file")
	}
	defer openedFile.Close()

	// 調用 AI 微服務進行分析
	return s.Client.AnalyzePose(openedFile, file.Filename)
}
