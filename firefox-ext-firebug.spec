%define pre X.0a8

Summary: Web development tool extension for firefox
Name: firefox-ext-firebug
Version: 1.7
Release: %mkrel 0.%pre.1
License: MPL
Group:	Networking/WWW
URL:	https://addons.mozilla.org/en-US/firefox/addon/1843
#Source: http://www.gtlib.gatech.edu/pub/mozilla.org/addons/1843/firebug-%{version}-fx.xpi
Source: http://getfirebug.com/releases/firebug/1.7X/firebug-%{version}%{pre}.xpi
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires:	mozilla-firefox => %{firefox_epoch}:%{firefox_version}
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

