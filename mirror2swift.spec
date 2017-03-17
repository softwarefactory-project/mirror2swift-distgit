%global         commit 7effa8e8bd6cc4a7739e0d1ffb90c7349fdd5533

Name:           mirror2swift
Version:        0.1
Release:        1.20160818git7effa8e%{?dist}
Summary:        Tool to mirror a HTTP site to OpenStack Swift

License:        ASL 2.0
URL:            https://github.com/cschwede/mirror2swift
Source0:        https://github.com/cschwede/mirror2swift/archive/%{commit}.tar.gz

Patch0:         0001-Always-try-to-gunzip-repodata.patch

BuildArch:      noarch

Requires:       python-lxml
Requires:       PyYAML
Requires:       python2-requests

BuildRequires:  python2-devel
BuildRequires:  python-setuptools


%description
Tool to mirror a HTTP site to OpenStack Swift.


%prep
%autosetup -n %{name}-%{commit} -p1
rm requirements.txt test-requirements.txt


%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%files
%{_bindir}/mirror2swift
%{python2_sitelib}/mirror2swift
%{python2_sitelib}/mirror2swift-*.egg-info


%changelog
* Fri Mar 17 2017 Tristan Cacqueray - 0.1-1
- Initial packaging
