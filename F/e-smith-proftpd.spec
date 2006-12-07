Summary: e-smith specific proftpd configuration files and templates
%define name e-smith-proftpd
Name: %{name}
%define version 1.12.0
%define release 4
Version: %{version}
Release: %smerelease %{release}
Packager: %{_packager}
License: GPL
Vendor: Mitel Networks Corporation
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-proftpd-1.12.0-LogDirPerms.patch
Patch1: e-smith-proftpd-1.12.0-ftpusersfix.patch
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
BuildRequires: e-smith-devtools
Requires: e-smith-base >= 4.15.0-05, proftpd
Requires: e-smith-lib >= 1.15.1-33
Requires: iptables
AutoReqProv: no

%changelog
* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Thu Sep 21 2006 Gavin Weight <gweight@gmail.com> 1.12.0-03
- Expand /etc/ftpusers if user is locked/password reset. [SME: 1921]

* Tue Apr 18 2006 Gordon Rowell <gordonr@gormand.com.au> 1.12.0-02
- Force permissions on /var/log/proftpd in log/run script [SME: 1267]

* Thu Mar 16 2006 Charlie Brady <charlie_brady@mitel.com> 1.12.0-01
- Roll stable stream version. [SME: 1016]

* Tue Feb 28 2006 Charlie Brady <charlie_brady@mitel.com> 1.11.0-29
- Back out the chroot patch for now. [SME: 590]

* Fri Jan 27 2006 Shad L. Lords <slords@mail.com> 1.11.0-28
- Disable anonymous ibays if globally disabled.

* Fri Jan 27 2006 Shad L. Lords <slords@mail.com> 1.11.0-27
- Add chroot for users [SME: 590]
- Add ability to disable anonymous access [SME: 591]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 1.11.0-26
- Bump release number only

* Wed Oct 12 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-25]
- Filter out comments in peers files, to avoid log noise from
  tcpsvd. Fix name of peers/local templates.metadata file.
  [SF: 1324719]

* Wed Jul 27 2005 Shad Lords <slords@mail.com>
- [1.11.0-24]
- Move masq fragement from template to db [SF: 1241416]

* Tue Jun 14 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-23]
- Re-expand peers/{0,local} in remoteaccess-update, as permissions
  may have changed. [SF: 1220510]

* Tue Mar 29 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-22]
- Create empty template-begin template fragments for tcpsvd
  ACL files.

* Tue Mar 29 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-21]
- Don't use sigusr1 in bootstrap-console-save, as the service is not
  up, and sigusr1 will be ignored. Instead, call ./control/1 from run
  script.

* Wed Mar 23 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-20]
- Use sigusr1 in remoteaccess-update. This will generate the network ACL
  symlinks. 'adjust-services' implicitly starts any service which
  should be running.

* Wed Mar 16 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-19]
- Use tcpsvd in place of tcpserver. Manage network access lists
  using new esmith::tcpsvd library. Update e-smith-lib depenency.
- Add symlink /var/service/ftp -> proftpd.
- Add zero length template-begin files to peers/{0,local}, to avoid
  log noise from comment lines.

* Wed Mar 16 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-18]
- Add missing templates for peers/{0,local}.

* Wed Mar 16 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-17]
- Optimise template expansions versus events - only expand files
  which may have changed.

* Tue Mar 15 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-16]
- Fix service name in adjust-services symlink. [MN00065576]

* Sun Mar 13 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-15]
- Replace proftp-startstop action with call to 'adjust-services'.
  Update e-smith-lib version dependency. [MN00065576]
- Use generic_template_expand action in place of proftpd-conf.
  [MN00064130]
- Re-add missing restart patch to config.

* Thu Mar 10 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-14]
- Allow restarts of retreive and store. Patch from Shad. [MN00073802]
- Avoid duplicate Primary section in config. Patch from Shad. [MN00073804]

* Wed Feb  9 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-13]
- Remove migrate fragment for very old FTPServerMode property. [MN00065931]
- Clean BuildRequires. [charlieb MN00043055]

* Fri Sep  3 2004 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-12]
- Backout of user-create/delete addition. Wrong way to go.
  [msoulier MN00035806]

* Fri Sep  3 2004 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-11]
- Added proftpd-conf and startstop to user-create/delete.
  [msoulier MN00035806]

* Wed Aug  4 2004 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-10]
- Updated startstop to use esmith::util::serviceControl. [msoulier MN00031530]

* Mon Sep 22 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-09]
- Fixed network spec format. CIDR format expected. [msoulier 10069]

* Fri Sep  5 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-08]
- Fix c&p error in tcprules template fragment. [charlieb 9547]

* Fri Sep  5 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-07]
- Add requires for correct version of e-smith-base. [charlieb 9547]

* Fri Sep  5 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-06]
- Remove hosts.allow and xinetd.conf template fragments.
  [charlieb 9547]

* Fri Sep  5 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-05]
- Fix a couple of run time errors. [charlieb 9547]

* Fri Sep  5 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-04]
- Service directory and rc7.d symlinks must be called ftp, since that is
  the service record name. Use /etc/rc.d/init.d/supervise directory, to
  avoid potential clash with stock init script. [charlieb 9547,9930]

* Fri Sep  5 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-03]
- Use new createlinks library to reduce code. [charlieb 9809]

* Fri Sep  5 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-02]
- Run proftpd under supervise and tcpserver. [charlieb 9547]

* Fri Sep  5 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-01]
- Changing version to development stream number - 1.11.0

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [1.10.0-01]
- Changing version to stable stream number - 1.10.0

* Tue Apr 29 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-14]
- Modify xinetd.conf/30ftp to properly handle enabled/disabled/missing cases [gordonr 8609]

* Mon Apr 21 2003 Mark Knox <markk@e-smith.com>
- [1.9.0-13]
- Force 0640 on proftpd.conf [markk 8408]

* Tue Apr  8 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-12]
- Fix typo in path for anonymous login. [charlieb 5652]
- Remove selective binding to interfaces for now - it requires
  a full xinetd restart, which we don't do in remoteaccess-update.
  [charlieb 951]
- Change ScoreboardPath to ScoreboardFile - the former is deprecated
  (with extreme prejudice) in current proftpd. [charlieb 5411]

* Tue Apr  8 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-11]
- Add ScoreboardPath directive to config file templates [charlieb 5411]

* Tue Mar 18 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-10]
- Add config migration fragment to migrate old ftp access properties
  to new. [charlieb 7683]
- Change Copyright header to License. [charlieb]

* Thu Mar 13 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-09]
- Use LoginAccess property to control ftp login access - this replaces the
  "acccess" semantics of 5.5 and earlier. [charlieb 7466]
- Add back the special case for Primary i-bay, as it's needed for anonymous
  ftp.  [charlieb 5652]

* Fri Mar  7 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-08]
- esmith::utils::processTemplate => esmith::templates::processTemplate.
  [charlieb 7466]

* Thu Mar  6 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-07]
- Escape braces in logrotate.d template fragment [charlieb 6438]

* Thu Mar  6 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-06]
- Fix missed accessLimits => access change in ftp masq fragment [charlieb 7466]

* Thu Mar  6 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-05]
- Fix migrate fragment problem. [charlieb 1507]
- Remove legacy code from proftpd config templates, and simplify. [charlieb 7466]

* Mon Mar  3 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-04]
- Template /etc/logrotate.d/proftpd and remove postrotate sigHUP. [charlieb 6438]
- Add default config db fragments to set type/access/status [charlieb 1507]
- Replace migrate script in post-upgrade event with template fragment in
  db/configuration/migrate directory. [charlieb 1507]
- Use "access" rather than "accessLimits" to control access to ftp from
  outside LAN. [charlieb 7466]
- Bind to local interface only if access is private. [charlieb 951]

* Fri Feb 28 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-03]
- Re-do hosts.allow template to use esmith::ConfigDB::hosts_allow_spec.
  Add dependency on up-to-date e-smith-lib.
  TODO: fix accessLimits v access issue. [charlieb 5650]

* Wed Jan 29 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-02]
- Remove special cases for primary in proftpd.conf - primary
  is now a pre-defined i-bay. [charlieb 5652]

* Wed Jan 29 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-01]
- Rolling development stream to 1.9.0

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.8.0-01]
- Roll to maintained version number to 1.8.0

* Wed Oct  2 2002 Mark Knox <markk@e-smith.com>
- [1.7.3-05]
- Removed stray braces in get_all_by_prop [markk 3786]

* Mon Sep 23 2002 Mark Knox <markk@e-smith.com>
- [1.7.3-04]
- Fix proftpd.conf template breakage [markk 3786]

* Mon Sep 23 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.3-03]
- Fix hosts.allow template breakage [charlieb 3786]

* Thu Sep 19 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.3-02]
- Fix i-bay section of proftpd.conf [charlieb 4950]

* Thu Sep 12 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.3-01]
- Preparing for rebuild as-source, to get rid of some patch detritus - see
  bug 4825. [charlieb 4793]

* Thu Sep 12 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.2-05]
- Add missing 10LimitSiteChmod template fragment [charlieb 4793]

* Thu Sep 12 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.2-04]
- Replace deprecate AllowChmod with <Limit SITE_CHMOD>, which requires some
  fragment shuffling. Remove unnecessary template-{begin,end}, move
  10localAccess to 00localAccess. [charlieb 4793]

* Wed Sep 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.2-03]
- Fix esmith::Networks => esmith::NetworksDB snafu in /etc/proftpd.conf
  template. [charlieb 3786]

* Tue Sep 10 2002 Mark Knox <markk@e-smith.com>
- [1.7.2-02]
- Change use of allow_tcp_in() function to allow dynamic reconfig.
  [charlieb 4501]
- Remove deprecated split on pipe [markk 3786]

* Thu Aug  8 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.2-01]
- Remove 46AllowFTPActive masq template fragment, allow port 21 inbound
  access and allow netfilter connection tracking to do the rest of the
  job of FTP access control. [charlieb 4499]

* Wed Jul 17 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.1-01]
- Change masq script fragment to use iptables. [charlieb 1268]

* Wed Jun  5 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-01]
- Changing version to development stream number - 1.7.0

* Fri May 31 2002 Charlie Brady <charlieb@e-smith.com>
- [1.6.0-01]
- Changing version to maintained stream number to 1.6.0

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.5.5-01]
- RPM rebuild forced by cvsroot2rpm

* Fri May  3 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.4-01]
- Disable reverse DNS and ident lookups [charlieb 339]

* Fri May  3 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.3-01]
- Once more with feeling! (I missed one).

* Fri May  3 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.2-01]
- Fix createlinks problems with missing directories and $event scope.

* Fri May  3 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.1-01]
- Test build to verify CVS conversion.

* Fri May 3 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-01]
- rollRPM: Rolled version number to 1.5.0-01. Includes patches up to 1.4.0-08.

* Wed Dec 05 2001 Jason Miller <jmiller@e-smith.com>
- [1.4.0-08]
- Fix 45AllowFTP masq template to handle case where status=disabled

* Fri Nov 16 2001 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-07]
- Be sure to regenerate /etc/ftpusers during password-modify event, to allow
  access to password protected i-bays.
- Remove proftpd-conf actions from post-install and post-upgrade events -
  bootstrap-console-save is sufficient.

* Thu Nov 08 2001 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-06]
- Fix xinetd.conf template fragment so that status=disabled is honoured.

* Mon Oct 22 2001 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-05]
- Add missing bootstrap-console-save symlink.

* Tue Aug 21 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.4.0-04]
- Fixed e-smith-base dependency

* Tue Aug 21 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.4.0-03]
- Removed "public" from /etc/ftpusers
- Removed post-restore event
- Added Vendor tag

* Fri Aug 17 2001 gordonr
- [1.4.0-02]
- Autorebuild by rebuildRPM

* Wed Aug 8 2001 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-01]
- Rolled version number to 1.4.0-01. Includes patches upto 1.3.0-03.

* Fri Jul 6 2001 Peter Samuel <peters@e-smith.com>
- [1.3.0-03]
- Changed license to GPL

* Fri Jun 29 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-02]
- Make use of /etc/e-smith/pam/accounts.deny as template for /etc/ftpusers

* Fri Jun 29 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-01]
- Rolled version number to 1.3.0-01. Includes patches upto 1.2.0-07.

* Tue Mar 27 2001 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-07]
- Avoid proftp DoS attack with wildcards
- Allow FTP ports, with optional "ForcePassive|yes" property, defaulting to no

* Thu Feb  8 2001 Adrian Chung <adrianc@e-smith.com>
- [1.2.0-06]
- Rolling release number for GPG signing.

* Tue Jan 30 2001 Jason Miller <jmiller@e-smith.com>
- [1.2.0-05]
- Changed 'use smith::db' to 'use esmith::db'.

* Tue Jan 30 2001 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-04]
- And "use esmith::db" is reuqired.

* Mon Jan 29 2001 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-03]
- Fixed syntax error in previous fix :-)

* Fri Jan 26 2001 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-02]
- Fix reference to legacy config variable in proftpd.conf fragment

* Fri Jan 26 2001 Peter Samuel <peters@e-smith.com>
- [1.2.0-01]
- Rolled version number to 1.2.0-01. Includes patches upto 1.1.0-13.

* Thu Jan 25 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-13]
- Added default for accessLimits in proftpd-conf

* Wed Jan 24 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-12]
- Added AllowFTP fragment for /etc/rc.d/init.d/masq.
- Remove %post action

* Thu Jan 18 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-11]
- FTP now uses a new setting FTP access limits in remote access
  which completely governs access control to the service.
- The old FTP setting governs only user logins.
- updated xinetd.conf/ftp fragment to use new value

* Wed Jan 17 2001 Jason Miller <jmiller@e-smith.com>
- removed %postun deletion of ftp line in configuration
  to comply with the sillyness of rpm upgrade

* Fri Jan 12 2001 Gordon Rowell <gordonr@e-smith.com>
- ftpd != ftp :-(

* Fri Jan 12 2001 Gordon Rowell <gordonr@e-smith.com>
- Migrate FTPServerMode variable

* Sat Jan  6 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-7]
- Only run %post and %postun scripts if in runlevel 7

* Fri Jan  5 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-6]
- add selective bind back in.

* Fri Jan  5 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-5]
- backed out bind local interface code, needs to be rethought
  to allow access to localhost

* Thu Jan  4 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-4]
- changed 30ftp to only expand if ftp service is enabled.
- if ftp access is set to private, only bind to LocalIP in
  xinetd.conf

* Sun Dec 17 2000 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-3]
- Delete /etc/rc.d/init.d/masq template fragment.

* Mon Dec  4 2000 Adrian Chung <adrianc@e-smith.com>
- Added link for post-install.

* Fri Dec  1 2000 Adrian Chung <adrianc@e-smith.com>
- initial release

%description
Configuration files and templates for the ProFTPd ftp server.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
perl createlinks

mkdir -p root/service
ln -s /var/service/proftpd root/service/ftp

mkdir -p root/var/service/proftpd/supervise
touch root/var/service/proftpd/down

mkdir -p root/var/service/proftpd/log/supervise

mkdir -p root/var/log/proftpd

mkdir -p root/var/service/proftpd/env
mkdir -p root/var/service/proftpd/peers
mkdir -p root/etc/e-smith/templates/var/service/proftpd/peers/{0,local}
touch root/etc/e-smith/templates/var/service/proftpd/peers/{0,local}/template-begin

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    --dir /var/service/proftpd 'attr(01755,root,root)' \
    --file /var/service/proftpd/down 'attr(0644,root,root)' \
    --file /var/service/proftpd/run 'attr(0755,root,root)' \
    --file /var/service/proftpd/control/1 'attr(0755,root,root)' \
    --dir /var/service/proftpd/log 'attr(0755,root,root)' \
    --dir /var/service/proftpd/log/supervise 'attr(0700,root,root)' \
    --dir /var/service/proftpd/supervise 'attr(0700,root,root)' \
    --file /var/service/proftpd/log/run 'attr(0755,root,root)' \
    --dir /var/log/proftpd 'attr(2750,smelog,smelog)' \
    > %{name}-%{version}-%{release}-filelist
echo "%doc COPYING" >> %{name}-%{version}-%{release}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%pre
/sbin/e-smith/create-system-user smelog 1002 \
    'sme log user' /var/log/smelog /bin/false

%preun

%post

%postun

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
