Summary:	SETI@home screensaver for KDE
Summary(pl.UTF-8):   Wygaszacz ekranu SETI@home dla KDE
Name:		ksetisaver
Version:	0.3.4
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://www.frozenlight.de/content/ksetisaver/%{name}-%{version}.tar.gz
# Source0-md5:	2efb42aebea56b8a1fa55f37604e149f
URL:		http://www.frozenlight.de/
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.0.3
Requires:	kdebase-screensavers
Requires:	setiathome
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _htmldir        /usr/share/doc/kde/HTML

%description
SETI@home screensaver for KDE.

%description -l pl.UTF-8
Wygaszacz ekranu SETI@home dla KDE.

%prep
%setup -q

mv -f po/{zh_CN.GB2312,zh_CN}.po
mv -f po/{zh_CN.GB2312,zh_CN}.gmo

%{__perl} -pi -e 's/zh_CN\.GB2312/zh_CN/g' po/Makefile.in
%{__perl} -pi -e 's/\[zh_CN\.GB2312\]/\[zh_CN\]/;s/\[no\]/\[nb\]/;s/\[no_NY\]/\[nn\]/' \
	ksetisaver/ksetisaver.desktop

%build
cp -f /usr/share/automake/config.* admin
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_appsdir="%{_applnkdir}"; export kde_appsdir
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/apps/kscreensaver
mv $RPM_BUILD_ROOT%{_applnkdir}/System/ScreenSavers/* $RPM_BUILD_ROOT%{_datadir}/apps/kscreensaver

%find_lang ksetisaver --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f ksetisaver.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/ksetisaver
%{_datadir}/apps/kscreensaver/*.desktop
