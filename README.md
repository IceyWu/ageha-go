<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/IceyWu/ageha-python/main/assets/brand/ageha-mark-light.svg">
    <img src="https://raw.githubusercontent.com/IceyWu/ageha-python/main/assets/brand/ageha-mark.svg" alt="Ageha butterfly mark" width="128" height="128">
  </picture>
  <h1>Ageha</h1>
  <p><strong>A Go toolkit.</strong></p>
  <p>Created and maintained by Lev Wu.</p>
  <p><a href="https://github.com/IceyWu/ageha-go/blob/main/README.md">English</a> · <a href="https://github.com/IceyWu/ageha-go/blob/main/README.zh-CN.md">简体中文</a></p>
  <p>
    <a href="https://github.com/IceyWu/ageha-go/actions/workflows/ci.yml"><img src="https://github.com/IceyWu/ageha-go/actions/workflows/ci.yml/badge.svg?branch=main" alt="CI"></a>
    <a href="https://pkg.go.dev/github.com/IceyWu/ageha-go"><img src="https://pkg.go.dev/badge/github.com/IceyWu/ageha-go.svg" alt="Go Reference"></a>
    <img src="https://img.shields.io/badge/Go-1.26%2B-00ADD8?style=flat-square&amp;logo=go&amp;logoColor=white" alt="Go 1.26+">
    <a href="https://github.com/IceyWu/ageha-go/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-555555?style=flat-square" alt="MIT license"></a>
  </p>
</div>

---

Ageha is a Go toolkit by **Lev Wu**.

## Installation

Ageha is available through the public Go module proxy. No GitHub authentication is required.

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

## Development

Requires Go 1.26+ and Python 3.11+ for consumer verification.

```bash
go test ./...
go vet ./...
go build ./...
python scripts/verify-consumer.py
```

## Releases

Release Please maintains a version PR and changelog. Merging it creates a Git tag
and GitHub Release through CI, then verifies a fresh download of that exact version.
See the [release guide](docs/publishing.md).

## License

[MIT](LICENSE) · **Lev Wu**
