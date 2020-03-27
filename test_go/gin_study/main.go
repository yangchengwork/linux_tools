package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

func main() {
    r := gin.Default();

    r.GET("/", func(c *gin.Context) {
        c.String(http.StatusOK, "Who are you?");
    })

    r.Run(":9080");
}
