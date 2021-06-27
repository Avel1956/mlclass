BUILDIR = F:\Onedrive\Doctorado\Doctorado 2021\software\mlclass\Reference clssificator\Markdown files
FILENAME = marktest

command:
	mkdir $(BUILDIR) -p
	pandoc $(FILENAME).md \
	--filter pandoc-citeproc \
	--from= markdown+text_math_single_backslash+tex_math_dollars+raw_tex \
	--to=latex \
	--output=$(BUILDIR)/$(FILENAME).pdf \
	--pdf-engine+xelatex


