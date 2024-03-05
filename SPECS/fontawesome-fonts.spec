%global fontname fontawesome
%global fontconf 60-%{fontname}.conf

Name:		%{fontname}-fonts
Version:	4.7.0
Release:	5%{?dist}

Summary:	Iconic font set
License:	OFL
URL:		http://fontawesome.io
Source0:	http://fontawesome.io/assets/font-awesome-%{version}.zip
Source1:	%{name}-fontconfig.conf
Source2:	README-Trademarks.txt
BuildArch:	noarch
BuildRequires:	fontpackages-devel
BuildRequires:	ttembed
Requires:	fontpackages-filesystem


%description
Font Awesome gives you scalable vector icons that can instantly be
customized — size, color, drop shadow, and anything that can be done with the
power of CSS.

This package contains OpenType and TrueType font files which are typically used
locally.

%package web
License:	OFL and MIT
Requires:	%{fontname}-fonts = %{version}-%{release}
Summary:	Iconic font set, web files

%description web
Font Awesome gives you scalable vector icons that can instantly be
customized — size, color, drop shadow, and anything that can be done with the
power of CSS.

This package contains CSS, SCSS and LESS style files as well as Web Open Font
Format versions 1 and 2, Embedded OpenType and SVG font files which are
typically used on the web.

%prep
%setup -q -n font-awesome-%{version}
cp -p %SOURCE2 .

%build
ttembed fonts/*.ttf fonts/*.otf

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p fonts/*.ttf fonts/*.otf fonts/*.woff fonts/*.svg fonts/*.woff2 fonts/*.eot %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
		%{buildroot}%{_fontconfig_confdir}/%{fontconf}

mkdir -p %{buildroot}%{_datadir}/font-awesome-web/
cp -a css less scss %{buildroot}%{_datadir}/font-awesome-web/

# files:
%_font_pkg -f %{fontconf} *.ttf *.otf
%exclude %{_datadir}/fonts/fontawesome/fontawesome-webfont.svg
%exclude %{_datadir}/fonts/fontawesome/fontawesome-webfont.woff
%exclude %{_datadir}/fonts/fontawesome/fontawesome-webfont.woff2
%exclude %{_datadir}/fonts/fontawesome/fontawesome-webfont.eot

%doc README-Trademarks.txt

%files web
%{_datadir}/font-awesome-web/
%{_datadir}/fonts/fontawesome/fontawesome-webfont.svg
%{_datadir}/fonts/fontawesome/fontawesome-webfont.woff
%{_datadir}/fonts/fontawesome/fontawesome-webfont.woff2
%{_datadir}/fonts/fontawesome/fontawesome-webfont.eot

%changelog
* Tue Nov 14 2023 Thomas Woerner <twoerner@redhat.com> - 4.7.0-5
- Release bump to solve missing fontawesome-fonts-web in RHEL 8.9 and later
  Resolves: RHEL-16351

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 27 2016 Fabio Alessandro Locati <fale@redhat.com> - 4.7.0-1
- Update to 4.7.0

* Sun May 22 2016 Fabio Alessandro Locati <fale@redhat.com> - 4.6.3-1
- Update to 4.6.3
- Update the brand icons list using the script

* Thu May 05 2016 Fabio Alessandro Locati <fale@redhat.com> - 4.6.2-1
- Update to 4.6.1
- Update the brand icons list using a new script
- Add the script to create brand icons list

* Wed Apr 13 2016 Fabio Alessandro Locati <fale@redhat.com> - 4.6.1-1
- Update to 4.6.0
- Update the brand list with the icons new in 4.6.0

* Tue Mar 29 2016 Fabio Alessandro Locati <fale@redhat.com> - 4.5.0-1
- Update to 4.5.0
- Update the brand list with the icons new in 4.5.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 04 2015 Nils Philippsen <nils@redhat.com> - 4.4.0-2
- include .eot files
- amend -web license and summary, and descriptions

* Thu Sep 17 2015 Matthias Runge <mrunge@redhat.com> - 4.4.0-1
- update to 4.4.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Dec 04 2014 Matthias Runge <mrunge@redhad.com> - 4.1.0-2
- include .woff and .svg files (rhbz#1110646)

* Tue Jul 08 2014 Petr Vobornik <pvoborni@redhat.com> - 4.1.0-1
- update to version 4.1.0
- renamed web packaged dir from font-awesome-$version to font-awesome-web

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 02 2014 Petr Vobornik <pvoborni@redhat.com> - 4.0.3-1
- embeddable flag set to installable by ttembed
- web package license updated to MIT
- README-Trademarks.txt added

* Mon Nov 04 2013 Ryan Lerch <ryanlerch@fedoraproject.org> - 4.0.3-0
- initial package based off spot's package
