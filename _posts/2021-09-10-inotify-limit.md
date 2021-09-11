---
title: Change inotify limit
layout: post
tags: [Ubuntu 20.04]
---

add file `/etc/sysctl.d/100-inotify.conf` with following
```bash
# Increase inotify availability
fs.inotify.max_user_watches = 524288
```

Run `sudo sysctl --system` to update sysctl.

Run `sysctl fs.inotify.max_user_watches` to verify.
If the limit is not changed, it may be overwritten by another conf file.  The output of `sudo sysctl --system` provides clues.
