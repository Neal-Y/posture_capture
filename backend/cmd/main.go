// main.go - Go 主程序
package main

import (
	"backend/internal/infrastructure"
	"backend/internal/route"
	"log"
)

func main() {
	dbErr := infrastructure.InitMySQL()
	if dbErr != nil {
		log.Fatal(dbErr)
	}

	_, err := route.InitGinServer()
	if err != nil {
		log.Fatal(err)
	}
}
