#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	AI
%define	pnam	NeuralNet-Mesh
Summary:	AI::NeuralNet::Mesh - an optimized, accurate neural network Mesh
Summary(pl):	AI::NeuralNet::Mesh - zoptymalizowana, dok³adna sieæ neuronowa Mesh
Name:		perl-%{pdir}-%{pnam}
Version:	0.44
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.zip
# Source0-md5:	5d1c68c7d494da158ce50c263a7d77a1
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AI::NeuralNet::Mesh is an optimized, accurate neural network Mesh.
It was designed with accuracy and speed in mind.

This network model is very flexible.  It will allow for classic binary
operation or any range of integer or floating-point inputs you care
to provide.  With this you can change activation types on a per node
or per layer basis (you can even include your own anonymous subs as
activation types).  You can add sigmoid transfer functions and control
the threshold.  You can learn data sets in batch, and load CSV data
set files.  You can do almost anything you need to with this module.
This code is designed to be flexible.

%description -l pl
AI::NeuralNet::Mesh to zoptymalizowana, dok³adna sieæ neuronowa Mesh.
Zosta³a zaprojektowana z my¶l± o dok³adno¶ci i szybko¶ci.

Model sieci jest bardzo elastyczny. Pozwala na klasyczne operacje
binarne oraz dowolny zakres wej¶æ ca³kowitych lub zmiennoprzecinkowych
jaki tylko chcemy dostarczyæ. Mo¿na zmieniæ czasy aktywacji dla wêz³ów
lub warstw (mo¿na nawet do³±czyæ w³asne anonimowe podsieci jako typy
aktywacji). Mo¿na dodawaæ funkcje transferu sigmoidalnego i kontrolê
progu. Mo¿na uczyæ zbiorów danych wsadowo i wczytywaæ dane z plików
CSV. Mo¿na robiæ prawie wszystko co jest potrzebne. Kod jest
zaprojektowany tak, by by³ elastyczny.

%prep
%setup -q -c

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes *.htm README
%{perl_vendorlib}/AI/NeuralNet/*.pm
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_examplesdir}/%{name}-%{version}/*.mesh
%{_examplesdir}/%{name}-%{version}/*.txt
%{_examplesdir}/%{name}-%{version}/*.dat
%{_examplesdir}/%{name}-%{version}/*.pcx
%{_mandir}/man3/*
