%define modname	Package-Stash
%define modver 0.39

Summary:	Routines for manipulating stashes
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/Package::Stash
Source0:	http://www.cpan.org/modules/by-module/Package/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Module::Implementation)
BuildRequires:	perl(Package::Stash::XS)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Requires)
BuildRequires:	perl(Dist::CheckConflicts)
# Not found by rpm auto-provides
Provides:	perl(Package::Stash::Conflicts) = %{version}
BuildRequires:	perl-devel

%description
Manipulating stashes (Perl's symbol tables) is occasionally necessary, but
incredibly messy, and easy to get wrong. This module hides all of that
behind a simple API.

NOTE:	Most methods in this class require a variable specification that
includes a sigil. If this sigil is absent, it is assumed to represent the
IO slot.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README META.json
%{_bindir}/package-stash-conflicts
%{perl_vendorlib}/Package
%{_mandir}/man3/*
%{_mandir}/man1/package-stash-conflicts.1*
