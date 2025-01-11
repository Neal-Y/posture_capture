package main

import (
	"backend/configs"
	"backend/internal/route"
	"log"
)

func main() {
	configs.LoadConfig()

	// 啟動 Gin 服務
	_, err := route.InitGinServer()
	if err != nil {
		log.Fatal(err)
	}
}
