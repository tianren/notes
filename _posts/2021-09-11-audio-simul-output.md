---
title: Play audio simultaneously via multiple devices
layout: post
tags: [Ubuntu 20.04]
---

### Basic

```sh
pacmd load-module module-combine-sink sink_name=combined

# optional, set as default
pacmd set-default-sink combined

# verify
pacmd list-sinks | grep -e "name:" -e "index:"
```

### To specify the set of devices

```sh
# find the names of available sinks
pacmd list-sinks | grep -e "name:" -e "index:"

# create a master virtual sink device
pacmd load-module module-combine-sink sink_name=combined slaves=[name1],[name2]
```

### To combine two HDMI audio devices

check the link below

### To remove the virtual combined sink

```sh
# whne there is only one virtual combined sink
pacmd unload-module module-combine-sink

# when there are multiple, first find out the index
pacmd list-modules | grep -B1 -A3 "<module-combine-sink>"
# remove the virtual sink by index
pacmd unload-module [module index]
```

---

Based on answers below [this question](https://askubuntu.com/questions/1212142/how-to-simultaneously-play-audio-via-2-separate-hdmi-output-devices-connected-to)
