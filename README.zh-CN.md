<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/IceyWu/ageha-python/main/assets/brand/ageha-mark-light.svg">
    <img src="https://raw.githubusercontent.com/IceyWu/ageha-python/main/assets/brand/ageha-mark.svg" alt="Ageha 蝴蝶标志" width="128" height="128">
  </picture>
  <h1>Ageha</h1>
  <p><strong>一个 Go 工具包。</strong></p>
  <p>由 Lev Wu 创建与维护。</p>
  <p><a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a></p>
  <p>
    <a href="https://github.com/IceyWu/ageha-go/actions/workflows/ci.yml"><img src="https://github.com/IceyWu/ageha-go/actions/workflows/ci.yml/badge.svg?branch=main" alt="CI"></a>
    <img src="https://img.shields.io/badge/Go-1.26%2B-00ADD8?style=flat-square&amp;logo=go&amp;logoColor=white" alt="Go 1.26+">
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-555555?style=flat-square" alt="MIT license"></a>
  </p>
</div>

---

Ageha 是由 **Lev Wu** 开发的 Go 工具包。

## 安装

这是一个私有 Go 模块。先通过有仓库权限的账号完成 Git 认证，
并在 `GOPRIVATE` 中加入 `github.com/IceyWu/ageha-go`（保留已有规则）。

```bash
go get github.com/IceyWu/ageha-go@v0.0.1
```

```go
package main

import (
    "fmt"
    "github.com/IceyWu/ageha-go"
)

func main() {
    fmt.Println(ageha.Greet("Lev Wu")) // Hello, Lev Wu!
}
```

## 开发

需要 Go 1.26+；独立模块验证脚本需要 Python 3.11+。

```bash
go test ./...
go vet ./...
go build ./...
python scripts/verify-consumer.py
```

## 发布

Release Please 自动维护版本与变更日志 PR；合并后由 CI 创建 Git 标签和 GitHub Release，
再从 GitHub 下载该版本进行独立调用验证。详见[发布指南](docs/publishing.md)。

## 许可证

[MIT](LICENSE) · **Lev Wu**
