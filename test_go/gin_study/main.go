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

    r.GET("/user/:name", func(c *gin.Context) {
        name := c.Param("name");
        c.String(http.StatusOK, "Hello %s", name);
    })

    r.GET("/user/:name/*action", func(c *gin.Context) {
        name := c.Param("name");
        action := c.Param("action");
        msg := name + " is " + action;
        c.String(http.StatusOK, msg);
    })

    r.GET("/users", func(c *gin.Context) {
        name := c.Query("name");
        role := c.DefaultQuery("role", "teacher");
        c.String(http.StatusOK, "%s is %s", name, role);
    })

    r.Run(":9080");
}
