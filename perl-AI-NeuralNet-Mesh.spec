%include	/usr/lib/rpm/macros.perl
%define	pdir	AI
%define	pnam	NeuralNet-Mesh
Summary:	AI::NeuralNet::Mesh - An optimized, accurate neural network Mesh
Summary(pl):	AI::NeuralNet::Mesh - zoptymalizowana, dok�adna sie� neuronowa Mesh
Name:		perl-%{pdir}-%{pnam}
Version:	0.44
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.zip
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
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
AI::NeuralNet::Mesh to zoptymalizowana, dok�adna sie� neuronowa Mesh.
Zosta�a zaprojektowana z my�l� o dok�adno�ci i szybko�ci.

Model sieci jest bardzo elastyczny. Pozwala na klasyczne operacje
binarne oraz dowolny zakres wej�� ca�kowitych lub zmiennoprzecinkowych
jaki tylko chcemy dostarczy�. Mo�na zmieni� czasy aktywacji dla w�z��w
lub warstw (mo�na nawet do��czy� w�asne anonimowe podsieci jako typy
aktywacji). Mo�na dodawa� funkcje transferu sigmoidalnego i kontrol�
progu. Mo�na uczy� zbior�w danych wsadowo i wczytywa� dane z plik�w
CSV. Mo�na robi� prawie wszystko co jest potrzebne. Kod jest
zaprojektowany tak, by by� elastyczny.

%prep
%setup -q -n %{name}-%{version} -c

%build
%{__perl} Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/AI/NeuralNet/*.pm
%doc Changes *.htm README
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_examplesdir}/%{name}-%{version}/*.mesh
%{_examplesdir}/%{name}-%{version}/*.txt
%{_examplesdir}/%{name}-%{version}/*.dat
%{_examplesdir}/%{name}-%{version}/*.pcx
%{_mandir}/man3/*
