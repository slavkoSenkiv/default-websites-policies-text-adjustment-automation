from pathlib import Path

site_name = input('enter website name (example: Just A Conservative): ')  # 1 Just A Conservative

# here we convert website name to all needed formats
lover_site_name = site_name.lower()                     # 2 just a conservative
upper_site_name = site_name.upper()                     # 3 JUST A CONSERVATIVE
nospace_site_name = site_name.replace(' ', '')          # 4 JustAConservative
lover_nospace_site_name = nospace_site_name.lower()     # 5 justaconservative
upper_nospace_site_name = nospace_site_name.upper()     # 6 JUSTACONSERVATIVE

# privacy doc section
wg_privacy = Path.cwd()/('wg privacy.txt')
new_privacy = Path.cwd()/('new privacy.txt')

wg_privacy_doc = open(wg_privacy, 'r')
wg_privacy_doc_content = wg_privacy_doc.read()

wg_privacy_doc_content = wg_privacy_doc_content.replace('Wise Gazette', site_name)
wg_privacy_doc_content = wg_privacy_doc_content.replace('wisegazette', lover_nospace_site_name)
wg_privacy_doc_content = wg_privacy_doc_content.replace('Wisegazette', lover_nospace_site_name)
wg_privacy_doc_content = wg_privacy_doc_content.replace('WISEGAZETTE', upper_nospace_site_name)
wg_privacy_doc_content = wg_privacy_doc_content.replace('WISE GAZETTE', upper_site_name)

new_privacy_doc = open(new_privacy, 'w')
new_privacy_doc.write('Privacy Policy\n')
new_privacy_doc.write(wg_privacy_doc_content)

# about doc section
wg_about = Path.cwd()/('wg about.txt')
new_about = Path.cwd()/('new about.txt')

wg_about_doc = open(wg_about, 'r')
wg_about_doc_content = wg_about_doc.read()

wg_about_doc_content = wg_about_doc_content.replace('Wise Gazette', site_name)
wg_about_doc_content = wg_about_doc_content.replace('wisegazette', lover_nospace_site_name)
wg_about_doc_content = wg_about_doc_content.replace('Wisegazette', lover_nospace_site_name)
wg_about_doc_content = wg_about_doc_content.replace('WISEGAZETTE', upper_nospace_site_name)
wg_about_doc_content = wg_about_doc_content.replace('WISE GAZETTE', upper_site_name)

new_about_doc = open(new_about, 'w')
new_about_doc.write('About Us\n')
new_about_doc.write(wg_about_doc_content)

# contact doc section
wg_contact = Path.cwd()/('wg contact.txt')
new_contact = Path.cwd()/('new contact.txt')

wg_contact_doc = open(wg_contact, 'r')
wg_contact_doc_content = wg_contact_doc.read()

wg_contact_doc_content = wg_contact_doc_content.replace('Wise Gazette', site_name)
wg_contact_doc_content = wg_contact_doc_content.replace('wisegazette', lover_nospace_site_name)
wg_contact_doc_content = wg_contact_doc_content.replace('Wisegazette', lover_nospace_site_name)
wg_contact_doc_content = wg_contact_doc_content.replace('WISEGAZETTE', upper_nospace_site_name)
wg_contact_doc_content = wg_contact_doc_content.replace('WISE GAZETTE', upper_site_name)

new_contact_doc = open(new_contact, 'w')
new_contact_doc.write('Contact Us\n')
new_contact_doc.write(wg_contact_doc_content)

# terms doc section
wg_terms = Path.cwd()/('wg terms.txt')
new_terms = Path.cwd()/('new terms.txt')

wg_terms_doc = open(wg_terms, 'r')
wg_terms_doc_content = wg_terms_doc.read()

wg_terms_doc_content = wg_terms_doc_content.replace('Wise Gazette', site_name)
wg_terms_doc_content = wg_terms_doc_content.replace('wisegazette', lover_nospace_site_name)
wg_terms_doc_content = wg_terms_doc_content.replace('Wisegazette', lover_nospace_site_name)
wg_terms_doc_content = wg_terms_doc_content.replace('WISEGAZETTE', upper_nospace_site_name)
wg_terms_doc_content = wg_terms_doc_content.replace('WISE GAZETTE', upper_site_name)

new_terms_doc = open(new_terms, 'w')
new_terms_doc.write('Terms Of Conditions\n')
new_terms_doc.write(wg_terms_doc_content)

print('\ndone')

