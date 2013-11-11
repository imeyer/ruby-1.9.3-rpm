# What is this spec?

This spec is an attempt to push for a stable replacement of Ruby 1.8.x with 1.9.3+ on RHEL based systems. I have based it off of the work of [FrameOS](http://www.frameos.org) specs for Ruby 1.9.3 and Ruby Enterprise Edition.

### How to install

#### RHEL/CentOS 5/6

    yum install -y rpm-build rpmdevtools readline-devel ncurses-devel gdbm-devel tcl-devel openssl-devel db4-devel byacc libyaml-devel libffi-devel make glibc-devel tk-devel gcc
    rpmdev-setuptree
    cd ~/rpmbuild/SOURCES
    wget http://ftp.ruby-lang.org/pub/ruby/1.9/ruby-1.9.3-p448.tar.gz
    cd ~/rpmbuild/SPECS
    wget https://raw.github.com/imeyer/ruby-1.9.3-rpm/master/ruby19.spec
    rpmbuild -bb ruby19.spec
    ARCH=`uname -m`
    KERNEL_REL=`uname -r`
    KERNEL_TMP=${KERNEL_REL%.$ARCH}
    DISTRIB=${KERNEL_TMP##*.}
    yum localinstall ~/rpmbuild/RPMS/${ARCH}/ruby-1.9.3.p448-2.${DISTRIB}.${ARCH}.rpm ~/rpmbuild/RPMS/${ARCH}/ruby-libs-1.9.3.p448-2.${DISTRIB}.${ARCH}.rpm \
        ~/rpmbuild/RPMS/${ARCH}/ruby-devel-1.9.3.p448-2.${DISTRIB}.${ARCH}.rpm ~/rpmbuild/RPMS/${ARCH}/ruby-irb-1.9.3.p448-2.${DISTRIB}.${ARCH}.rpm \
        ~/rpmbuild/RPMS/${ARCH}/ruby-ri-1.9.3.p448-2.${DISTRIB}.${ARCH}.rpm ~/rpmbuild/RPMS/${ARCH}/rubygems-1.8.23-2.${DISTRIB}.${ARCH}.rpm \
        ~/rpmbuild/RPMS/${ARCH}/rubygem-rake-0.9.2.2-2.${DISTRIB}.${ARCH}.rpm ~/rpmbuild/RPMS/${ARCH}/rubygem-rdoc-3.9.5-2.${DISTRIB}.${ARCH}.rpm \
        ~/rpmbuild/RPMS/${ARCH}/rubygem-bigdecimal-1.1.0-2.${DISTRIB}.${ARCH}.rpm ~/rpmbuild/RPMS/${ARCH}/rubygem-io-console-0.3-2.${DISTRIB}.${ARCH}.rpm \
        ~/rpmbuild/RPMS/${ARCH}/rubygem-json-1.5.5-2.${DISTRIB}.${ARCH}.rpm ~/rpmbuild/RPMS/${ARCH}/rubygem-minitest-2.5.1-2.${DISTRIB}.${ARCH}.rpm \
        ~/rpmbuild/RPMS/${ARCH}/ruby-tcltk-1.9.3.p448-2.${DISTRIB}.${ARCH}.rpm ~/rpmbuild/RPMS/x86_64/ruby-debuginfo-1.9.3.p448-2.${DISTRIB}.${ARCH}.rpm 

**PROFIT!**

If you are having trouble on the last line because of installed rubies, then run:

`yum remove ruby-* puppet facter`

### What it does

+ Builds
+ Installs
+ Overwrites/upgrades your currently installed ruby package (**DANGEROUS**)

### What it does **not** do

+ Split packages into ruby-libs, ruby-devel, etc (looking for help here)
+ Install alongside Ruby 1.8.x

###

+ If you upgrade from an already installed 1.8.x, you will need to re-install all of your gems. If anyone has a decent way to do this programatically, i'll add it to the doc.

### Requirements

+ EPEL Yum repository (for rpmdev-setuptree)

### Distro support

Tested working (as sane as I could test for) on:

* CentOS 5.x x86_64
* CentOS 6.3 (Final)

### Personal thoughts

This is by no means, correct, or sane. Nor does it follow any sort of policy for packaging. I leave that to the people who are most familiar with such things, and will willingly accept patches that add those features.
