Summary:	SETI@home screensaver for KDE
Summary(pl):	Wygaszacz ekranu SETI@home dla KDE
Name:		ksetisaver
Version:	0.2.7
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.frozenlight.de/content/ksetisaver/ksetisaver-0.2.7.tar.gz
URL:		http://www.frozenlight.de
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.0
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define         _htmldir        /usr/share/doc/kde/HTML

%description
SETI@home screensaver for KDE.

%description -l pl
Wygaszacz ekranu SETI@home dla KDE.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"

%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang ksetisaver

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/System/ScreenSavers/*
%{_datadir}/apps/*
#%{_pixmapsdir}/*/*/*/*
%lang(de) %{_datadir}/locale/de
%lang(fr) %{_datadir}/locale/fr
