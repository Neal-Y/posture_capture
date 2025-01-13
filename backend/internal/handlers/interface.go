package handlers

import (
	"backend/internal/services"
	"github.com/gin-gonic/gin"
)

type AnalyzeHandler struct {
	analyzeService services.AnalyzeServiceInterface
}

func RegisterAnalyzeRoutes(r *gin.RouterGroup, analyzeService services.AnalyzeServiceInterface) *AnalyzeHandler {
	h := &AnalyzeHandler{analyzeService: analyzeService}

	newRoute(h, r)

	return h
}

func newRoute(h *AnalyzeHandler, r *gin.RouterGroup) {
	r.POST("/analyze", h.Analyze)
}
