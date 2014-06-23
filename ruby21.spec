%define rubyver         2.1
%define rubyminorver    2
%define rubyversion     %{rubyver}.%{rubyminorver}

Name:           ruby
Version:        %{rubyversion}
Release:        1%{?dist}
License:        Ruby License/GPL - see COPYING
URL:            http://www.ruby-lang.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  readline libyaml libyaml-devel readline-devel ncurses ncurses-devel gdbm gdbm-devel glibc-devel tcl-devel gcc unzip openssl-devel db4-devel byacc make libffi-devel unzip
Requires:       libyaml
Source0:        ftp://ftp.ruby-lang.org/pub/ruby/%{rubyver}/ruby-%{rubyversion}.tar.gz
Summary:        An interpreter of object-oriented scripting language
Group:          Development/Languages
Provides: ruby(abi) = 2.1
Provides: ruby-irb
Provides: ruby-rdoc
Provides: ruby-libs
Provides: ruby-devel
Provides: ruby(rubygems)
Provides: rubygems
Obsoletes: ruby
Obsoletes: ruby-libs
Obsoletes: ruby-irb
Obsoletes: ruby-rdoc
Obsoletes: ruby-devel
Obsoletes: rubygems

%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming.  It has many features to process text
files and to do system management tasks (as in Perl).  It is simple,
straight-forward, and extensible.

%prep
%setup -n ruby-%{rubyversion}

%build
export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"

%configure \
  --enable-shared \
  --disable-rpath \
  --includedir=%{_includedir}/ruby \
  --libdir=%{_libdir}

make %{?_smp_mflags}

%install
# installing binaries ...
make install DESTDIR=$RPM_BUILD_ROOT

#we don't want to keep the src directory
rm -rf $RPM_BUILD_ROOT/usr/src

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_bindir}
%{_includedir}
%{_datadir}
%{_libdir}

%changelog
* Mon Jun 23 2014 Aleks Bunin <github@compuix.com> - 2.1.2
- Updated for Ruby 2.1.2
* Fri Jun 6 2014 Aleks Bunin <sbunin@gmail.com> - 2.0.0-p481
- Updated for Ruby 2.0.0-p481
* Mon Nov 25 2013 Aleks Bunin <sbunin@gmail.com> - 2.0.0-p353
- Updated for Ruby 2.0.0-p353
* Fri Aug 23 2013 Aleks Bunin <sbunin@mgail.com> - 2.0.0-p247
- Update for Ruby 2.0.0-p247
* Thu Jun 27 2013 Henrik <henrik@haf.se> - 1.9.3-p448
- Update for Ruby 1.9.3-p448 release.
* Thu May 23 2013 Attila Bogár <attila@fidescreativa.com> - 1.9.3-p429
- Update for Ruby 1.9.3-p429 release.
* Tue Apr 23 2013 Aleks Bunin <sbunin@gmail.com> - 1.9.3-p392
- Update for Ruby 1.9.3-p392 release.
* Thu Feb 14 2013 Martin Bokman <martin@bokman.org> - 1.9.3-p385
- Update for Ruby 1.9.3-p385 release.
* Tue Feb 5 2013 Ian Meyer <ianmmeyer@gmail.com> - 1.9.3-p374
- Update for Ruby 1.9.3-p327 release.
* Sun Nov 25 2012 Gareth Jones <me@gazj.co.uk> - 1.9.3-p327
- Update for Ruby 1.9.3-p327 release.
* Wed Apr 25 2012 mathew <meta@pobox.com> - 1.9.3-p194-1
- Update for Ruby 1.9.3-p194 release.
* Sat Feb 24 2012 Ian Meyer <ianmmeyer@gmail.com> - 1.9.3-p125-1
- Spec to replace system ruby with 1.9.3-p125
