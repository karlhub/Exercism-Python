import re

def format_type(line):
    # Function to format line according to possible types: header, unordered list, or paragraph
    mlh = re.match('#+ (.*)', line)
    pos = line.find(" ")
    if mlh and pos in (1,2,6):
        # Line is a header
        lin = '<h' + str(pos) + '>' + mlh.group(1) + '</h' + str(pos) + '>'
        typ = "header"
    else:
        mll = re.match('\* (.*)', line)
        if mll:
            # Line is an unordered list
            lin = '<li>' + mll.group(1) + '</li>'
            typ = "unordered list"
        else:
            # Line is a paragraph
            lin = '<p>' + line + '</p>'
            typ = "paragraph"
    return lin, typ

def format_ul(lin, typ_prev, typ):
    # Function to detect first or last item of an unordered list and format accordingly
    if typ_prev != typ:
        if typ == "unordered list":
            # 1st item of an unordered list
            lin = "<ul>" + lin
        elif typ_prev == "unordered list":
            # 1st item after an unordered list
            lin = "</ul>" + lin
    return lin

def format_line(lin):
    # Function to format line: detect bold and italic pieces of line.
    ml = re.match('(.*)__(.*)__(.*)', lin)
    if ml:
        # Bold
        lin = format_line(ml.group(1)) + '<strong>' + format_line(ml.group(2)) + '</strong>' + format_line(ml.group(3))
    ml = re.match('(.*)_(.*)_(.*)', lin)
    if ml:
        # Italic
        lin = format_line(ml.group(1)) + '<em>' + format_line(ml.group(2)) + '</em>' + format_line(ml.group(3))
    return lin

def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    typ = ''
    for lin in lines:
        typ_prev = typ
        lin, typ = format_type(lin)
        lin = format_ul(lin, typ_prev, typ)
        lin = format_line(lin)
        res += lin
    if typ == "unordered list":
        # close unordered list in case last line was an item of an UL
        res = res + "</ul>"
    return res

# Program tester
#while True:
#    markdown_text = input ("Markdown text: ")
#    if markdown_text == "done":
#        break
#    print ("Markdown parsed: ", parse(markdown_text))

#print ("=> End of program")
