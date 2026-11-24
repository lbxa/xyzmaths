![XYZ Maths](docs/xyz-splash-banner.png)

# XYZ Maths

XYZ Maths is the home of Lucas Barbosa's mathematics books and problem
editorials, and the source for [xyzmaths.org](https://xyzmaths.org).

| Book                                                                    | Build from the repository root      |
| ----------------------------------------------------------------------- | ----------------------------------- |
| [Linear Algebra](books/linear-algebra/README.md)                        | `make -C books/linear-algebra book` |
| [Introduction to Mathematical Analysis](books/maths-analysis/README.md) | `make -C books/maths-analysis book` |

`make books` builds both PDFs. Each is written to `build/main.pdf` inside
its book directory. `make check` also builds both formula sheets and the
standalone homework handouts. See the [book tooling guide](docs/book-tooling.md)
for prerequisites, editor setup, and release artifacts.

The homepage links to two collections.

- **XYZ Books** at `/books/` lists _Linear Algebra_ at `/notes/linear-algebra/`
  and _Introduction to Mathematical Analysis_ at `/notes/maths-analysis/`.
  Each has a web reader, an exercise index, and its own manuscript PDF on
  GitHub Releases. The [web notes guide](docs/web-notes.md) covers both editions.
- **XYZ PoW** at `/pow/` gives each Problem of the Week a statement, a
  worked solution and an editorial explaining the method.

To publish a weekly problem, add a Markdown file to [src/content/pow](src/content/pow)
using an existing entry as a model. Put the self-contained problem in
`statement`, the direct calculation or proof in `solution`, and the full
editorial in the Markdown body. For a C++ implementation, add a `.cpp` file
with the same basename beside the entry. The solution and editorial both
display that source. Include the problem source, publication date, topic,
difficulty and estimated solving time. The filename supplies its public URL.
The archive and homepage pick up the entry on the next website build.

The books share [authoring skills and conventions](AGENTS.md#books). Each book
maintains its own course outline, source records, homework placement map, and
third-party notices. The original text and illustrations are available under
[CC BY-NC-ND 4.0](books/maths-analysis/LICENSE-CC-BY-NC-ND-4.0.txt).
The shared book build scripts retain their [Apache 2.0 licence](books/linear-algebra/LICENSE).
