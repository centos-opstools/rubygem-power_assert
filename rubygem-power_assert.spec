# Generated from power_assert-0.3.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name power_assert

Name: rubygem-%{gem_name}
Version: 0.3.1
Release: 1%{?dist}
Summary: Power Assert for Ruby
Group: Development/Languages
License: 2-clause BSDL and Ruby's
URL: https://github.com/k-tsj/power_assert
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
# the following BuildRequires are development dependencies
# BuildRequires: rubygem(test-unit)
# BuildRequires: rubygem(simplecov)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Power Assert for Ruby. Power Assert shows each value of variables and method
calls in the expression. It is useful for testing, providing which value
wasn't correct when the condition is not satisfied.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/




# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%{gem_instdir}/BSDL
%license %{gem_instdir}/COPYING
%{gem_instdir}/LEGAL
%{gem_instdir}/benchmarks
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/power_assert.gemspec
%{gem_instdir}/test

%changelog
* Wed Sep 21 2016 Rich Megginson <rmeggins@redhat.com> - 0.3.1-1
- Initial package
