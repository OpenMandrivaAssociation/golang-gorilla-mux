%define prerelease 9ede152210fa25c1377d33e867cb828c19316445
%define import_path github.com/gorilla/mux
%define gosrc %{go_dir}/src/pkg/%{import_path}
%define shortcommit %(c=%{prerelease}; echo ${c:0:7})

Summary:	A powerful URL router and dispatcher for golang
Name:		golang-gorilla-mux
Version:	0.1.git%{shortcommit}
Release:	3
License:	BSD
Group:		Development/Other
Url:		https://%{import_path}
Source0:        https://%{import_path}/archive/%{prerelease}.tar.gz
Provides:       golang(%{import_path}) = %{version}-%{release}
BuildArch:	noarch
BuildRequires:	golang

%description
Package gorilla/mux implements a request router and dispatcher.

The name mux stands for "HTTP request multiplexer". Like the standard
http.ServeMux, mux.Router matches incoming requests against a list of
registered routes and calls a handler for the route that matches the URL or
other conditions.

%prep
%setup -q -n mux-%{prerelease}

%build

%install
mkdir -p %{buildroot}%{gosrc}
cp -av * %{buildroot}%{gosrc}/
rm -f %{buildroot}%{gosrc}/{LICENSE,README.md}

%files
%doc LICENSE README.md
%{gosrc}/*
