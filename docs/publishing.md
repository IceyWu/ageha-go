# Publishing

Ageha is a private Go module, `github.com/IceyWu/ageha-go`, containing package `ageha`.
Go module identity is its import path; there is no global bare-name reservation for `ageha`.
Go publishes library versions as Git tags, not as uploads to a separate registry.

## CI release workflow

1. Implement a change using Conventional Commits (`feat:`, `fix:`, breaking-change markers).
2. Push/merge to `main`. CI checks Go 1.26.0 and latest stable on Linux, and stable on Windows.
3. Release Please's Go strategy updates `version.go`, the manifest and changelog in a version PR.
4. Review and merge the version PR. CI creates `vX.Y.Z` and a GitHub Release.
5. In the same workflow, CI downloads that exact private module into an empty module cache,
   compiles/runs an independent consumer, checks the version and module source, and verifies module checksums.

There is no local publish command. All release tags are created by CI. The first release is
`v0.0.1`; the initial commit uses `Release-As: 0.0.1`, not a permanent version override.
Bot-created version PRs are checked explicitly through reusable CI, since ordinary PR workflows
may require approval or not automatically run when created with `GITHUB_TOKEN`.

The built-in `GITHUB_TOKEN` is sufficient for this repository's CI to create releases and read
the private module. Consumer verification passes credentials only through temporary subprocess
environment configuration, never through a persisted credential URL or file.

## Installing a private module

Use a GitHub account with read access. Configure Git authentication with GitHub CLI (`gh auth setup-git`)
or your own SSH/credential setup. Add `github.com/IceyWu/ageha-go` to `GOPRIVATE`, preserving
any existing patterns. This avoids sending private module requests to public proxies and checksum services.

```bash
go get github.com/IceyWu/ageha-go@v0.0.1
```

The repository remains private, so unauthenticated users cannot install it and pkg.go.dev/public
module proxies cannot index it. Publishing for unrestricted public use would require making
the source available publicly (or operating a suitable separate public module distribution).

## Validation and recovery

CI runs gofmt, `go mod tidy` with a clean-diff check, vet, unit/example tests, build, and an independent
consumer. Local verification uses a `replace` directive; released-version verification forbids
`replace`, requires the exact version, and verifies the downloaded module lives in the fresh cache.

Preserve the pre-release commit before merging. Never move or overwrite a published version tag:
Go caches and authenticates module content. Fix a bad release with a new version PR; if necessary,
retract it in a later `go.mod` release. Do not delete a tag to simulate rollback of a cached module.

References: [Go publishing](https://go.dev/doc/modules/publishing),
[Private modules](https://go.dev/ref/mod#private-modules),
[Release Please strategies](https://github.com/googleapis/release-please/blob/main/docs/customizing.md).
