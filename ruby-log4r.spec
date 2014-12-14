#
# Conditional build:
%bcond_without	doc			# don't build ri/rdoc

%define pkgname log4r
Summary:	Ruby Logging framework
Summary(pl.UTF-8):	Szkielet do logowania w języku Ruby
Name:		ruby-%{pkgname}
Version:	1.1.9
Release:	4
License:	GPL v3
Group:		Development/Libraries
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	5b402b3b8f3735d56f93301f37f149ff
URL:		http://log4r.rubyforge.org/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
Provides:	ruby-LOG4R
Obsoletes:	ruby-LOG4R
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log4r is a comprehensive and flexible logging library written in Ruby
for use in Ruby programs. It features a hierarchical logging system of
any number of levels, custom level names, logger inheritance, multiple
output destinations, execution tracing, custom formatting, thread
safetyness, XML and YAML configuration, and more.

%description -l pl.UTF-8
Log4r to obszerna i elastyczna biblioteka do logowania napisana w
języku Ruby przeznaczona do używania w programach napisanych w tym
języku. Jest to system hierarchicznego logowania z dowolną liczbą
poziomów, własnymi nazwami poziomów, dziedziczeniem loggerów, wieloma
docelowymi wyjściami, śledzeniem wykonywania, własnym formatowaniem,
uwzględnieniem wątków, konfiguracją XML i YAML i innymi.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%__gem_helper spec

%if %{with doc}
rdoc --op rdoc lib
rdoc --ri --op ri lib
rm -r ri/{Object,REXML}
rm ri/cache.ri
rm ri/created.rid
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir},%{ruby_ridir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}
rm -r $RPM_BUILD_ROOT%{ruby_vendorlibdir}/log4r/rdoc

%if %{with doc}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{ruby_vendorlibdir}/log4r.rb
%{ruby_vendorlibdir}/log4r
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

%if %{with doc}
%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/Log4r
%dir %{ruby_ridir}/lib
%{ruby_ridir}/lib/log4r
%endif
