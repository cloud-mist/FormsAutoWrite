package main

import (
	"fmt"
	"image"
	_ "image/jpeg"
	_ "image/png"
	"log"
	"os"

	"github.com/liyue201/goqr"
)

func main() {
	res := GetUrl("./xuexi.jpeg")

	f, err := os.Create("./tmp.txt")
	if err != nil {
		log.Fatalln("Restxt File create failed:", err)
	}

	_, err = f.Write([]byte(res))
	if err != nil {
		log.Fatalln("Write url to txt file err:", err)
	}

	fmt.Println("Img2url succeed!")
}

func GetUrl(path string) string {
	f, err := os.Open(path)
	if err != nil {
		log.Fatalln("open file failed :", err)
	}
	defer f.Close()

	img, _, err := image.Decode(f)
	if err != nil {
		log.Fatalln("decode failed:", err)
	}

	qrCodes, err := goqr.Recognize(img)
	if err != nil {
		log.Fatalln("Recognize failed:", err)
	}

	urls := make([]string, 0)

	for _, qrCode := range qrCodes {
		urls = append(urls, string(qrCode.Payload))
	}

	return urls[0]
}
