%define ruby_archdir    %(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
Summary:	Ruby Logging framework
Name:		ruby-LOG4R
Version:	1.0.5
%define tarname log4r
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://unc.dl.sourceforge.net/sourceforge/log4r/%{tarname}-%{version}.tgz
# Source0-md5:	fc69892335d86f7dcd8f8b47a1bbe801
Source1:	setup.rb
URL:			http://log4r.sourceforge.net/
BuildRequires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log4r is a comprehensive and flexible logging library written in Ruby for use
in Ruby programs. It features a hierarchical logging system of any number of
levels, custom level names, logger inheritance, multiple output destinations,
execution tracing, custom formatting, thread safteyness, XML and YAML
configuration, and more.

%prep
%setup -q -n %{tarname}-%{version}

%build
cp %{SOURCE1} .
mv src lib
ruby setup.rb config \
	--site-ruby=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}

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
%{ruby_ridir}
