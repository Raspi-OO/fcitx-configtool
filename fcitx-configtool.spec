Name:		fcitx-configtool
Version:	0.4.10
Release:	1
Summary:	Gtk+-based configuring tools for Fcitx
License:	GPLv2+
URL:		https://github.com/fcitx/fcitx-configtool
Source0:	http://download.fcitx-im.org/fcitx-configtool/%{name}-%{version}.tar.xz

BuildRequires:	gcc
BuildRequires:	cmake, fcitx-devel, gettext, intltool, libxml2-devel
BuildRequires:	gtk2-devel, iso-codes-devel, libtool, unique-devel
BuildRequires:	gtk3-devel, unique3-devel
Requires:	fcitx


%description
fcitx-config-gtk and fcitx-config-gtk3 are Gtk based configuring tools for
Fcitx.


%prep
%setup -q -n %{name}-%{version}

%build
mkdir -pv build
pushd build
%cmake -DENABLE_GTK3=ON -DENABLE_GTK2=ON ..
make %{?_smp_mflags} VERBOSE=1

%install
pushd build
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
popd

%find_lang %{name}

%files -f %{name}.lang
%doc README
%license COPYING
%{_bindir}/*


%changelog
* Fri Sep 18 2020 Luke Yue <lukedyue@gmail.com> - 0.4.10-1
- Initial package
