# Created by pyp2rpm-3.3.3
%global pypi_name ufolib2

Name:           python-%{pypi_name}
Version:        0.5.1
Release:        1
Summary:        ufoLib2 is a UFO font processing library
Group:          Development/Python
License:        Apache 2.0
URL:            https://github.com/fonttools/ufoLib2
Source0:        https://files.pythonhosted.org/packages/source/u/%{pypi_name}/ufoLib2-%{version}.zip
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python3dist(attrs)
BuildRequires:  python3dist(fonttools)
BuildRequires:  python3dist(fs)
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(wheel)

%{?python_provide:%python_provide python-%{pypi_name}}

Requires:       python3dist(attrs)
Requires:       python3dist(fonttools)
Requires:       python3dist(lxml)

%description
ufoLib2 is a UFO font library.

%prep
%autosetup -n ufoLib2-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py_build

%install
%py_install

%files
%license LICENSE tests/data/LICENSE_UbuTestData.txt
%doc README.md
%{python_sitelib}/ufoLib2
%{python_sitelib}/ufoLib2-%{version}-py%{python_version}.egg-info
