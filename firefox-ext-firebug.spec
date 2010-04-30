%define _mozillaextpath %{firefox_mozillapath}/extensions

Summary: Web development tool extension for firefox
Name: firefox-ext-firebug
Version: 1.5.3
Release: %mkrel 1
License: MPL
Group:	Networking/WWW
URL:	https://addons.mozilla.org/en-US/firefox/addon/1843
Source: http://www.gtlib.gatech.edu/pub/mozilla.org/addons/1843/firebug-%{version}-fx.xpi
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires:	mozilla-firefox => %{firefox_epoch}:%{firefox_version}
BuildRequires:	firefox-devel

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
mkdir -p %{buildroot}%{_mozillaextpath}

hash="$(sed -n '/.*em:id="\(.*\)"/{s//\1/p;q}' install.rdf)"
if [ -z "$hash" ]; then
    hash="$(sed -n '/.*em:id>\(.*\)<\/em:id>.*/{s//\1/p;q}' install.rdf)"
fi
if [ -z "$hash" ]; then
    echo "Failed to find plugin hash."
    exit 1
fi
extdir="%{_mozillaextpath}/$hash"
mkdir -p "%{buildroot}$extdir"
cp -af * "%{buildroot}$extdir/"

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%dir %firefox_mozillapath
%{_mozillaextpath}
