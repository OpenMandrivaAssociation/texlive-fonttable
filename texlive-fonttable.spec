# revision 21399
# category Package
# catalog-ctan /macros/latex/contrib/fonttable
# catalog-date 2009-10-20 21:39:17 +0200
# catalog-license lppl1.3
# catalog-version 1.6
Name:		texlive-fonttable
Version:	1.6
Release:	1
Summary:	Print font tables from a LaTeX document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fonttable
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fonttable.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fonttable.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fonttable.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This is a package version of nfssfont.tex (part of the LaTeX
distribution); it enables you to print a table of the
characters of a font and/or some text (for demonstration or
testing purposes), from within a document. (Packages such as
testfont and nfssfont.tex provide these facilities, but they
run as interactive programs: the user is expected to type
details of what is needed.) Note that the package mftinc also
has a \fonttable function; the documentation explains how avoid
a clash with that package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fonttable/fonttable.sty
%doc %{_texmfdistdir}/doc/latex/fonttable/README
%doc %{_texmfdistdir}/doc/latex/fonttable/fonttable.pdf
#- source
%doc %{_texmfdistdir}/source/latex/fonttable/fonttable.dtx
%doc %{_texmfdistdir}/source/latex/fonttable/fonttable.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
