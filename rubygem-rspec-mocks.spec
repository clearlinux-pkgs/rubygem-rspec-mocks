#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-rspec-mocks
Version  : 3.3.2
Release  : 9
URL      : https://rubygems.org/downloads/rspec-mocks-3.3.2.gem
Source0  : https://rubygems.org/downloads/rspec-mocks-3.3.2.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec-support
BuildRequires : rubygem-thread_order

%description
# RSpec Mocks [![Build Status](https://secure.travis-ci.org/rspec/rspec-mocks.svg?branch=master)](http://travis-ci.org/rspec/rspec-mocks) [![Code Climate](https://codeclimate.com/github/rspec/rspec-mocks.svg)](https://codeclimate.com/github/rspec/rspec-mocks)
rspec-mocks is a test-double framework for rspec with support for method stubs,
fakes, and message expectations on generated test-doubles and real objects
alike.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n rspec-mocks-3.3.2
gem spec %{SOURCE0} -l --ruby > rubygem-rspec-mocks.gemspec

%build
gem build rubygem-rspec-mocks.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
rspec-mocks-3.3.2.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/rspec-mocks-3.3.2.gem
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/.document
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/.yardopts
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/Changelog.md
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/License.txt
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/README.md
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/any_instance.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/any_instance/chain.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/any_instance/error_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/any_instance/expect_chain_chain.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/any_instance/expectation_chain.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/any_instance/message_chains.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/any_instance/proxy.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/any_instance/recorder.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/any_instance/stub_chain.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/any_instance/stub_chain_chain.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/argument_list_matcher.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/argument_matchers.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/configuration.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/error_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/example_methods.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/instance_method_stasher.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/marshal_extension.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/matchers/expectation_customization.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/matchers/have_received.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/matchers/receive.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/matchers/receive_message_chain.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/matchers/receive_messages.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/message_chain.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/message_expectation.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/method_double.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/method_reference.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/mutate_const.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/mutex.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/object_reference.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/order_group.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/proxy.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/reentrant_mutex.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/space.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/standalone.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/syntax.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/targets.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/test_double.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/verifying_double.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/verifying_message_expecation.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/verifying_proxy.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-mocks-3.3.2/lib/rspec/mocks/version.rb
/usr/lib64/ruby/gems/2.3.0/specifications/rspec-mocks-3.3.2.gemspec
