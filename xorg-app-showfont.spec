Summary:	showfont application - font dumper for X font server
Summary(pl.UTF-8):	Aplikacja showfont do wypisywania szczegółów fontów z serwera fontów X
Name:		xorg-app-showfont
Version:	1.0.7
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/showfont-%{version}.tar.xz
# Source0-md5:	37d58a267bc874746f1be885a0d4ab17
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libFS-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
showfont displays data about a font that matches the given pattern.
The information shown includes font information, font properties,
character metrics, and character bitmaps.

%description -l pl.UTF-8
showfont wyświetla dane o foncie pasującym do zadanego wzorca.
Informacje obejmują informacje o foncie, właściwości fontu, metryki
znaków i bitmapy znaków.

%prep
%setup -q -n showfont-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/showfont
%{_mandir}/man1/showfont.1*
