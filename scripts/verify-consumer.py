"""Verify Ageha from a separate module, using a local source or a released Git tag."""

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

MODULE = "github.com/IceyWu/ageha-go"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", help="Released v-prefixed tag; omit to check local source")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    version = re.search(r'const Version = "([^"]+)"', (root / "version.go").read_text(encoding="utf-8")).group(1)
    if args.version:
        assert args.version == f"v{version}"
    with tempfile.TemporaryDirectory(prefix="ageha-go-") as temporary:
        consumer = Path(temporary)
        env = os.environ.copy()
        env.update({
            "GOWORK": "off", "GOENV": "off", "GOTOOLCHAIN": "local",
            "GOPROXY": "https://proxy.golang.org", "GOPRIVATE": "", "GONOSUMDB": "",
            "GONOPROXY": "", "GOSUMDB": "sum.golang.org", "GOMODCACHE": str(consumer / "mod-cache"),
            "GOCACHE": str(consumer / "build-cache"), "GIT_TERMINAL_PROMPT": "0",
        })
        def go(*arguments: str, capture: bool = False) -> str:
            result = subprocess.run(["go", *arguments], cwd=consumer, env=env,
                                    check=True, text=True, encoding="utf-8",
                                    stdout=subprocess.PIPE if capture else None)
            return result.stdout or ""

        go("mod", "init", "example.com/ageha-consumer")
        if args.version:
            go("get", f"{MODULE}@{args.version}")
        else:
            go("mod", "edit", f"-replace={MODULE}={root.as_posix()}")
            go("get", f"{MODULE}@v0.0.0")
        (consumer / "main.go").write_text(
            'package main\nimport ("fmt"; "' + MODULE + '")\n'
            'func main() {\n'
            'if ageha.Greet("Lev Wu") != "Hello, Lev Wu!" { panic("greeting mismatch") }\n'
            'if ageha.Greet("世界") != "Hello, 世界!" { panic("unicode mismatch") }\n'
            f'if ageha.Version != "{version}" {{ panic("version mismatch") }}\n'
            'fmt.Println(ageha.Greet("Lev Wu"))\n}\n', encoding="utf-8",
        )
        go("mod", "tidy")
        go("run", "-mod=readonly", ".")
        go("mod", "verify")
        metadata = json.loads(go("list", "-m", "-json", MODULE, capture=True))
        if args.version:
            assert metadata["Version"] == args.version
            assert "Replace" not in metadata
            assert Path(metadata["Dir"]).is_relative_to(consumer / "mod-cache")
            assert metadata["Sum"].startswith("h1:")
        print(json.dumps({"module": MODULE, "version": metadata["Version"],
                          "source": "official Go proxy" if args.version else "local replacement",
                          "checksum": metadata.get("Sum"), "status": "PASSED"}))


if __name__ == "__main__":
    main()
