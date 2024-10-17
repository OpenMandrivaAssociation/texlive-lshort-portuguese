Name:		texlive-lshort-portuguese
Version:	55643
Release:	2
Summary:	Introduction to LaTeX in Portuguese
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/lshort/portuguese
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-portuguese.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-portuguese.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This is the Portuguese translation of A Short Introduction to
LaTeX2e.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-portuguese/pt-lshort-5.01.0.src.tar.gz
%doc %{_texmfdistdir}/doc/latex/lshort-portuguese/pt-lshort.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
