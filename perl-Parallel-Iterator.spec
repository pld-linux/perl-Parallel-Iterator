#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Parallel
%define	pnam	Iterator
Summary:	Parallel::Iterator - Simple parallel execution
Name:		perl-Parallel-Iterator
Version:	1.00
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Parallel/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	879051d329ea79f59eb4b03bb0bf7c87
URL:		http://search.cpan.org/dist/Parallel-Iterator/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The map function applies a user supplied transformation function to
each element in a list, returning a new list containing the
transformed elements.

This module provides a 'parallel map'. Multiple worker processes are
forked so that many instances of the transformation function may be
executed simultaneously.

For time consuming operations, particularly operations that spend most
of their time waiting for I/O, this is a big performance win. It also
provides a simple idiom to make effective use of multi CPU systems.

There is, however, a considerable overhead associated with forking, so
the example in the synopsis (doubling a list of numbers) is not a
sensible use of this module.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT
./Build install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Parallel/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
