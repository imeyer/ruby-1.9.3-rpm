%define rubyver         1.9.3
%define rubyminorver    p551

Name:           ruby
Version:        %{rubyver}%{rubyminorver}
Release:        0.2%{?dist}
License:        Ruby License/GPL - see COPYING
URL:            http://www.ruby-lang.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  readline libyaml libyaml-devel readline-devel ncurses ncurses-devel gdbm gdbm-devel glibc-devel tcl-devel gcc unzip openssl-devel db4-devel byacc make libffi-devel
Requires:       libyaml
Source0:        ftp://ftp.ruby-lang.org/pub/ruby/ruby-%{rubyver}-%{rubyminorver}.tar.gz
Summary:        An interpreter of object-oriented scripting language
Group:          Development/Languages
Provides: ruby(abi) = 1.9
Provides: ruby-irb = %{version}-%{release}
Provides: ruby-rdoc = %{version}-%{release}
Provides: ruby-libs = %{version}-%{release}
Provides: ruby-devel = %{version}-%{release}
Provides: ruby(rubygems) = %{version}-%{release}
Provides: rubygems = %{version}-%{release}

Obsoletes: ruby-libs < %{version}-%{release}
Obsoletes: ruby-irb < %{version}-%{release}
Obsoletes: ruby-rdoc < %{version}-%{release}
Obsoletes: ruby-devel < %{version}-%{release}
Obsoletes: rubygems < %{version}-%{release}

Conflicts: ruby-libs < %{version}-%{release}
Conflicts: ruby-irb < %{version}-%{release}
Conflicts: ruby-rdoc < %{version}-%{release}
Conflicts: ruby-devel < %{version}-%{release}
Conflicts: rubygems < %{version}-%{release}

%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming.  It has many features to process text
files and to do system management tasks (as in Perl).  It is simple,
straight-forward, and extensible.

%prep
%setup -n ruby-%{rubyver}-%{rubyminorver}

%build
export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"

%configure \
  --enable-shared \
  --disable-rpath \
  --includedir=%{_includedir}/ruby \
  --libdir=%{_libdir}

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

# installing binaries ...
make install DESTDIR=$RPM_BUILD_ROOT

# force compression of man pages
gzip --force $RPM_BUILD_ROOT%{_mandir}/man1/*.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_bindir}/*
%{_includedir}/ruby
%{_datadir}/ri
%{_libdir}/ruby
%{_libdir}/lib*.*
%{_libdir}/pkgconfig/ruby*
%doc %{_mandir}/man1/*.1*
%doc BSDL COPYING COPYING.ja GPL

%changelog
* Mon Mar 23 2015 Nico Kadel-Garcia <nkadel@skyhookwireless.com> - 1.9.3-p551
- Update for Ruby 1.9.3-p551 release.
- Be more specific about libdir, bindir, and mandir components
- Use 0.1 release number, to avoid update conflicts
- Update provides and conflicts and obsolets to help avoid ruby conflict
- Precompress man page entries
* Thu Sep 19 2013 Daniel Haskin <djhaskin987@gmail.com> - 1.9.3-p448
- Added man pages entries
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
