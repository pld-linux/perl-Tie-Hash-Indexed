#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	Hash-Indexed
Summary:	Tie::Hash::Indexed - Ordered hashes for Perl
Summary(pl):	Tie::Hash::Indexed - uporz±dkowane hasze dla Perla
Name:		perl-Tie-Hash-Indexed
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	dd2436cfd7cf378c5e685baf24b4402b
URL:		http://search.cpan.org/dist/Tie-Hash-Indexed/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie::Hash::Indexed is very similar to Tie::IxHash. However, it is
written completely in XS and usually about twice as fast as
Tie::IxHash. It's quite a lot faster when it comes to clearing or
deleting entries from large hashes. Currently, only the plain tying
mechanism is supported.

%description -l pl
Tie::Hash::Indexed jest bardzo podobny do Tie::IxHash. Jednak jest
napisany w ca³o¶ci w XS i zwykle oko³o dwa razy szybszy ni¿
Tie::IxHash. Jest du¿o szybszy, je¶li zachodzi potrzeba czyszczenia
lub usuwania wpisów z du¿ych haszy. Aktualnie obs³ugiwany jest tylko
zwyk³y mechamizm wi±zania.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
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
%doc Changes README TODO
%{perl_vendorarch}/Tie/Hash/*.pm
%dir %{perl_vendorarch}/auto/Tie/Hash/Indexed
%{perl_vendorarch}/auto/Tie/Hash/Indexed/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Tie/Hash/Indexed/*.so
%{_mandir}/man3/*
