Name:		b43-openfwwf
Version:	5.2
Release:	10%{?dist}
Summary:	Open firmware for some Broadcom 43xx series WLAN chips
Group:		System Environment/Kernel
License:	GPLv2
URL:		http://www.ing.unibs.it/openfwwf/
Source0:	http://www.ing.unibs.it/openfwwf/firmware/openfwwf-%{version}.tar.gz
Source1:	README.openfwwf
Source2:	openfwwf.conf
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch
BuildRequires:	b43-tools
Requires:	udev
Requires:	module-init-tools


%description
Open firmware for some Broadcom 43xx series WLAN chips.
Currently supported models are 4306, 4311(rev1), 4318 and 4320.


%prep
%setup -q -n openfwwf-%{version}
sed -i s/"-o 0 -g 0"// Makefile
install -p -m 0644 %{SOURCE1} .
install -p -m 0644 %{SOURCE2} .

%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=$RPM_BUILD_ROOT/lib/firmware/b43-open
install -p -D -m 0644 openfwwf.conf $RPM_BUILD_ROOT%{_sysconfdir}/modprobe.d/openfwwf.conf



%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING LICENSE README.openfwwf
%dir /lib/firmware/b43-open
/lib/firmware/b43-open/b0g0bsinitvals5.fw
/lib/firmware/b43-open/b0g0initvals5.fw
/lib/firmware/b43-open/ucode5.fw
%{_sysconfdir}/modprobe.d/openfwwf.conf


%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 11 2010 Peter Lemenkov <lemenkov@gmail.com> 5.2-5
- Changed directory for storing firmware (rhbz #651350)

* Tue Mar 16 2010 John W. Linville <linville@redhat.com> 5.2-4
- Remove erroneous copyright notice from README.openfwwf

* Wed Jan 27 2010 Peter Lemenkov <lemenkov@gmail.com> 5.2-3
- Fixed typo in summary.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Peter Lemenkov <lemenkov@gmail.com> 5.2-1
- Ver. 5.2

* Mon Jun 29 2009 Peter Lemenkov <lemenkov@gmail.com> 5.1-3
- Changed README a lot
- Changed description

* Fri Jun  5 2009 Peter Lemenkov <lemenkov@gmail.com> 5.1-2
- Added config-file for modprobe

* Wed Mar 18 2009 Peter Lemenkov <lemenkov@gmail.com> 5.1-1
- Initial package for Fedora

