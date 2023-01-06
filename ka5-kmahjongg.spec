#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.12.1
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kmahjongg
Summary:	kmahjongg
Name:		ka5-%{kaname}
Version:	22.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	2b7e1da8738ed00e3dc9bd7f78837aa7
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel >= 5.8.0
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	ka5-libkmahjongg-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdeclarative-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-knewstuff-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	python
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In KMahjongg the tiles are scrambled and staked on top of each other
to resemble a certain shape. The player is then expected to remove all
the tiles off the game board by locating each tile's matching pair.

%description -l pl.UTF-8
W KMahjonggu kafelki są wymieszane i poukładane jeden na drugim tworząc
pewien kształt. Zadaniem gracza jest zdjąć wszystkie kafelki z planszy
znajdując pary.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/lt
%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmahjongg
%{_desktopdir}/org.kde.kmahjongg.desktop
%{_datadir}/config.kcfg/kmahjongg.kcfg
%{_iconsdir}/hicolor/128x128/apps/kmahjongg.png
%{_iconsdir}/hicolor/16x16/apps/kmahjongg.png
%{_iconsdir}/hicolor/22x22/apps/kmahjongg.png
%{_iconsdir}/hicolor/32x32/apps/kmahjongg.png
%{_iconsdir}/hicolor/48x48/apps/kmahjongg.png
%{_iconsdir}/hicolor/64x64/apps/kmahjongg.png
%{_iconsdir}/hicolor/scalable/apps/kmahjongg.svgz
%{_datadir}/kmahjongg
%{_datadir}/metainfo/org.kde.kmahjongg.appdata.xml
%{_datadir}/qlogging-categories5/kmahjongg.categories
