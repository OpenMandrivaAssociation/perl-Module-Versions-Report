%define upstream_name    Module-Versions-Report
%define upstream_version 1.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Perl module to report versions of all modules in memory
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std
rm -rf %{buildroot}%{perl_vendorarch}

%files
%doc ChangeLog README
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.60.0-1mdv2010.0
+ Revision: 406171
- rebuild using %%perl_convert_version

* Thu Oct 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.06-1mdv2009.1
+ Revision: 296795
- update to new version 1.06

* Mon Jun 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-1mdv2009.0
+ Revision: 220144
- update to new version 1.05

* Sat Jun 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-1mdv2009.0
+ Revision: 216585
- update to new version 1.04

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.03-1mdv2008.1
+ Revision: 136291
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon May 21 2007 Michael Scherer <misc@mandriva.org> 1.03-1mdv2008.0
+ Revision: 29061
- Update to new version 1.03

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 1.02-4mdv2008.0
+ Revision: 25297
- rebuild


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.02-3mdk
- Fix According to perl Policy
	- Source URL

* Wed Dec 28 2005 Michael Scherer <misc@mandriva.org> 1.02-2mdk
- Do not ship empty dir

* Sat Oct 01 2005 Michael Scherer <misc@mandriva.org> 1.02-1mdk
- First mandriva package

