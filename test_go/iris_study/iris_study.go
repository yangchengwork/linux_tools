package main

import (
	"fmt"

	"github.com/kataras/iris/v12"
)

func main() {
	fmt.Println("hello world!")

	app := iris.New()
	app.RegisterView(iris.HTML("./views", ".html"))

	// Method: GET
	// Resource: http://localhost:8080
	app.Get("/", func(ctx iris.Context) {
		ctx.ViewData("message", "中文测试")
		ctx.View("hello.html")
	})

	// Method: GET
	// Resource: http://localhost:8080/user/42
	app.Get("/user/{id:uint64}", func(ctx iris.Context) {
		userID, _ := ctx.Params().GetUint64("id")
		ctx.Writef("User ID: %d", userID)
		fmt.Println("id", userID)
	})

	app.Listen(":8080", iris.WithCharset("UTF-8"))
}