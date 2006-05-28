Summary:	Convert specified subversion xml logfile to GNU-style ChangeLog
Name:		svn2log
Version:	0.1
Release:	0.3
License:	BSD
Group:		Applications/Text
Source0:	http://nemerle.org/svn/nemerle/trunk/misc/svn2log.py
# Source0-md5:	3e27b3df04c5213811c82f42e27eb649
Patch0:		%{name}-xml.patch
Requires:	python-qp_xml
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert specified subversion xml logfile to GNU-style ChangeLog.

%prep
%setup -q -c -T
cp %{SOURCE0} %{name}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
