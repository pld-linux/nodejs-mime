%define		pkg	mime
Summary:	A comprehensive library for mime-type mapping
Name:		nodejs-%{pkg}
Version:	1.2.11
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	a96a25013bf4693868ceb6d75983174d
URL:		https://github.com/broofa/node-mime
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Comprehensive MIME type mapping API. Includes all 600+ types and 800+
extensions defined by the Apache project, plus additional types
submitted by the node.js community.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -pr types %{pkg}.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/%{pkg}
