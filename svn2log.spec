Summary:	Convert specified subversion xml logfile to GNU-style ChangeLog
Name:		svn2log
Version:	0.1
Release:	0.1
License:	BSD
Group:		Applications/Text
Source0:	http://svn.digium.com/view/repotools/%{name}
# Source0-md5:	d9cf6dd67691648f935ce0dabbf24c50
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert specified subversion xml logfile to GNU-style ChangeLog.

%prep
%setup -q -c -T
cp %{SOURCE0} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
