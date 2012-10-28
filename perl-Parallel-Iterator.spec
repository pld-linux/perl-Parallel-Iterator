#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Parallel
%define	pnam	Iterator
Summary:	Parallel::Iterator - Simple parallel execution
Summary(pl.UTF-8):	Parallel::Iterator - proste zrównoleglenie wykonywania
Name:		perl-Parallel-Iterator
Version:	1.00
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Parallel/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	879051d329ea79f59eb4b03bb0bf7c87
URL:		http://search.cpan.org/dist/Parallel-Iterator/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-dirs >= 2.1-19
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

%description -l pl.UTF-8
Funkcja map wykonuje zadane przez użytkownika przekształcenie na
każdym elemencie listy, zwracając nową listę zawierającą
przekształcone elementy.

Ten moduł udostępnia równogległą wersję tej funkcji. Uruchamiane jest
wiele procesów, co pozwala na jednoczesne wykonywanie wielu instancji
funkcji przekształcenia.

Dla czasochłonnych operacji, w szczególności takich, przy których
większość to oczekiwanie na we/wy, daje to duży zysk wydajnościowy.
Moduł także udostępnia prosty idiom, pozwalający efektywnie
wykorzystać systemy wieloprocesorowe.

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
%{perl_vendorlib}/Parallel/Iterator.pm
%{_mandir}/man3/Parallel::Iterator.3pm*
%{_examplesdir}/%{name}-%{version}
