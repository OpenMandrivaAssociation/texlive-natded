Name:		texlive-natded
Version:	32693
Release:	1
Summary:	Typeset natural deduction proofs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/natded
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/natded.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/natded.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides commands to typeset proofs in the style
used by Jaskowski, or that of Kalish and Montague.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/natded/natded.sty
%doc %{_texmfdistdir}/doc/latex/natded/README.md
%doc %{_texmfdistdir}/doc/latex/natded/extended_doc.pdf
%doc %{_texmfdistdir}/doc/latex/natded/extended_doc.tex
%doc %{_texmfdistdir}/doc/latex/natded/natded.pdf
%doc %{_texmfdistdir}/doc/latex/natded/natded.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
