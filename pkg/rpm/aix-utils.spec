Name:           aix-utils
Version:        1.0
Release:        0%{?dist}
Summary:        Various utilities to aid in AIX monitoring and management

BuildRoot:      %{buildroot}
Group:          Applications/Productivity
License:        GPLv3+
URL:            https://github.com/absperf/%{name}
Source:         %{name}-%{version}.tar.gz
BuildRequires:  json-c
Requires:       json-c

%description
Set of utility programs for AIX management

%prep
%setup -q

%build
gmake CC=gcc

%install
gmake install PREFIX=%{buildroot}/opt/freeware

%files
%defattr(0755, root, bin)
%{_bindir}/psjson
%{_bindir}/errptjson

%changelog
* Wed Mar 16 2016 Taylor C. Richberger <tcr@absolute-performance.com> 1.0-0
- Initial RPM writing
