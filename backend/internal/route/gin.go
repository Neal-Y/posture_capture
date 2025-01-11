package route

import (
	"backend/configs"
	"backend/internal/clients"
	"backend/internal/handlers"
	"backend/internal/services"
	"github.com/gin-gonic/gin"
)

// InitGinServer 初始化 Gin 服務器
func InitGinServer() (server *gin.Engine, err error) {
	server = GinRoute()
	// 啟動服務
	err = server.Run(":8080")
	return
}

func GinRoute() (server *gin.Engine) {
	server = gin.New()
	server.Use(gin.Logger())

	// 初始化依賴
	client := clients.NewAIClient(configs.AppConfig.AIServiceURL, configs.AppConfig.HTTPClient)
	analyzeService := services.NewAnalyzeService(client)
	analyzeHandler := handlers.NewAnalyzeHandler(analyzeService)

	// 註冊路由
	api := server.Group("/api")
	api.POST("/analyze", analyzeHandler.Analyze)

	return server
}
