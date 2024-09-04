# pandoc-vinotes

This 3rd-party plugin for vinotes integrates the cli tool `pandoc` into vinotes as a simple `export` command.

## Usage

1. `vn export <filepath>` - exports the filepath into a pdf, if filepath not provided, opens a fuzzy finder for choosing markdown files.
2. `vn export-vault` - under development.

## Release

Add the below to your `plugin.json` for installing `pandoc-vinotes` in your vault:

```json
"smyk07/pandoc-vinotes": {
  "utils": ["export", "export-vault"],
  "opts": {}
}
```

_Be sure to run `vn check-plugins` once added..._
