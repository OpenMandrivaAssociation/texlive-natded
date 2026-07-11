%global tl_name natded
%global tl_revision 32693

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Typeset natural deduction proofs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/natded
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/natded.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/natded.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides commands to typeset proofs in the style used by
Jaskowski, or that of Kalish and Montague.

