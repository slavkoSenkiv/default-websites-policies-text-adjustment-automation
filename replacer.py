# wg wisegazette
# new

from pathlib import Path

site_name = input('enter website name: \n(example: Just A Conservative)\n')

lover_site_name = site_name.lower()
upper_site_name = site_name.upper()
nospace_site_name = site_name.replace(' ', '')
lover_nospace_site_name = nospace_site_name.lower()
upper_nospace_site_name = nospace_site_name.upper()

# where to get data from
wg_terms = Path.cwd()/('wg terms.txt')
wg_about_us = Path.cwd()/('wg about.txt')
wg_contact_us = Path.cwd()/('wg contact.txt')
wg_privacy_policy = Path.cwd()/('wg privacy.txt')

# where to put modified data
new_terms = Path.cwd()/('new terms.txt')
new_about_us = Path.cwd()/('new about.txt')
new_contact_us = Path.cwd()/('new contact.txt')
new_privacy_policy = Path.cwd()/('new privacy.txt')

# opening files
wg_terms_file = open(wg_terms, 'r')
wg_terms_file_content = wg_terms_file.read()

<<<<<<< Updated upstream
wg_about_us_file = open(wg_about_us, 'r')
wg_about_us_file_content = wg_about_us_file.read()

wg_contact_us_file = open(wg_contact_us, 'r')
wg_contact_us_file_content = wg_contact_us_file.read()

wg_privacy_policy_file = open(wg_privacy_policy, 'r')
wg_privacy_policy_file_content = wg_privacy_policy_file.read()

wg_terms_file_content = wg_terms_file_content.replace('Wise Gazette', site_name)
wg_terms_file_content = wg_terms_file_content.replace('wisegazette', lover_nospace_site_name)
wg_terms_file_content = wg_terms_file_content.replace('WISEGAZETTE', upper_nospace_site_name)
wg_terms_file_content = wg_terms_file_content.replace('WISE GAZETTE', upper_site_name)
=======
def in_page_replacer(page):

    wg_file_path = Path.cwd()/(f'wg {page}.txt')
    wg_file = open(wg_file_path, 'r')
    wg_file_content = wg_file.read()
>>>>>>> Stashed changes

wg_terms_file_content = wg_terms_file_content.replace('Wise Gazette', site_name)
wg_terms_file_content = wg_terms_file_content.replace('wisegazette', lover_nospace_site_name)
wg_terms_file_content = wg_terms_file_content.replace('WISEGAZETTE', upper_nospace_site_name)
wg_terms_file_content = wg_terms_file_content.replace('WISE GAZETTE', upper_site_name)

wg_terms_file_content = wg_terms_file_content.replace('Wise Gazette', site_name)
wg_terms_file_content = wg_terms_file_content.replace('wisegazette', lover_nospace_site_name)
wg_terms_file_content = wg_terms_file_content.replace('WISEGAZETTE', upper_nospace_site_name)
wg_terms_file_content = wg_terms_file_content.replace('WISE GAZETTE', upper_site_name)

<<<<<<< Updated upstream
wg_terms_file_content = wg_terms_file_content.replace('Wise Gazette', site_name)
wg_terms_file_content = wg_terms_file_content.replace('wisegazette', lover_nospace_site_name)
wg_terms_file_content = wg_terms_file_content.replace('WISEGAZETTE', upper_nospace_site_name)
wg_terms_file_content = wg_terms_file_content.replace('WISE GAZETTE', upper_site_name)

file = open(new_terms, 'w')
file.write(fileContent)
print('done')#



=======
while True:
    doc = pyinputplus.inputMenu(['Contact Us',
                                 'About Us Health',
                                 'About Us Non Health',
                                 'Privacy Policy',
                                 'Terms And Conditions',
                                 'Footer'],
                                 'Pick which doc you want copy to clipboard:\n', numbered=True)
    in_page_replacer(doc)
    print(f'\n{doc} modified text copied to clipboard\n')

>>>>>>> Stashed changes
