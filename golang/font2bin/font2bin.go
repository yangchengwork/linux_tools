package main

import (
	"bytes"
	"flag"
	"fmt"
	"image"
	"image/png"
	"io/ioutil"
	"log"
	"os"

	"gopkg.in/gographics/imagick.v2/imagick"
)

var (
	resize  = flag.String("resize", "16x24!", "要转换输出的图片大小")
	binName = flag.String("bin", "/tmp/gump.bin", "输出的bin文件名")
)

const outImg string = "/tmp/gumpTmp.png"

func readImage() []byte {
	f, err := os.Open(outImg)
	if err != nil {
		log.Fatalf("打开转换后的文件错误\n")
	}
	defer f.Close()

	img, err := png.Decode(f)
	if err != nil {
		log.Fatalf("转换格式错误")
	}

	bounds := img.Bounds()
	dx := bounds.Max.X
	dy := bounds.Max.Y
	cy := dy / 8

	offset := 0
	binData := byte(0)
	binArray := make([]byte, 0)

	garyrect := image.NewGray(bounds)

	for iy := 0; iy < cy; iy++ {
		for x := 0; x < dx; x++ {
			for y := 0; y < 8; y++ {
				dotColor := img.At(x, (iy*8)+y)
				garyrect.Set(x, y, dotColor)
				c := garyrect.GrayAt(x, y)
				// fmt.Printf("%d ", c.Y)
				binData = binData >> 1
				if c.Y > 0x10 {
					// fmt.Printf("0")
				} else {
					binData += 0x80
					// fmt.Printf("1")
				}

				offset++
				if (offset % 8) == 0 {
					binArray = append(binArray, binData)
					// fmt.Printf("0x%02X, ", binData)
					binData = 0
				}
			}
			// fmt.Println()
		}
	}
	// fmt.Printf("len=%d\n", len(binArray))

	return binArray
}

func conver(resize string, char byte) {
	imagick.Initialize()
	defer imagick.Terminate()
	// fmt.Println(*sizeStr)

	labelChar := fmt.Sprintf("label:%c", char)
	if char == '@' {
		labelChar = "label:@%c"
	} else if char == '\\' {
		labelChar = "label:\\\\"
	}

	_, err := imagick.ConvertImageCommand([]string{
		"convert", "-pointsize", "36",
		// "-colors", "2",
		"-font", "/usr/share/fonts/truetype/iosevka/iosevka-medium.ttf",
		labelChar, outImg,
	})
	if err != nil {
		log.Fatalf("生成文字%d图片失败%s\n", char, err)
	}
	/*
		_, err = imagick.ConvertImageCommand([]string{
			"convert", outImg, "-bordercolor", "white", "-trim", outImg,
		})
		if err != nil {
			log.Fatalf("去除白边失败%s\n", err)
		}
	*/
	_, err = imagick.ConvertImageCommand([]string{
		"convert", outImg, "-resize", resize, "-colorspace", "Gray", outImg,
	})
	if err != nil {
		log.Fatalf("转换图片失败%s\n", err)
	}
}

func main() {
	flag.Parse()

	bData := bytes.NewBuffer([]byte{})

	// 0 ~ 9
	startChar := byte(0x21)
	endChar := byte(0x7F)
	for c := startChar; c < endChar; c++ {
		conver(*resize, c)
		bmpData := readImage()
		bData.Write(bmpData)
	}
	/*
			// A ~ Z
			startChar = byte(0x41)
			endChar = byte(0x5B)
			for c := startChar; c < endChar; c++ {
				conver(*resize, c)
				bmpData := readImage()
				bData.Write(bmpData)
			}

		// a ~ z
		startChar = byte(0x61)
		endChar = byte(0x7B)
		for c := startChar; c < endChar; c++ {
			conver(*resize, c)
			bmpData := readImage()
			bData.Write(bmpData)
		}
	*/

	fmt.Printf("bin %d\n", len(bData.Bytes()))

	err := ioutil.WriteFile(*binName, bData.Bytes(), 0644)
	if err != nil {
		log.Fatalln(err)
	}

}
