---
title: Customize Scheme Handler
layout: post
tags: [Ubuntu 20.04]
---

create a desktop entry `[name].desktop` in `~/.local/share/applications/`.
[More information about desktop entries](https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html)

```sh
[Desktop Entry]
Type=Application
Name=[description]
Exec=[program] %u
StartupNotify=false
MimeType=x-scheme-handler/[scheme name];
```

Then setup mime information
```sh
xdg-mime default [name].desktop x-scheme-handler/[scheme name]

# check if set up correctly
xdg-mime query default x-scheme-handler/[scheme name]

# may not be necessary?
update-desktop-database ~/.local/share/applications/

# test
xdg-open [scheme name]://something
```
