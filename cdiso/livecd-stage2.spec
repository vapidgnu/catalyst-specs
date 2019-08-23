subarch: amd64
version_stamp: latest
target: livecd-stage2
rel_type: default
profile: default/linux/amd64/17.0/desktop
snapshot: latest
source_subpath: default/livecd-stage1-amd64-installer-latest

livecd/bootargs: dokeymap
livecd/cdtar: /usr/share/catalyst/livecd/cdtar/isolinux-elilo-memtest86+-cdtar.tar.bz2
livecd/fsscript: /home/dotc/repos/releng/releases/weekly/scripts/livecd.sh
livecd/fstype: squashfs

### dotc
# mod: Thu May  9 10:38:41 PDT 2019
livecd/iso: livecd-amd64-near-genreleng.iso

livecd/type: gentoo-release-livecd
livecd/volid: Gentoo amd64 LiveCD latest
livecd/xsession: awesome
livecd/xdm: gdm
livecd/motd: "dotc did" 
### dotc 
## mod: Thu May  9 10:33:18 PDT 2019
#livecd/overlay: @REPO_DIR@/releases/latest/overlays/common/overlay/livecd
#livecd/root_overlay: @REPO_DIR@/releases/latest/overlays/common/root_overlay

boot/kernel: gentoo
boot/kernel/gentoo/sources: =sys-kernel/gentoo-sources-4.19.27-r1 
boot/kernel/gentoo/config: /root/generated-config
boot/kernel/gentoo/use: atm png truetype usb
boot/kernel/gentoo/packages:
	media-libs/alsa-oss
	media-sound/alsa-utils
### Masked (~amd64)
#	net-dialup/fcdsl
### Masked (~amd64)
#	net-dialup/fritzcapi
### Masked (~amd64)
#	net-dialup/slmodem
#	net-misc/br2684ctl
### Masked (~amd64)
#	net-wireless/acx
	net-wireless/hostap-utils
#	net-wireless/ipw3945
#	net-wireless/madwifi-ng-tools
#	net-wireless/rt2500
### Masked (~amd64)
#	net-wireless/rtl8187
#	sys-apps/pcmciautils
	sys-kernel/linux-firmware
	sys-fs/ntfs3g

livecd/empty:
	/var/tmp
	/var/empty
	/var/run
	/var/state
	/var/cache/edb/dep
	/tmp
	/usr/portage
	/usr/src
	/root/.ccache
	/usr/share/genkernel/pkg/x86/cpio

livecd/rm:
	/etc/*-
	/etc/*.old
	/root/.viminfo
	/var/log/*.log
	/usr/share/genkernel/pkg/x86/*.bz2
