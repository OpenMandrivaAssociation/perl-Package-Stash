%define upstream_name Package-Stash
%define upstream_version 0.34

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Package::Stash::Conflicts\\)'
%else
%define _requires_exceptions perl(Package::Stash::Conflicts)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Routines for manipulating stashes
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Package/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Module::Implementation)
BuildRequires:	perl(Package::Stash::XS)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Requires)
BuildRequires:	perl(Dist::CheckConflicts)
BuildRequires:	perl(Package::DeprecationManager)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Manipulating stashes (Perl's symbol tables) is occasionally necessary, but
incredibly messy, and easy to get wrong. This module hides all of that
behind a simple API.

NOTE: Most methods in this class require a variable specification that
includes a sigil. If this sigil is absent, it is assumed to represent the
IO slot.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README META.json
%{_mandir}/man3/*
%{perl_vendorlib}/Package
%{_bindir}/package-stash-conflicts


%changelog
* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.290.0-1mdv2011.0
+ Revision: 654179
- update to new version 0.29

* Sat Mar 19 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.260.0-1
+ Revision: 647035
- new version

* Wed Feb 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.250.0-1
+ Revision: 635206
- update to new version 0.25

* Sat Jan 08 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.220.0-1mdv2011.0
+ Revision: 630617
- new version

* Thu Nov 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.130.0-1mdv2011.0
+ Revision: 596033
- update to new version 0.13

* Mon Jul 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 551215
- import perl-Package-Stash


* Mon Jul 12 2010 cpan2dist 0.05-1mdv
- initial mdv release, generated with cpan2dist
