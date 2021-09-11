---
title: Hide ubuntu desktop icons
layout: post
system: Ubuntu 20.04
---

{% if page.system %}System: {{ page.system }}{% endif %}

{% if page.title %}# {{ page.title }}{% endif %}

```bash
gsettings set org.gnome.shell.extensions.desktop-icons show-home false
gsettings set org.gnome.shell.extensions.desktop-icons show-trash false

# Optional
gsettings set org.gnome.desktop.background show-desktop-icons false
```
