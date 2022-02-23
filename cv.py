import pandas as pd
import pybtex.database.input.bibtex
from cv_fcns import *

# name formats in .bib file (to make bold in publications section)
name_formats = ["R. Kurchin", "R. C. Kurchin"]

# define file paths to content
pubs_fpath = "MyPapers.bib"
awards_fpath = "../rkurchin.github.io/markdown_generator/awards.tsv"
# talks_fpath = "../rkurchin.github.io/markdown_generator/talks.tsv"
talks_contrib_fpath = "talks_contrib.tsv"
talks_invited_fpath = "talks_invited.tsv"
posters_fpath = "./posters.tsv"
# service_fpath = "../rkurchin.github.io/markdown_generator/service.tsv"

# can exclude some posters to keep CV from running over pages
#posters_exclude = [3, 4, 12]
posters_exclude = [4, 12]

# define paths to TeX outputs
pubs_texpath = "inputs/pubs.tex"
awards_texpath = "inputs/awards.tex"
# talks_texpath = "inputs/talks.tex"
talks_invited_texpath = "inputs/talks_invited.tex"
talks_contrib_texpath = "inputs/talks_contrib.tex"
posters_texpath = "inputs/posters.tex"
service_texpath = "inputs/service.tex"

# make dictionaries for easy indexing/readability
# (there's probably a tidier way to do this...)
sections = ["awards", "talks_invited", "talks_contrib", "posters"] #, "service"]
sections_files = {"awards":awards_fpath, "talks_invited":talks_invited_fpath, "talks_contrib":talks_contrib_fpath, "posters":posters_fpath} #, "service":service_fpath}
sections_tex = {"awards":awards_texpath, "talks_invited":talks_invited_texpath, "talks_contrib":talks_contrib_texpath, "posters":posters_texpath} # , "service":service_texpath}
sections_fcns = {"awards":list_award, "talks_invited":list_pres, "talks_contrib":list_pres, "posters": list_pres} #, "service":list_service}

# write out the TeX files
for sec in sections:
    # read in the data
    datafile = sections_files[sec]
    info = pd.read_csv(datafile, sep="\t", header=0)

    if sec == "posters":
        info.drop(posters_exclude, inplace=True)
    
    texfile = sections_tex[sec]
    list_func = sections_fcns[sec]

    with open(texfile,'w') as f:
        # list first one explicitly
        first_line = dict(info.iloc[0])
        
        # add a little fudge space, not sure what in .cls file makes this necessary...
        if sec=="service":
            first_line["date_str"] = "\hspace{-1.5mm}" + first_line["date_str"]
        else:
            first_line["date"] = "\hspace{-1.5mm}" + first_line["date"]

        list_func(first_line, f)

        year = info.iloc[0].date[:4]
        if sec=="service":
            year = info.iloc[0].date_str

        # then iterate through and print year only when it changes
        for row, item in info.iloc[1:].iterrows():
            if sec=="service":
                list_func(dict(item), f)
            elif item.date[:4]==year:
                list_func(dict(item), f, include_year=False)
            else:
                year = item.date[:4]
                list_func(dict(item), f)

            
#### PUBLICATIONS
# doing separately from other sections for now because of the numbering
# could probably all be rolled in without *too* much difficulty

# read in data
parser = pybtex.database.input.bibtex.Parser()
pubs = parser.parse_file(pubs_fpath)

# write TeX file
with open(pubs_texpath,'w') as f:
    for n,entry in enumerate(pubs.entries):
        m = len(pubs.entries)-n # reverse numbering

        if len(str(m)) == 1: # pad number
            num_str = '0' + str(m)
        else:
            num_str = str(m)

        # for first one, include year
        if n==0:
            list_pub(pubs, entry, f, num_str, name_formats)
            year = pubs.entries[entry].fields['year']
        else:
            if pubs.entries[entry].fields['year'] == year:
                list_pub(pubs, entry, f, num_str, name_formats, include_year=False)
            else:
                year = pubs.entries[entry].fields['year']
                list_pub(pubs, entry, f, num_str, name_formats)
