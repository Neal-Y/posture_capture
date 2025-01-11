package clients

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"mime/multipart"
	"net/http"
)

// AIClientInterface 定義 AI 客戶端的接口
type AIClientInterface interface {
	AnalyzePose(image io.Reader, filename string) (map[string]interface{}, error)
}

type AIClient struct {
	BaseURL    string
	HTTPClient *http.Client
}

// NewAIClient 初始化 AI 微服務客戶端
func NewAIClient(baseURL string, httpClient *http.Client) AIClientInterface {
	return &AIClient{
		BaseURL:    baseURL,
		HTTPClient: httpClient,
	}
}

// AnalyzePose 發送圖像到 AI 微服務進行分析
func (c *AIClient) AnalyzePose(image io.Reader, filename string) (map[string]interface{}, error) {
	// 準備 HTTP 請求
	req, err := c.prepareRequest(image, filename)
	if err != nil {
		return nil, fmt.Errorf("準備請求失敗: %w", err)
	}

	// 發送請求並獲取響應
	resp, err := c.doRequest(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	// 解析響應
	result, err := c.parseResponse(resp.Body)
	if err != nil {
		return nil, fmt.Errorf("解析響應失敗: %w", err)
	}

	return result, nil
}

// prepareRequest 準備包含圖像的 HTTP 請求
func (c *AIClient) prepareRequest(image io.Reader, filename string) (*http.Request, error) {
	// 構建 multipart 表單數據
	body := &bytes.Buffer{}
	writer := multipart.NewWriter(body)

	part, err := writer.CreateFormFile("image", filename)
	if err != nil {
		return nil, err
	}

	if _, err := io.Copy(part, image); err != nil {
		return nil, err
	}

	if err := writer.Close(); err != nil {
		return nil, err
	}

	// 創建 HTTP 請求
	req, err := http.NewRequest("POST", c.BaseURL+"/analyze", body)
	if err != nil {
		return nil, err
	}

	// 設置請求頭
	req.Header.Set("Content-Type", writer.FormDataContentType())

	return req, nil
}

// doRequest 發送 HTTP 請求並返回響應
func (c *AIClient) doRequest(req *http.Request) (*http.Response, error) {
	resp, err := c.HTTPClient.Do(req)
	if err != nil {
		return nil, fmt.Errorf("發送請求失敗: %w", err)
	}

	// 檢查響應狀態碼
	if resp.StatusCode != http.StatusOK {
		resp.Body.Close()
		return nil, fmt.Errorf("AI 微服務返回錯誤狀態: %s", resp.Status)
	}

	return resp, nil
}

// parseResponse 解析響應體為結果
func (c *AIClient) parseResponse(body io.Reader) (map[string]interface{}, error) {
	var result map[string]interface{}
	if err := json.NewDecoder(body).Decode(&result); err != nil {
		return nil, err
	}
	return result, nil
}
