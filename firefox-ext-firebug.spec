%define pre X.0b3

Summary: Web development tool extension for firefox
Name: firefox-ext-firebug
Version: 1.7
Release: %mkrel 0.%pre.2
License: MPL
Group:	Networking/WWW
URL:	https://addons.mozilla.org/en-US/firefox/addon/1843
#Source: http://www.gtlib.gatech.edu/pub/mozilla.org/addons/1843/firebug-%{version}-fx.xpi
Source: http://getfirebug.com/releases/firebug/1.7X/firebug-%{version}%{pre}.xpi
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires:	mozilla-firefox => %{firefox_version}
BuildRequires:	firefox-devel
Buildarch: noarch

%description
The most popular and powerful web development tool

    * Inspect HTML and modify style and layout in real-time
    * Use the most advanced JavaScript debugger available for any browser
    * Accurately analyze network usage and performance
    * Extend Firebug and add features to make Firebug even more powerful
    * Get the information you need to get it done with Firebug.


%prep
%setup -q -c -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{firefox_extdir}

hash="$(sed -n '/.*em:id="\(.*\)"/{s//\1/p;q}' install.rdf)"
if [ -z "$hash" ]; then
    hash="$(sed -n '/.*em:id>\(.*\)<\/em:id>.*/{s//\1/p;q}' install.rdf)"
fi
if [ -z "$hash" ]; then
    echo "Failed to find plugin hash."
    exit 1
fi
extdir="%{firefox_extdir}/"
mkdir -p "%{buildroot}$extdir"
cp -af %SOURCE0 "%{buildroot}$extdir/$hash.xpi"


%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%{firefox_extdir}



%changelog
* Sat Mar 19 2011 Funda Wang <fwang@mandriva.org> 1.7-0.X.0b3.1mdv2011.0
+ Revision: 646523
- 1.7.X.0b3

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 1.7-0.X.0a11.2
+ Revision: 640433
- rebuild to obsolete old packages

* Wed Feb 16 2011 Thierry Vignaud <tv@mandriva.org> 1.7-0.X.0a11.1
+ Revision: 638078
- new prerelease

* Tue Feb 15 2011 Thierry Vignaud <tv@mandriva.org> 1.7-0.X.0a10.1
+ Revision: 637877
- new prerelease

* Wed Jan 26 2011 Thierry Vignaud <tv@mandriva.org> 1.7-0.X.0a9.1
+ Revision: 632900
- new release

* Wed Jan 19 2011 Thierry Vignaud <tv@mandriva.org> 1.7-0.X.0a8.1
+ Revision: 631666
- new version
- prevent need to rebuild for every new firefox
 (package only .xpi still doesn't work)
- only package .xpi

* Wed Jan 05 2011 Thierry Vignaud <tv@mandriva.org> 1.7-0.X.0a7.1mdv2011.0
+ Revision: 628864
- rebuild for new firefox

* Tue Nov 30 2010 Thierry Vignaud <tv@mandriva.org> 1.7-0.X.0a7mdv2011.0
+ Revision: 604013
- new release
  firebug-1.6.0-fx.xpi
  firebug-1.7X.0a7.xpi

* Tue Nov 30 2010 Thierry Vignaud <tv@mandriva.org> 1.6.0-0.0mdv2011.0
+ Revision: 603235
- new release

* Wed Nov 17 2010 Thierry Vignaud <tv@mandriva.org> 1.6-0.X.0b4mdv2011.0
+ Revision: 598388
- 1.6X.0b4

* Mon Nov 15 2010 Thierry Vignaud <tv@mandriva.org> 1.6-0.X.0b3mdv2011.0
+ Revision: 597634
- switch to 1.6x branch (which is compatible with firefox4)

* Sun Nov 14 2010 Thierry Vignaud <tv@mandriva.org> 1.5.4-4mdv2011.0
+ Revision: 597379
- rebuild for new firefox

* Tue Jul 27 2010 Funda Wang <fwang@mandriva.org> 1.5.4-3mdv2011.0
+ Revision: 561160
- rebuild for ff 3.6.8

* Mon Jun 28 2010 Frederic Crozat <fcrozat@mandriva.com> 1.5.4-2mdv2010.1
+ Revision: 549365
- rebuild with FF 3.6.6

  + Funda Wang <fwang@mandriva.org>
    - New version 1.5.4

* Fri Apr 30 2010 Thierry Vignaud <tv@mandriva.org> 1.5.3-1mdv2010.1
+ Revision: 541247
- import firefox-ext-firebug


* Fri Apr 30 2010 Thierry Vignaud <tvignaud@mandriva.com> 1.5.3-1mdv2010.1
- initial release

