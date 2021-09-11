---
title: Hide ubuntu desktop icons
layout: post
tags: [Ubuntu 20.04]
---

```bash
gsettings set org.gnome.shell.extensions.desktop-icons show-home false
gsettings set org.gnome.shell.extensions.desktop-icons show-trash false

# Optional
gsettings set org.gnome.desktop.background show-desktop-icons false
```
