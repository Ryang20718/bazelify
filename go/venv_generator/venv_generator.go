package main

import (
	"fmt"
	"os"
	"path/filepath"
	"strings"
)

func main() {
	err := filepath.Walk("bazel-bin/python", func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if strings.Contains(path, "site-pa") && strings.Contains(path, "pip_") {
			fmt.Println(path)
		}
		return nil
	})
	if err != nil {
		fmt.Println(err)
	}
}
