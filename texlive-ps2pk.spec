Name:		texlive-ps2pk
Version:	52851
Release:	1
Summary:	Generate a PK font from an Adobe Type 1 font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ps2pk
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ps2pk.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ps2pk.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Generates a PK file from an Adobe Type 1 font. PK fonts are (or
used to be) valuable in enabling previewers to view documents
generated that use Type 1 fonts. The program makes use of code
donated to the X consortium by IBM.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/ps2pk.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/ps2pk.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/pk2bm.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/pk2bm.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/pfb2pfa.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/pfb2pfa.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/mag.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/mag.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
