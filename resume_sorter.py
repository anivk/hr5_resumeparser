import csv

accept_ids = {}
ids = []
resume_title = []



link_page = []
html = open('demo.htm').readlines()
for line in html:
    if line.strip()[:4] == 'href':
        link_page.append(line)

fnames = []
for line in html:
    if line.strip()[:15] == '<td class=xl72>':
        fnames.append(line[17:-7])

lnames = []
for line in html:
    if line.strip()[:15] == '<td class=xl76>':
        lnames.append(line[17:-7])

id = []
for line in html:
    print line

link_page_sanitize_1 = []
for linker in link_page:
    link_page_sanitize_1.append(linker.strip()[68:])

#print link_page_sanitize_1

link_page_sanitize_2 = []
for linker in link_page_sanitize_1:
    link_page_sanitize_2.append(linker.strip()[:-16])

print ids
print link_page_sanitize_2

counter = 0

for person in ids:
    for res_name in link_page_sanitize_2:
        if person[3] == res_name[13:]:
            counter = counter + 1


