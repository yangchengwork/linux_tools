package main

import (
    "log"
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

    r.POST("/form", func(c *gin.Context) {
        username := c.PostForm("username");
        password := c.DefaultPostForm("password", "000000");

        c.JSON(http.StatusOK, gin.H {
            "username": username,
            "password": password,
        })
    })

    r.POST("/posts", func(c *gin.Context) {
        id          := c.Query("id");
        page        := c.DefaultQuery("page", "0");
        username    := c.PostForm("username");
        password    := c.DefaultPostForm("password", "000000");

        c.JSON(http.StatusOK, gin.H {
            "id"      : id,
            "page"    : page,
            "username": username,
            "password": password,
        })
    })

    r.POST("/postmap", func(c *gin.Context) {
        ids     := c.QueryMap("ids");
        names   := c.PostFormMap("names")

        c.JSON(http.StatusOK, gin.H {
            "ids"   : ids,
            "names" : names,
        })
    })

    r.GET("/redirect", func(c *gin.Context) {
        c.Redirect(http.StatusMovedPermanently, "/index")
    })

    r.GET("/goindex", func(c *gin.Context) {
        c.Request.URL.Path = "/"
        r.HandleContext(c)
    })

    defaultHandler := func(c *gin.Context) {
        c.JSON(http.StatusOK, gin.H {
            "path": c.FullPath(),
        })
    }
    // grous: v1
    v1 := r.Group("/v1");
    {
        v1.GET("/posts", defaultHandler)
        v1.GET("/series", defaultHandler)
    }
    // grous: v2
    v2 := r.Group("/v2");
    {
        v2.GET("/posts", defaultHandler)
        v2.GET("/series", defaultHandler)
    }

    r.POST("/upload1", func(c *gin.Context) {
        file, _ := c.FormFile("file")
        // c.SaveUploaderFile(file, dst)
        c.String(http.StatusOK, "%s uploaded!", file.Filename)
    })

    r.POST("/upload2", func(c *gin.Context) {
        // Multipart form
        form, _ := c.MultipartForm();
        files := form.File["upload[]"]

        for _, file := range files {
            log.Println(file.Filename)
            // c.SaveUploadedFile(file, dst)
        }
        c.String(http.StatusOK, "%d files uploaded!", len(files))
    })

    r.Run(":9080");
}
