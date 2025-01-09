package handlers

import (
	"backend/internal/services"
	"github.com/gin-gonic/gin"
	"net/http"
)

var AnalyzeService *services.AnalyzeService

func AnalyzeHandler(c *gin.Context) {
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
	result, err := AnalyzeService.AnalyzePose(openedFile, file.Filename)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}

	// 返回分析結果
	c.JSON(http.StatusOK, result)
}
