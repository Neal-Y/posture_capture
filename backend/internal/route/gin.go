package route

import (
	"backend/internal/clients"
	"backend/internal/handlers"
	"backend/internal/services"
	"github.com/gin-gonic/gin"
	"time"
)

// InitGinServer 初始化 Gin 服務器
func InitGinServer() (*gin.Engine, error) {
	server := GinRouter()
	err := server.Run("127.0.0.1:8080")

	return server, err
}

// GinRouter 註冊路由和初始化依賴
func GinRouter() *gin.Engine {
	server := gin.New()
	server.Use(gin.Logger())

	// 初始化依賴
	client := clients.NewAIClient("http://localhost:8000", 10*time.Second)
	analyzeService := services.NewAnalyzeService(client)

	// 註冊處理器
	handlers.AnalyzeService = analyzeService
	api := server.Group("/api")
	api.POST("/analyze", handlers.AnalyzeHandler)

	return server
}
