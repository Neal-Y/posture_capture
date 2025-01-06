// gin.go - 初始化路由
package route

import (
    "github.com/gin-gonic/gin"
    "backend/internal/handlers"
)

// InitGinServer initializes the Gin server
func InitGinServer() (*gin.Engine, error) {
    router := gin.Default()

    handlers.SetupRouter(router)

    return router, nil
}
