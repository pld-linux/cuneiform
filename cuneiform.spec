Summary:	OCR system
Name:		cuneiform
Version:	1.1.0
Release:	2
License:	BSD
Group:		Applications/Graphics
Source0:	http://launchpad.net/cuneiform-linux/1.1/1.1/+download/%{name}-linux-%{version}.tar.bz2
# Source0-md5:	09fd160cdfc512f26442a7e91246598d
Patch0:		%{name}-libm.patch
URL:		https://launchpad.net/cuneiform-linux
BuildRequires:	ImageMagick-c++-devel
BuildRequires:	cmake
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OCR system originally developed and open sourced by
Cognitive technologies.

%prep
%setup -q -n %{name}-linux-%{version}
%patch0 -p1

%build
rm -f builddir/CMakeCache.txt
%{__mkdir_p} builddir
cd builddir
export CFLAGS="%{rpmcflags}"
export CXXFLAGS="%{rpmcflags}"
%{__cmake} .. \
	-DCMAKE_INSTALL_PREFIX="%{_prefix}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C builddir install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT{%{_includedir},%{_libdir}/lib*.so}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc issues.txt original\ russian\ readme.rtf readme.txt
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/lib*.so.0
%{_datadir}/%{name}
