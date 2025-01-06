package main

import (
	"backend/internal/route"
	"log"
	"net/http"
)

func main() {
	// 初始化 Gin 路由
	router := route.InitRouter()

	// 啟動伺服器
	log.Println("Backend is running on :8080")
	log.Fatal(http.ListenAndServe(":8080", router))
}
