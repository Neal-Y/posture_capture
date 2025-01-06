package route

import (
	"backend/internal/handlers"
	"github.com/gin-gonic/gin"
)

// InitRouter initializes the API routes
func InitRouter() *gin.Engine {
	router := gin.Default()

	// 定義 /analyze 路由
	router.POST("/analyze", handlers.AnalyzeHandler)

	return router
}
