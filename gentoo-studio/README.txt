"""The Catalyst build process. Spec files are linked in each step:

stage3 seed downloaded from gentoo.org
stage1.spec edited to use seed
catalyst -s latest
catalyst -f stage1.spec
catalyst -f stage2.spec
catalyst -f stage3.spec
catalyst -f stage4.spec
stage4.spec calls fsscript.sh
Other files:

/etc/security/limits.conf – Looking into converting this to /etc/security/limits.d files. """ -- from https://gentoostudio.org/?page_id=174
