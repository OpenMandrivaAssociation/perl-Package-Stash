%define upstream_name    Package-Stash
%define upstream_version 0.29

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Routines for manipulating stashes
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Package/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::Fatal)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Requires)
BuildRequires: perl(Dist::CheckConflicts)
BuildRequires: perl(Package::DeprecationManager)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml LICENSE README META.json
%{_mandir}/man3/*
%{perl_vendorlib}/Package
%{_bindir}/package-stash-conflicts


