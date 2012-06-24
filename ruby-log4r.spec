%define tarname log4r
Summary:	Ruby Logging framework
Summary(pl):	Szkielet do logowania w j�zyku Ruby
Name:		ruby-LOG4R
Version:	1.0.5
Release:	2
License:	GPL
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/log4r/%{tarname}-%{version}.tgz
# Source0-md5:	fc69892335d86f7dcd8f8b47a1bbe801
Source1:	setup.rb
URL:		http://log4r.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
%ruby_mod_ver_requires_eq
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log4r is a comprehensive and flexible logging library written in Ruby
for use in Ruby programs. It features a hierarchical logging system of
any number of levels, custom level names, logger inheritance, multiple
output destinations, execution tracing, custom formatting, thread
safetyness, XML and YAML configuration, and more.

%description -l pl
Log4r to obszerna i elastyczna biblioteka do logowania napisana w
j�zyku Ruby przeznaczona do u�ywania w programach napisanych w tym
j�zyku. Jest to system hierarchicznego logowania z dowoln� liczb�
poziom�w, w�asnymi nazwami poziom�w, dziedziczeniem logger�w, wieloma
docelowymi wyj�ciami, �ledzeniem wykonywania, w�asnym formatowaniem,
uwzgl�dnieniem w�tk�w, konfiguracj� XML i YAML i innymi.

%prep
%setup -q -n %{tarname}-%{version}
cp %{SOURCE1} .
mv src lib

%build
ruby setup.rb config \
	--siterubyver=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup
rdoc --inline-source --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_rubylibdir}/*
%{ruby_ridir}/*
