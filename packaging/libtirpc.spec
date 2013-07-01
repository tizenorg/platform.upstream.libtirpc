#

Name:           libtirpc
Version:        0.2.2
Release:        0
License:        BSD-4-Clause
Summary:        Transport Independent RPC Library
Url:            http://sourceforge.net/projects/libtirpc/
Group:          System/Libraries
Source:         %{name}-%{version}.tar.bz2
Source100:      baselibs.conf
Source1001: 	libtirpc.manifest
BuildRequires:  libtool
BuildRequires:  pkgconfig(pkg-config)

%description
The Transport Independent RPC library (TI-RPC) is a replacement for the
standard SunRPC library in glibc which does not support IPv6 addresses.
This implementation allows the support of other transports than UDP and
TCP over IPv4

%package devel
License:        BSD-4-Clause
Summary:        Transport Independent RPC Library
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libtirpc = %{version}

%description devel
The Transport Independent RPC library (TI-RPC) is a replacement for the
standard SunRPC library in glibc which does not support IPv6 addresses.
This implementation allows the support of other transports than UDP and
TCP over IPv4

%prep
%setup -q
cp %{SOURCE1001} .

%build
autoreconf -fiv
%configure --disable-static --with-pic --libdir=/%{_lib}
make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}%{_libdir}
ln -s -v /%{_lib}/$(readlink %{buildroot}/%{_lib}/%{name}.so) %{buildroot}%{_libdir}/%{name}.so
rm -rf %{buildroot}/%{_lib}/*.so
mv -v %{buildroot}/%{_lib}/pkgconfig %{buildroot}/%{_libdir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root)
%config %{_sysconfdir}/netconfig
/%{_lib}/libtirpc.so.1*

%files devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libtirpc.so
%dir %{_includedir}/tirpc/
%{_includedir}/tirpc/*
%{_libdir}/pkgconfig/*

%docs_package

%changelog
