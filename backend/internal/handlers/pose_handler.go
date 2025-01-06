// pose_handler.go - 處理 /analyze 路由
package handlers

import (
    "net/http"
    "github.com/gin-gonic/gin"
    "backend/internal/clients"
)

// HandleAnalyzeRoute handles the /analyze route
func HandleAnalyzeRoute(c *gin.Context) {
    // Call AI Service
    clients.CallAIService()

    // Respond to client
    c.JSON(http.StatusOK, gin.H{"message": "Pose analyzed successfully"})
}
