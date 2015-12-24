#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	Patricia
Summary:	Net::Patricia - Patricia Trie Perl module for fast IP address lookups
Summary(pl.UTF-8):	Net::Patricia - moduł Perla Patricia Trie do szybkiego wyszukiwania adresów IP
Name:		perl-Net-Patricia
Version:	1.22
Release:	4
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/G/GR/GRUBER/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ef838f7512b050ca4b35d742f9565b3b
URL:		http://search.cpan.org/dist/Net-Patricia/
BuildRequires:	perl-Net-CIDR-Lite
BuildRequires:	perl-Socket6
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module uses a Patricia Trie data structure to quickly perform IP
address prefix matching for applications such as IP subnet, network or
routing table lookups.

The data structure is based on a radix tree using a radix of two,
so sometimes you see patricia implementations called "radix" as well.
The term "Trie" is derived from the word "retrieval" but is pronounced
like "try".  Patricia stands for "Practical Algorithm to Retrieve
Information Coded as Alphanumeric", and was first suggested for
routing table lookups by Van Jacobsen. Patricia Trie performance
characteristics are well-known as it has been employed for routing
table lookups within the BSD kernel since the 4.3 Reno release.

%description -l pl.UTF-8
Ten moduł używa struktury danych Patricia Trie do wykonywania
szybkiego dopasowywania prefiksów IP dla zastosowań takich jak
przeszukiwanie podsieci IP, sieci czy tabel routingu.

Struktura danych jest oparta na drzewie radix przy podstawie
wynoszącej 2 - implementacje patricia czasem są nazywane także radix.
Termin "Trie" pochodzi od słowa "retrieval" (odczytywanie), ale jest
wymawiany jak "try". Patricia to skrót od "Practical Algorithm to
Retrieve Information Coded as Alphanumeric" (praktyczny algorytm
odczytywania informacji zakodowanych alfanumerycznie) i jako
pierwszy zaproponowany do przeszukiwania tabel routingu przez Van
Jacobsena. Charakterystyki wydajności Patricia Trie są dobrze znane,
jako że struktura ta jest wykorzystywana przy przeszukiwaniu tabel
routingu w jądrze BSD od wersji 4.3 Reno.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Net/*.pm
%dir %{perl_vendorarch}/auto/Net/Patricia
%attr(755,root,root) %{perl_vendorarch}/auto/Net/Patricia/Patricia.so
%{_mandir}/man3/*
