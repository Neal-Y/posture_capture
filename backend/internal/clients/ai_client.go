package clients

import (
	"io"
)

// AnalyzePose simulates the response from AI service
func AnalyzePose(file io.Reader) (map[string]interface{}, error) {
	// 模擬返回固定結果
	return map[string]interface{}{
		"message": "Mock success",
		"landmarks": []map[string]float64{
			{"x": 0.5, "y": 0.5, "z": 0.0},
			{"x": 0.6, "y": 0.4, "z": 0.0},
		},
	}, nil
}
