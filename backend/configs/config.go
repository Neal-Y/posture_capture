package configs

import (
	"log"
	"net/http"
	"time"

	"github.com/spf13/viper"
)

type Config struct {
	AIServiceURL     string
	AIServiceTimeout time.Duration
	ServerHost       string
	ServerPort       int
	HTTPClient       *http.Client
}

var AppConfig Config

func LoadConfig() {
	// 設置 viper 搜索路徑
	viper.AddConfigPath("./configs")
	viper.SetConfigName("config")
	viper.SetConfigType("yaml")

	// 讀取配置文件
	err := viper.ReadInConfig()
	if err != nil {
		log.Fatalf("Error while reading config file: %s", err)
	}

	// 初始化 HTTP 客戶端
	httpClient := &http.Client{
		Timeout: viper.GetDuration("ai_service.timeout"),
	}

	// 初始化配置
	AppConfig = Config{
		AIServiceURL:     viper.GetString("ai_service.url"),
		AIServiceTimeout: viper.GetDuration("ai_service.timeout"),
		ServerHost:       viper.GetString("server.host"),
		ServerPort:       viper.GetInt("server.port"),
		HTTPClient:       httpClient,
	}
}
