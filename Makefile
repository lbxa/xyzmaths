.PHONY: books check

books:
	$(MAKE) -C books/linear-algebra book
	$(MAKE) -C books/maths-analysis book

check:
	$(MAKE) -C books/linear-algebra check
	$(MAKE) -C books/maths-analysis check
