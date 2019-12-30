# Kurchin_CV
This is the code I use for maintaining my CV. To see what the output looks like, take a look at the `CV.pdf` file in this repo. It’s reasonably customizable; I’ll provide basic info here, you can also check out this blog post (link to come) for more details about my choices in putting this together!

**If you use this for your own CV, feel free to adapt but please fork this repo and credit me as well as the original authors (see below).**

## Features
* Formatting for main sections (one narrow column of customizable width for dates, one wide for details) and subheaders within these sections
* Built-in functions for several types of item listing formats
* Automatic import of `.tsv` files used for maintaining various parts of [my website](rkurchin.github.io) ([repo here](https://github.com/rkurchin/rkurchin.github.io)) using Python scripts (or you can generate the TeX files yourself if you don’t use the same webpage format)
* Automatic import of publication list from a `.bib` file, including bolding of name and numbering of citations
* (one of my favorite parts) Customizable vertical spacing “fudge factors” to avoid those annoying situations where the last little bit of a section runs onto the next page

## Basic usage
1. Edit `CV.tex` and the contents of the “inputs” folder (these can either be done by hand or using `cv.py`, see below) to contain your own information.
2. Run `pdflatex CV.tex` and the output should be produced in `CV.pdf`

### Using Python scripts
The Python code is designed to read from a `.bib` file (for Publications) and `.tsv` (for other sections). For an example of the format of these files, see the “markdown_generator” folder in [the repo for my website](https://github.com/rkurchin/rkurchin.github.io).

If you use this, make sure to edit the top section of `cv.py` so it knows where to find these files and any/all spellings or formats of your name that come up in your citations so that it can make them bold.

## Requirements
### TeX packages 
Nothing exotic here, should all be present in a standard distro.
(The particular use of each one is indicated in comments in `cv.cls`)
* `parskip`
* `xcolor`
* `geometry`
* `fancyhdr`
* `hyperref`
* `tabularx`
* `longtable`
* `sparse`
* `calc`
* `ulem`

### Python packages
(Only necessary if you want to use the automagical Python code that generates the contents of the “inputs” folder)
* `pandas`
* `pybtex`

## Credit where credit is due
* The basic layout of the CV is heavily inspired by [Jerry Wang](https://www.cmu.edu/cee/people/faculty/wang.html)’s CV.
* For the structure of the `cv.cls` file, I started from [this template](https://www.overleaf.com/articles/rishi-shahs-resume/vgxvkmxktyxn) that I found on Overleaf, which was originally developed by [Trey Hunner](https://treyhunner.com) and posted on [LaTeX Templates](https://www.latextemplates.com)
* The Python code for citation formatting was adapted from something I got from [Giuseppe Romano](https://github.com/romanodev) awhile ago