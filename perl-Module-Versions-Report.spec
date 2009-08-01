%define upstream_name    Module-Versions-Report
%define upstream_version 1.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Perl module to report versions of all modules in memory
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:  noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Perl module to report versions of all modules in memory.
If you add "use Module::Versions::Report;" to a program (especially handy if 
your program is one that demonstrates a bug in some module), then when the 
program has finished running, you well get a report detailing the all 
modules in memory, and noting the version of each (for modules that 
defined a $VERSION, at least).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -rf $RPM_BUILD_ROOT/%{perl_vendorarch}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog README
%{perl_vendorlib}/*
%{_mandir}/man3/*
