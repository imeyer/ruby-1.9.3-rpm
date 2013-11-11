%define patch_level p448

%define rversion 1.9.3
%define ruby_version %{rversion}.%{patch_level}

%define rubygems_version 1.8.23
%define rake_version 0.9.2.2
%define rdoc_version 3.9.5
%define bigdecimal_version 1.1.0
%define io_console_version 0.3
%define json_version 1.5.5
%define minitest_version 2.5.1

Summary: An interpreter of object-oriented scripting language
Name: ruby
Version: %{ruby_version}
Release: 2%{?dist}
Group: Development/Languages
License: Ruby License/GPL - see COPYING
URL: http://www.ruby-lang.org/
Source0: ftp://ftp.ruby-lang.org/pub/ruby/ruby-%{rversion}-%{patch_level}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: db4-devel
BuildRequires: gdbm-devel
BuildRequires: glibc-devel
BuildRequires: libyaml-devel
BuildRequires: libffi-devel
BuildRequires: ncurses-devel
BuildRequires: openssl-devel
BuildRequires: readline-devel
BuildRequires: tk-devel
BuildRequires: tcl-devel
BuildRequires: gcc
BuildRequires: byacc
BuildRequires: make

Requires: libyaml
Requires: %{name}-libs = %{version}-%{release}

%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming.  It has many features to process text
files and to do system management tasks (as in Perl).  It is simple,
straight-forward, and extensible.

%package devel
Summary: A Ruby development environment
Group: Development/Languages
License: Ruby License/GPL
Requires: %{name} = %{version}-%{release}
Provides: ruby-devel = %{version}-%{release}

%description devel
Header files and libraries for building an extension library for the
Ruby or an application embedding Ruby.

%package libs
Summary: Libraries necessary to run Ruby
Group: Development/Libraries
License: Ruby License/GPL
Requires: %{name} = %{version}-%{release}
Provides: ruby(abi) = %{ruby_abi}

%description libs
This package includes the libruby, necessary to run Ruby.

%package irb
Summary: The Interactive Ruby
Group: Development/Languages
License: Ruby License/GPL
Requires: %{name}-libs = %{version}-%{release}
Requires: ruby(rubygems) >= %{rubygems_version}
Provides: irb = %{version}-%{release}
Provides: ruby(irb) = %{version}-%{release}

%description irb
The irb is acronym for Interactive Ruby.  It evaluates ruby expression
from the terminal.

%package ri
Summary: Ruby interactive reference
Group: Documentation
License: Ruby License/GPL
Requires: rubygem(rdoc) >= %{rdoc_version}
Provides: ri = %{version}-%{release}
Provides: ruby(ri) = %{version}-%{release}

%description ri
ri is a command line tool that displays descriptions of built-in
Ruby methods, classes and modules. For methods, it shows you the calling
sequence and a description. For classes and modules, it shows a synopsis
along with a list of the methods the class or module implements.

This package provides ri descriptions and documentation about Ruby.

The ri executable itself is in the rubygem-rdoc package.

%package -n rubygems
Summary: The Ruby standard for packaging ruby libraries
Version: %{rubygems_version}
Group: Development/Libraries
License: Ruby License/GPL
Requires: ruby(abi) = %{ruby_abi}
Requires: rubygem(rdoc) >= %{rdoc_version}
Requires: rubygem(io-console) >= %{io_console_version}
Provides: gem = %{rubygems_version}
Provides: ruby(rubygems) = %{rubygems_version}

%description -n rubygems
RubyGems is the Ruby standard for publishing and managing third party
libraries.

%package -n rubygem-rake
Summary: Ruby based make-like utility
Version: %{rake_version}
Group: Development/Libraries
License: MIT
Requires: ruby(abi) = %{ruby_abi}
Requires: ruby(rubygems) >= %{rubygems_version}
Provides: rake = %{rake_version}
Provides: rubygem(rake) = %{rake_version}

%description -n rubygem-rake
Rake is a Make-like program implemented in Ruby. Tasks and dependencies are
specified in standard Ruby syntax.

%package -n rubygem-rdoc
Summary: A tool to generate HTML and command-line documentation for Ruby projects
Version: %{rdoc_version}
Group: Development/Libraries
License: Ruby License
Requires: ruby(abi) = %{ruby_abi}
Requires: ruby(rubygems) >= %{rubygems_version}
Requires: ruby(irb) = %{ruby_version}-%{release}
Requires: ruby(ri) = %{ruby_version}-%{release}
Provides: rdoc = %{rdoc_version}
Provides: rubygem(rdoc) = %{rdoc_version}

%description -n rubygem-rdoc
RDoc produces HTML and command-line documentation for Ruby projects.
RDoc includes the +rdoc+ and +ri+ tools for generating and displaying
documentation from the command-line.

%package -n rubygem-bigdecimal
Summary: BigDecimal provides arbitrary-precision floating point number class.
Version: %{bigdecimal_version}
Group: Development/Libraries
License: Ruby License/GPL
Requires: ruby(abi) = %{ruby_abi}
Requires: ruby(rubygems) >= %{rubygems_version}
Provides: rubygem(bigdecimal) = %{bigdecimal_version}

%description -n rubygem-bigdecimal
BigDecimal provides arbitrary-precision decimal floating-point number class.

%package -n rubygem-io-console
Summary: IO/Console is a simple console utilizing library
Version: %{io_console_version}
Group: Development/Libraries
License: Ruby License
Requires: ruby(abi) = %{ruby_abi}
Requires: ruby(rubygems) >= %{rubygems_version}
Provides: rubygem(io-console) = %{io_console_version}

%description -n rubygem-io-console
IO/Console provides very simple and portable access to console. It doesn't
provide higher layer features, such like curses and readline.

%package -n rubygem-json
Summary: This is a JSON implementation as a Ruby extension in C
Version: %{json_version}
Group: Development/Libraries
License: Ruby License
Requires: ruby(abi) = %{ruby_abi}
Requires: ruby(rubygems) >= %{rubygems_version}
Provides: rubygem(json) = %{version}-%{release}

%description -n rubygem-json
This is a implementation of the JSON specification according to RFC 4627
www.ietf.org/rfc/rfc4627.txt.

%package -n rubygem-minitest
Summary: Minitest provides a complete suite of testing facilities.
Version: %{minitest_version}
Group: Development/Libraries
License: MIT
Requires: ruby(abi) = %{ruby_abi}
Requires: ruby(rubygems) >= %{rubygems_version}
Provides: rubygem(minitest) = %{minitest_version}

%description -n rubygem-minitest
minitest provides a complete suite of testing facilities supporting TDD,
BDD, mocking, and benchmarking.

%package tcltk
Summary: Tcl/Tk interface for scripting language Ruby
License: Ruby License
Group: Development/Languages
Requires: ruby(abi) = %{ruby_abi}
Provides: ruby(tcltk) = %{version}-%{release}

%description tcltk
Tcl/Tk interface for the object-oriented scripting language Ruby.

%prep
%setup -n ruby-%{rversion}-%{patch_level}

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
make install DESTDIR=%{buildroot}

#we don't want to keep the src directory
rm -rf %{buildroot}/usr/src

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/ruby-%{rversion}-%{patch_level}

%files
%defattr(-, root, root, -)
%{_bindir}/erb
%{_bindir}/ruby
%{_bindir}/testrb
%doc COPYING*
%doc ChangeLog
%doc GPL
%doc BSDL
%doc LEGAL
%doc README
%doc NEWS
%doc doc/ChangeLog-*
%doc doc/NEWS-*
%doc README.EXT*
%doc ToDo
%{_mandir}/man1/erb*
%{_mandir}/man1/ruby*

%files devel
%defattr(-, root, root, -)
%{_libdir}/libruby.so
%{_libdir}/libruby-static.a
%{_libdir}/ruby/1.9.1/mkmf.rb
%dir %{_libdir}/ruby/1.9.1
%{_libdir}/pkgconfig/ruby-1.9.pc
%dir %{_libdir}/pkgconfig
%{_includedir}

%files libs
%defattr(-, root, root, -)
%doc doc/etc.rd
%doc doc/etc.rd.ja
%doc doc/forwardable.rd.ja
%doc doc/forwardable.rd
%doc ext/racc/cparse/README
%doc ext/readline/README*
%doc ext/ripper/README
%doc ext/stringio/README
%doc ext/syslog/syslog.txt
%doc doc/re.rdoc
%doc doc/shell.rd
%doc doc/shell.rd.ja
%dir %{_libdir}/ruby
%{_libdir}/ruby/1.9.1
%{_libdir}/libruby.so.*

%exclude %{_libdir}/ruby/1.9.1/irb.rb
%exclude %{_libdir}/ruby/1.9.1/irb

%exclude %{_libdir}/ruby/1.9.1/ubygems.rb
%exclude %{_libdir}/ruby/1.9.1/rubygems.rb
%exclude %{_libdir}/ruby/1.9.1/rubygems
%exclude %{_libdir}/ruby/1.9.1/rbconfig

%exclude %{_libdir}/ruby/1.9.1/rake.rb
%exclude %{_libdir}/ruby/1.9.1/rake
%exclude %{_libdir}/ruby/gems/1.9.1/gems/rake-%{rake_version}
%exclude %{_libdir}/ruby/gems/1.9.1/specifications/rake-%{rake_version}.gemspec

%exclude %{_libdir}/ruby/1.9.1/rdoc.rb
%exclude %{_libdir}/ruby/1.9.1/rdoc
%exclude %{_libdir}/ruby/gems/1.9.1/gems/rdoc-%{rdoc_version}
%exclude %{_libdir}/ruby/gems/1.9.1/specifications/rdoc-%{rdoc_version}.gemspec

%exclude %{_libdir}/ruby/1.9.1/bigdecimal
%exclude %{_libdir}/ruby/1.9.1/%{_arch}-linux/bigdecimal.so
%exclude %{_libdir}/ruby/gems/1.9.1/specifications/bigdecimal-%{bigdecimal_version}.gemspec

%exclude %{_libdir}/ruby/1.9.1/io
%exclude %{_libdir}/ruby/1.9.1/%{_arch}-linux/io
%exclude %{_libdir}/ruby/gems/1.9.1/specifications/io-console-%{io_console_version}.gemspec

%exclude %{_libdir}/ruby/1.9.1/json.rb
%exclude %{_libdir}/ruby/1.9.1/json
%exclude %{_libdir}/ruby/1.9.1/%{_arch}-linux/json
%exclude %{_libdir}/ruby/gems/1.9.1/specifications/json-%{json_version}.gemspec

%exclude %{_libdir}/ruby/1.9.1/minitest
%exclude %{_libdir}/ruby/gems/1.9.1/specifications/minitest-%{minitest_version}.gemspec

%exclude %{_libdir}/ruby/1.9.1/tk*.rb
%exclude %{_libdir}/ruby/1.9.1/*-tk.rb
%exclude %{_libdir}/ruby/1.9.1/tcltk.rb
%exclude %{_libdir}/ruby/1.9.1/%{_arch}-linux/tcltklib.so
%exclude %{_libdir}/ruby/1.9.1/%{_arch}-linux/tkutil.so
%exclude %{_libdir}/ruby/1.9.1/tk
%exclude %{_libdir}/ruby/1.9.1/tkextlib

%files irb
%defattr(-, root, root, -)
%{_bindir}/irb
%{_libdir}/ruby/1.9.1/irb.rb
%{_libdir}/ruby/1.9.1/irb
%{_mandir}/man1/irb.1*

%files ri
%defattr(-, root, root, -)
%{_datadir}/ri

%files -n rubygems
%defattr(-, root, root, -)
%{_bindir}/gem
%{_libdir}/ruby/1.9.1/ubygems.rb
%{_libdir}/ruby/1.9.1/rubygems.rb
%{_libdir}/ruby/1.9.1/rubygems
%{_libdir}/ruby/1.9.1/rbconfig
%{_libdir}/ruby/gems
%{_libdir}/ruby/site_ruby
%{_libdir}/ruby/vendor_ruby
%exclude %{_libdir}/ruby/gems/1.9.1/gems
%exclude %{_libdir}/ruby/gems/1.9.1/specifications

%files -n rubygem-rake
%defattr(-, root, root, -)
%{_bindir}/rake
%{_libdir}/ruby/1.9.1/rake.rb
%{_libdir}/ruby/1.9.1/rake
%{_libdir}/ruby/gems/1.9.1/gems/rake-%{rake_version}
%{_libdir}/ruby/gems/1.9.1/specifications/rake-%{rake_version}.gemspec
%{_mandir}/man1/rake.1*

%files -n rubygem-rdoc
%defattr(-, root, root, -)
%{_bindir}/ri
%{_bindir}/rdoc
%{_libdir}/ruby/1.9.1/rdoc.rb
%{_libdir}/ruby/1.9.1/rdoc
%{_libdir}/ruby/gems/1.9.1/gems/rdoc-%{rdoc_version}
%{_libdir}/ruby/gems/1.9.1/specifications/rdoc-%{rdoc_version}.gemspec
%{_mandir}/man1/ri*

%files -n rubygem-bigdecimal
%defattr(-, root, root, -)
%doc ext/bigdecimal/*.html
%doc ext/bigdecimal/README
%{_libdir}/ruby/1.9.1/bigdecimal
%{_libdir}/ruby/1.9.1/%{_arch}-linux/bigdecimal.so
%{_libdir}/ruby/gems/1.9.1/specifications/bigdecimal-%{bigdecimal_version}.gemspec

%files -n rubygem-io-console
%defattr(-, root, root, -)
%{_libdir}/ruby/1.9.1/io
%{_libdir}/ruby/1.9.1/%{_arch}-linux/io
%{_libdir}/ruby/gems/1.9.1/specifications/io-console-%{io_console_version}.gemspec

%files -n rubygem-json
%{_libdir}/ruby/1.9.1/json.rb
%{_libdir}/ruby/1.9.1/json
%{_libdir}/ruby/1.9.1/%{_arch}-linux/json
%{_libdir}/ruby/gems/1.9.1/specifications/json-%{json_version}.gemspec

%files -n rubygem-minitest
%{_libdir}/ruby/1.9.1/minitest
%{_libdir}/ruby/gems/1.9.1/specifications/minitest-%{minitest_version}.gemspec

%files tcltk
%{_libdir}/ruby/1.9.1/tk*.rb
%{_libdir}/ruby/1.9.1/*-tk.rb
%{_libdir}/ruby/1.9.1/tcltk.rb
%{_libdir}/ruby/1.9.1/%{_arch}-linux/tcltklib.so
%{_libdir}/ruby/1.9.1/%{_arch}-linux/tkutil.so
%{_libdir}/ruby/1.9.1/tk
%{_libdir}/ruby/1.9.1/tkextlib

%changelog
* Mon Nov 11 2013 Claudio Filho <claudio.filho@locaweb.com.br> - 1.9.3.p448-2
- Fix variables.
- Fix version.
- Fix licenses.
- Fix BuildRequires.
- Fix %clean.
- Split ruby package into various subpackages:
  - ruby-devel
  - ruby-libs
  - ruby-irb
  - ruby-ri
  - ruby-tcltk
  - rubygems
  - rubygem-rake
  - rubygem-rdoc
  - rubygem-bigdecimal
  - rubygem-io-console
  - rubygem-json
  - rubygem-minitest

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
