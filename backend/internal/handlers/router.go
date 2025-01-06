package handlers

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

// SetupRouter initializes the Gin router
func SetupRouter() *gin.Engine {
    router := gin.Default()

    router.POST("/analyze", HandleAnalyzeRoute)

    return router
}

// HandleAnalyzeRoute handles the /analyze route
func HandleAnalyzeRoute(c *gin.Context) {
    // Forward request to Python microservice
    resp, err := http.Post("http://localhost:5000/analyze", "application/json", c.Request.Body)
    if err != nil {
        c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to call AI service"})
        return
    }
    defer resp.Body.Close()

    c.DataFromReader(resp.StatusCode, resp.ContentLength, resp.Header.Get("Content-Type"), resp.Body, nil)
}
