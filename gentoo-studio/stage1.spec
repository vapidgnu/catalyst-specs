subarch: amd64
target: stage1
version_stamp: latest
rel_type: default
profile: default/linux/amd64/17.0
snapshot: latest
source_subpath: stage3-amd64-latest
update_seed: yes
update_seed_command: --update --deep --newuse --with-bdeps=y --backtrack=1000 @system @world
portage_confdir: /etc/portage
