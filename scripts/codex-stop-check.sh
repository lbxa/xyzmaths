#!/bin/sh
set -eu

root=$(CDPATH= cd -P "$(dirname "$0")/.." && pwd)
workdir=$(pwd -P)
failed_logs=

for book in books/linear-algebra books/maths-analysis; do
  case "$workdir/" in
    "$root/$book/"*) ;;
    *)
      changes=$(git -C "$root" status --porcelain --untracked-files=normal -- \
        "$book" Makefile mk/book.mk)
      [ -n "$changes" ] || continue
      ;;
  esac

  log="$book/build/codex-stop-check.log"
  mkdir -p "$root/$book/build"
  if ! make -C "$root/$book" check >"$root/$log" 2>&1; then
    failed_logs="$failed_logs $log"
  fi
done

if [ -n "$failed_logs" ]; then
  printf '{"systemMessage":"Book validation failed. See%s."}\n' "$failed_logs"
else
  printf '{}\n'
fi
