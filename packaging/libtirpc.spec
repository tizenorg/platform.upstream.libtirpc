Name:           libtirpc
License:        BSD-4-Clause
Group:          System/Libraries
Version:        0.2.2
Release:        0
Summary:        Transport Independent RPC Library
#BuildRequires:  libgssglue-devel
BuildRequires:  libtool
BuildRequires:  pkg-config
Url:            http://sourceforge.net/projects/libtirpc/
Source:         %{name}-%{version}.tar.bz2
Source100:        baselibs.conf

%description
The Transport Independent RPC library (TI-RPC) is a replacement for the
standard SunRPC library in glibc which does not support IPv6 addresses.
This implementation allows the support of other transports than UDP and
TCP over IPv4


%package devel
License:        BSD-4-Clause
Summary:        Transport Independent RPC Library
Group:          Development/Libraries/C and C++
Requires:       libtirpc = %{version} 
Requires:       glibc-devel

%description devel
The Transport Independent RPC library (TI-RPC) is a replacement for the
standard SunRPC library in glibc which does not support IPv6 addresses.
This implementation allows the support of other transports than UDP and
TCP over IPv4

%prep
%setup -q

%build
autoreconf -fiv
%configure --disable-static --with-pic --libdir=/%{_lib} 
%{__make} %{?_smp_mflags}

%install
%make_install
mkdir -p $RPM_BUILD_ROOT%{_libdir}
%{__ln_s} -v /%{_lib}/$(readlink %{buildroot}/%{_lib}/%{name}.so) %{buildroot}%{_libdir}/%{name}.so
mv -v $RPM_BUILD_ROOT/%{_lib}/pkgconfig $RPM_BUILD_ROOT/%{_libdir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files 
%defattr(-,root,root)
%config %{_sysconfdir}/netconfig
/%{_lib}/libtirpc.so.1*

%files devel
%defattr(-,root,root)
%{_libdir}/libtirpc.so
%dir /usr/include/tirpc/
/usr/include/tirpc/*
/usr/%{_lib}/pkgconfig/*

%docs_package

%changelog
