subarch: amd64
version_stamp: latest
target: stage4
rel_type: default
profile: default/linux/amd64/17.0
snapshot: latest
source_subpath: default/stage3-amd64-latest
portage_confdir: /etc/portage
portage_overlay: /var/lib/GentooStudio /var/lib/audio-overlay


stage4/motd: Welcome to Gentoo-pro audio. non-RT kernel. 
stage4/use:
abi_x86_32
abi_x86_64
X
a52
aac
aacplus
alsa
audacious
cdda
cddb
cdio
consolekit
corefonts
dbus
dirac
dssi
dts
dv
dvd
encode
equalizer
faac
ffmpeg
fftw
flac
fluidsynth
freesound
g3dvl
gif
gtk
gudev
hwdb
icu
id3
id3tag
ieee1394
introspection
jack
jpeg
ladspa
lame
libsamplerate
lv2
mad
matroska
midi
minizip
mp3
mp4
mpeg
mpg123
musepack
musicbrainz
netjack
ogg
opengl
opus
pcre16
png
policykit
python
python_targets_python3_5
qt3support
qt5
quicktime
realtime
rubberband
schroedinger
shine
shout
skins
sndfile
soundtouch
svg
taglib
theora
tiff
timidity
truetype
twolame
udev
upower
usb
vamp
vcd
vorbis
wav
wavpack
x264
xine
xkb
xml
xvfb
xvid
xvmc
-introspection
-pulseaudio
-xscreensaver

stage4/packages:
app-admin/syslog-ng
app-editors/nano
app-portage/cpuid2cpuflags
app-portage/eix
app-portage/gentoolkit
app-portage/repoman
app-portage/smart-live-rebuild
app-portage/ufed
dev-vcs/git
gnome-extra/nm-applet
media-libs/hydrogen-drumkits
media-plugins/alsa-plugins
media-plugins/calf
media-plugins/distrho-ports
media-plugins/dpf-plugins
media-plugins/drumgizmo
media-plugins/dssi-vst
media-plugins/eq10q-bin
media-plugins/swh-plugins
media-sound/a2jmidid
media-sound/alsa-tools
media-sound/alsa-utils
media-sound/ardour
media-sound/audacity
media-sound/cadence
media-sound/carla
media-sound/chuck
media-sound/fluidsynth
media-sound/fmit
media-sound/frescobaldi
media-sound/hydrogen
media-sound/idjc
media-sound/jack-rack
media-sound/jack2
media-sound/jamin
media-sound/japa
media-sound/lmms
media-sound/musescore
media-sound/pure-data
media-sound/qjackctl
media-sound/qsampler
media-sound/qtractor
media-sound/rosegarden
media-sound/sequencer64
media-sound/supercollider
media-video/ffmpeg
media-video/vlc
net-misc/dhcpcd
net-misc/networkmanager
sys-apps/usbutils
sys-boot/grub
sys-kernel/genkernel
sys-kernel/linux-firmware
x11-base/xorg-server
x11-misc/lightdm
x11-terms/xfce4-terminal
xfce-base/xfce4-meta
xfce-extra/xfce4-power-manager

# stage4/packages notes:
# /dev/vcs-git required for eix-sync to work

# Do not put sys-kernel/rt-sources in stage4/packages. That will cause boot/kernel to fail.
#boot/kernel: rt
#boot/kernel/rt/sources: rt-sources
#boot/kernel/rt/config: /root/catalyst/rt-sources-4.14.15-rt13.config
#boot/kernel/rt/packages: xf86-input-libinput

# dotc: MODDED: Tue Aug 20 13:45:36 PDT 2019
boot/kernel: gk-all
boot/kernel/gk-all/sources: gentoo-sources
boot/kernel/gk-all/gk_kernargs: --no-splash all


stage4/rcadd: alsasound|default dbus|default NetworkManager|default xdm|default

stage4/empty
/tmp
/usr/portage/distfiles
/usr/src
/var/cache/edb/dep
/var/cache/genkernel
/var/cache/portage/distfiles
/var/empty
/var/run
/var/state
/var/tmp

stage4/rm:
/etc/*-
/etc/*.old
/etc/ssh/ssh_host_*
/root/.*history
/root/.lesshst
/root/.ssh/known_hosts
/root/.viminfo
/usr/lib64/python*/site-packages/gentoolkit/test/eclean/testdistfiles.tar.gz

stage4/fsscript: /root/catalyst/fsscript.sh
