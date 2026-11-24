include ../../mk/book.mk

LATEXPAND ?= latexpand

.PHONY: export-problem

export-problem: problems/$(HW).tex
	mkdir -p build/export
	$(LATEXPAND) "$<" > "build/export/$(HW).tex"
