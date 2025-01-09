package main

import (
	"backend/internal/route"
	"log"
)

func main() {
	// 啟動 Gin 服務
	_, err := route.InitGinServer()
	if err != nil {
		log.Fatal(err)
	}
}
