#!/usr/bin/python3

search_pathes = ['n']

import os

candidates = []
for p in search_pathes:
    for root, dirs, files in os.walk(p):
        for file in files:
            if file.endswith(".md"):
                candidates.append(os.path.join(root,file))

# try:
#     import tqdm
#     iterdisplay = lambda x: tqdm.tqdm(x, desc = "searching notes")
# except ImportError:
#     iterdisplay = lambda x: x

# print('Candidates', candidates)

title_link_map = []
for file in candidates:
    with open(file) as f:
        # only check the first 10 lines
        for _ in range(10):
            ln = f.readline()
            if ln.startswith("title:"):
                title_link_map.append((ln[6:].strip(), os.path.splitext(file)[0] + ".html"))
                break
            if ln.startswith("# "):
                title_link_map.append((ln[2:].strip(), os.path.splitext(file)[0] + ".html"))
                break

# print (title_link_map)

with open("index.md", "w") as f:
    f.write("# Note index")
    for title, link in title_link_map:
        f.write("[{}]({})\n\n".format(title, link))
