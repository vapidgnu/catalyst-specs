subarch: amd64
version_stamp: installer-latest
target: livecd-stage1
rel_type: default
profile: default/linux/amd64/17.0/desktop
snapshot: latest
source_subpath: default/stage3-amd64-desktop-latest
portage_confdir: /home/catalyst/builds/default/portage/

livecd/use:
	branding
	livecd
	socks5

livecd/packages:
	app-accessibility/brltty
	app-admin/hddtemp
	app-admin/ide-smart
	app-admin/logrotate
	app-admin/passook
	app-admin/pwgen
	app-admin/sudo
	app-admin/syslog-ng
	app-arch/mt-st
	app-benchmarks/cpuburn
#	app-cdr/cdrkit
	app-crypt/gnupg
#	app-editors/emacs
	app-editors/vim
	app-misc/mc
	app-misc/screen
	app-portage/gentoolkit
	app-portage/mirrorselect
	app-portage/ufed
	app-text/wgetpaste
	dev-util/ccache
	dev-vcs/cvs
	dev-vcs/git
	dev-vcs/subversion
	gnome-base/gdm
#	gnome-base/gnome
#xfce-base/xfce4
	x11-wm/awesome  
	media-gfx/fbgrab
#	media-sound/audacious
	net-analyzer/netcat
	net-analyzer/nmap
	net-analyzer/tcpdump
	net-analyzer/traceroute
	net-dialup/mingetty
	net-dialup/minicom
### Masked (no keywords)
#	net-dialup/penggy
	net-dialup/pptpclient
	net-dialup/rp-pppoe
	net-firewall/iptables
	net-fs/cifs-utils
	net-fs/nfs-utils
	net-im/pidgin
	net-irc/irssi
#net-irc/xchat
	net-misc/bridge-utils
	net-misc/dhcpcd
	net-misc/iputils
	net-misc/ntp
	net-misc/rdate
	net-misc/rdesktop
	net-misc/vconfig
#net-misc/vpnc
	net-misc/whois
#net-p2p/bittorrent
	net-proxy/dante
	net-proxy/tsocks
	net-wireless/b43-fwcutter
### Masked (~amd64)
#	net-wireless/bcm43xx-fwcutter
	net-wireless/wireless-tools
	net-wireless/wpa_supplicant
### Masked (no keywords)
	sys-apps/ethtool
	sys-apps/fxload
	sys-apps/hdparm
	sys-apps/hwsetup
### Masked (no keywords)
#	sys-apps/ibm-powerpc-utils
### Masked (no keywords)
#	sys-apps/ibm-powerpc-utils-papr
	sys-apps/iproute2
### Masked (no keywords)
#	sys-apps/lssbus
	sys-apps/memtester
	sys-apps/netplug
	sys-block/parted
### Masked (no keywords)
#	sys-apps/powerpc-utils
	sys-apps/sdparm
	sys-apps/sg3_utils
	sys-apps/mlocate
	sys-apps/smartmontools
	sys-block/aoetools
	sys-block/disktype
### Masked (-amd64)
#	sys-block/gpart
	sys-block/partimage
#sys-block/qla-fc-firmware
### Masked (no keywords)
#	sys-boot/aboot
### Masked (no keywords)
#	sys-boot/elilo
	sys-boot/grub
#	sys-boot/lilo
	sys-boot/syslinux
### Masked (no keywords)
#	sys-boot/yaboot
### Masked (no keywords)
#	sys-devel/binutils-hppa64
	sys-devel/distcc
### Masked (no keywords)
#	sys-devel/gcc-hppa64
	sys-firmware/ipw2100-firmware
	sys-firmware/ipw2200-firmware
	sys-firmware/zd1201-firmware
	sys-firmware/zd1211-firmware
	sys-fs/cryptsetup
	sys-fs/dmraid
	sys-fs/dosfstools
	sys-fs/e2fsprogs
#sys-fs/hfsplusutils
	sys-fs/hfsutils
### Masked (no keywords)
#	sys-fs/iprutils
	sys-fs/jfsutils
	sys-fs/lsscsi
	sys-fs/lvm2
#	sys-fs/lvm-user
	sys-fs/mac-fdisk
	sys-fs/mdadm
	sys-fs/ntfs3g
	sys-fs/reiserfsprogs
	sys-fs/xfsprogs
	sys-kernel/genkernel
	sys-libs/gpm
	sys-power/acpid
	sys-process/htop
	sys-process/vixie-cron
	www-client/links
	www-client/qutebrowser
#	www-client/firefox
#	www-client/firefox-bin
	x11-base/xorg-server
	x11-base/xorg-x11
