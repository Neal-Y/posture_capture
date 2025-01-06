package handlers

import (
	"backend/internal/services"
	"github.com/gin-gonic/gin"
	"net/http"
)

func AnalyzeHandler(c *gin.Context) {
	// 獲取上傳的文件
	file, err := c.FormFile("image")
	if err != nil {
		// 打印錯誤
		c.JSON(http.StatusBadRequest, gin.H{"error": "No image provided"})
		return
	}

	openedFile, openErr := file.Open()
	if openErr != nil {
		// 打印文件打開錯誤
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to open file"})
		return
	}
	defer openedFile.Close()

	// 調用業務邏輯
	result, err := services.AnalyzePose(openedFile)
	if err != nil {
		// 打印業務邏輯的錯誤
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}

	// 返回分析結果
	c.JSON(http.StatusOK, result)
}
