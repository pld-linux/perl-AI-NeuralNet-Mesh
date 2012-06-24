#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	AI
%define		pnam	NeuralNet-Mesh
Summary:	AI::NeuralNet::Mesh - an optimized, accurate neural network Mesh
Summary(pl.UTF-8):   AI::NeuralNet::Mesh - zoptymalizowana, dokładna sieć neuronowa Mesh
Name:		perl-AI-NeuralNet-Mesh
Version:	0.44
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.zip
# Source0-md5:	5d1c68c7d494da158ce50c263a7d77a1
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AI::NeuralNet::Mesh is an optimized, accurate neural network Mesh. It
was designed with accuracy and speed in mind.

This network model is very flexible. It will allow for classic binary
operation or any range of integer or floating-point inputs you care to
provide. With this you can change activation types on a per node or
per layer basis (you can even include your own anonymous subs as
activation types). You can add sigmoid transfer functions and control
the threshold. You can learn data sets in batch, and load CSV data set
files. You can do almost anything you need to with this module. This
code is designed to be flexible.

%description -l pl.UTF-8
AI::NeuralNet::Mesh to zoptymalizowana, dokładna sieć neuronowa Mesh.
Została zaprojektowana z myślą o dokładności i szybkości.

Model sieci jest bardzo elastyczny. Pozwala na klasyczne operacje
binarne oraz dowolny zakres wejść całkowitych lub zmiennoprzecinkowych
jaki tylko chcemy dostarczyć. Można zmienić czasy aktywacji dla węzłów
lub warstw (można nawet dołączyć własne anonimowe podsieci jako typy
aktywacji). Można dodawać funkcje transferu sigmoidalnego i kontrolę
progu. Można uczyć zbiorów danych wsadowo i wczytywać dane z plików
CSV. Można robić prawie wszystko co jest potrzebne. Kod jest
zaprojektowany tak, by był elastyczny.

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
