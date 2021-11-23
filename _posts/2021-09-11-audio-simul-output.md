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

### Latency control

#### Method 1: add a virtual device

```sh
pactl load-module module-null-sink sink_name=delayed
pactl load-module module-loopback latency_msec=150 source=delayed.monitor sink=[fast sink]
pacmd load-module module-combine-sink sink_name=combined slaves=delayed,[slow sink]
```

#### Method 2: in the simplest scenario

```sh
pactl load-module module-loopback latency_msec=150 source_dont_move=true source=[slow sink].monitor sink=[fast sink]
```

### To combine two HDMI audio devices

check the link below

### To remove the virtual combined sink

```sh
# when there is only one virtual combined sink
pacmd unload-module module-combine-sink

# when there are multiple, first find out the index
pactl list short modules
# remove the virtual sink by index
pacmd unload-module [module index]
```

---

Based on
[How to simultaneously play audio via 2 separate HDMI output devices connected to one GPU?](https://askubuntu.com/questions/1212142/how-to-simultaneously-play-audio-via-2-separate-hdmi-output-devices-connected-to),
[Latency doesn't work with PulseAudio on linux](https://unix.stackexchange.com/questions/492716/latency-doesnt-work-with-pulseaudio-on-linux)
