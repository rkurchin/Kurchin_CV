
### functions for generating strings of TeX code
def cvItem_text(date, inst, dept, descr):
    return '\cvItem{{{date}}}{{{inst}}}{{{dept}}}{{{descr}}}\n'.format(date=date, inst=inst, dept=dept, descr=descr).replace('&','\&')

def pubsItem_text(date, num, text):
    return '\pubsItem{{{date}}}{{{num}}}{{{text}}}\n'.format(date=date, num=num, text=text)

# I was using this for dates on talks/posters before I decided to just put years for everything
#def format_date(date_str):
#    (year, month, day) = date_str.split('-')
#    return month+'/'+day+'/'+year

### functions for formatting particular item types
# awards/fellowships
def list_award(award_info, f, include_year=True):
    if include_year:
        year = str(award_info['year'])
    else:
        year = ""
    f.write(cvItem_text(year, award_info['title'], award_info['granter'], ''))

# publication
def list_pub(pubs, entry, f, num, name_formats, include_year=True):
    if include_year:
        year = pubs.entries[entry].fields['year']
    else:
        year = ""
    f.write(pubsItem_text(year, num, get_citation(pubs, entry, name_formats)))

# presentations (talk/poster)
def list_pres(pres_info, f, include_year=True):
    if include_year:
        year = str(pres_info['date'][:-6])
    else:
        year = ""

    title = "\hspace{-1.5mm}" + pres_info['title']

    # hacky fix for several posters that had awkward line breaks
    title = title.replace("Characterization and Bayesian Inference", "Characterization and Bayesian\\newline Inference")

    # scooches title back a bit to line up with next line
    f.write(cvItem_text(year, '', title, pres_info['venue']))

def list_service(serv_info, f):
    date_str = serv_info['date_str'].replace(' - ', ' -- ')
    title = serv_info['title'].replace("School of Engineering", "School of\\newline Engineering")
    f.write(cvItem_text(date_str, serv_info['title'], serv_info['venue'], ''))

# citation stuff

# stuff for truncating author list is unconscionably janky right now and will break if I ever become a supervising author, if not sooner...
def get_citation(pubs, entry, to_bold):
    # original code for this function from Giuseppe Romano, I adapted it

    data = pubs.entries[entry]

    # author list
    max_auths = 5 # max number to list out (-1 because 0-indexed)
    et_al_after = 2 # if more than six, put et al. after this index (this+1 many authors)
    n = len(data.persons['author'])
    if n > max_auths:
        et_al = True
    else:
        et_al = False
    found_me = False
    strc = ''
    for i,au in enumerate(data.persons['author']):

        tmp = str(au).split(',')
        if tmp[1].count(' ') == 2:
            middle_name = ' ' + tmp[1][-1] + '. '
        else:
            middle_name = ' '

        name = tmp[1].strip()[0]
        last_name = tmp[0]
        author = name + '.' + middle_name + last_name

        if author in to_bold:
            author = "\\textbf{{{a}}}".format(a=author)
            found_me = True
            strc += author
            strc += ', '

        if et_al and found_me and i>et_al_after:
            if "et al." not in strc:
                strc += "et al."
        else:
            if i < n-1:
                if not author in strc:
                    strc += author
                    strc += ', '
            else:
                strc += author
                strc += '. '

    # everything else
    if 'url' in data.fields.keys():
        url = data.fields['url']
    else:
        url = ''

    strc += r'''``''' + data.fields['title'] + r'''.'' '''
    for w in data.fields['journal'].split():
        strc += '\href{' + url + '}{' + '\\textit{' + w + '}' + '} '
    #if len(data.fields['volume'])> 0:
    if 'volume' in data.fields:
        strc += '\href{''' + url + '}{' + str(data.fields['volume']) + '}, '
    #if len(data.fields['pages'])> 0:
    if 'pages' in data.fields:
        strc += r'''\href{''' + url + r'''}{''' + str(data.fields['pages']) + '} '
    if len(data.fields['year'])> 0:
        strc += r'''\href{''' + url + r'''}{(''' + str(data.fields['year']) + ')}'

    return strc
