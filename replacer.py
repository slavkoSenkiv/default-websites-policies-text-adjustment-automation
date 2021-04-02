from pathlib import Path

site_name = input('enter website name (example: Just A Conservative): ')  # 1 Just A Conservative

# here we convert website name to all needed formats
lover_site_name = site_name.lower()                     # 2 just a conservative
upper_site_name = site_name.upper()                     # 3 JUST A CONSERVATIVE
nospace_site_name = site_name.replace(' ', '')          # 4 JustAConservative
lover_nospace_site_name = nospace_site_name.lower()     # 5 justaconservative
upper_nospace_site_name = nospace_site_name.upper()     # 6 JUSTACONSERVATIVE


def in_page_replacer(page):

    # privacy doc section
    wg_file_path = Path.cwd()/(f'wg {page}.txt')
    new_file_path = Path.cwd()/(f'new {page}.txt')

    wg_file = open(wg_file_path, 'r')
    wg_file_content = wg_file.read()

    wg_file_content = wg_file_content.replace('Wise Gazette', site_name)
    wg_file_content = wg_file_content.replace('wisegazette', lover_nospace_site_name)
    wg_file_content = wg_file_content.replace('Wisegazette', lover_nospace_site_name)
    wg_file_content = wg_file_content.replace('WISEGAZETTE', upper_nospace_site_name)
    wg_file_content = wg_file_content.replace('WISE GAZETTE', upper_site_name)

    new_file = open(new_file_path, 'w')
    new_file.write(f'{page}\n')
    new_file.write(wg_file_content)

in_page_replacer('Contact Us')
in_page_replacer('About Us')
in_page_replacer('Privacy Policy')
in_page_replacer('Terms Of Conditions')

print('\ndone')

