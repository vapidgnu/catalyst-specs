#!/bin/bash

wget https://gentoostudio.org/src/builds/complete/make.conf
wget https://gentoostudio.org/src/builds/complete/fstab
wget https://gentoostudio.org/src/builds/complete/limits.conf
wget https://gentoostudio.org/src/builds/complete/fw.rules
wget https://gentoostudio.org/src/builds/complete/GentooStudio.conf
wget https://gentoostudio.org/src/builds/complete/audio-overlay.conf
wget https://gentoostudio.org/src/builds/complete/xdm

# If existing make.conf files are not rm'd, the mv'd file won't replace it.
rm /etc/portage/make.conf*
mv make.conf /etc/portage/
mv fstab /etc/
mv limits.conf /etc/security/
mv fw.rules /etc/udev/rules.d/
mv GentooStudio.conf /etc/portage/repos.conf/
mv audio-overlay.conf /etc/portage/repos.conf/
mv xdm /etc/conf.d/

# Does /etc/security/limits.d/40-realtime-base.conf replace limits.conf?

# Make sure system is up to date
eix-sync
emerge -uDN --quiet --keep-going --with-bdeps=y --backtrack=1000 @system @world
emerge @preserved-rebuild
emerge --depclean
revdep-rebuild

# Official python for GentooStudio:
eselect python set python3.5

# Make sure /dev/snd/seq is present - not auto-loaded for some reason.
cat > /etc/conf.d/modules <<EOF
modules="snd_seq"
EOF
