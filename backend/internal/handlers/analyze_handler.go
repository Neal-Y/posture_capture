package handlers

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

// Analyze 處理 /analyze 請求
func (h *AnalyzeHandler) Analyze(c *gin.Context) {
	// 獲取上傳的文件
	file, err := c.FormFile("image")
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "No image provided"})
		return
	}

	// 調用服務層處理業務邏輯
	result, err := h.analyzeService.ProcessFile(file)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}

	// 返回分析結果
	c.JSON(http.StatusOK, result)
}
