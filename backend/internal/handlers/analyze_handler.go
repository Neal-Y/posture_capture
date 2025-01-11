package handlers

import (
	"backend/internal/services"
	"github.com/gin-gonic/gin"
	"net/http"
)

type AnalyzeHandler struct {
	AnalyzeService services.AnalyzeServiceInterface
}

// NewAnalyzeHandler 創建新的 AnalyzeHandler 實例
func NewAnalyzeHandler(service services.AnalyzeServiceInterface) *AnalyzeHandler {
	return &AnalyzeHandler{
		AnalyzeService: service,
	}
}

// Analyze 處理 /analyze 請求
func (h *AnalyzeHandler) Analyze(c *gin.Context) {
	// 獲取上傳的文件
	file, err := c.FormFile("image")
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "No image provided"})
		return
	}

	// 打開文件
	openedFile, err := file.Open()
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to open image"})
		return
	}
	defer openedFile.Close()

	// 調用 Service 層進行分析
	result, err := h.AnalyzeService.AnalyzePose(openedFile, file.Filename)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}

	// 返回分析結果
	c.JSON(http.StatusOK, result)
}
