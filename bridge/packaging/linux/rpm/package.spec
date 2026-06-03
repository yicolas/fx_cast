%global __os_install_post %{nil}
%define _source_payload w7.lzdio
%define _binary_payload w7.lzdio

Name: {{packageName}}
Summary: {{applicationName}}
Version: {{applicationVersion}}
Release: 1
License: MIT
Requires: avahi, avahi-compat-libdns_sd, nss-mdns

%description
{{applicationName}}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{{{executablePath}}}
{{#manifestPaths}}
mkdir -p $RPM_BUILD_ROOT/{{{manifestPath}}}
{{/manifestPaths}}

cp %{_distdir}/{{{executableName}}} $RPM_BUILD_ROOT/{{{executablePath}}}
cp %{_distdir}/{{{bindingName}}} $RPM_BUILD_ROOT/{{{executablePath}}}
{{#manifestPaths}}
cp %{_distdir}/{{{manifestName}}} $RPM_BUILD_ROOT/{{{manifestPath}}}
{{/manifestPaths}}

%files
{{{executablePath}}}/{{{executableName}}}
{{{executablePath}}}/{{{bindingName}}}
{{#manifestPaths}}
{{{manifestPath}}}/{{{manifestName}}}
{{/manifestPaths}}
