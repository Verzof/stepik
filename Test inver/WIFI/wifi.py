import subprocess
import sys


def extract_wifi_password():
    profiles_data = subprocess.check_output('netsh wlan show profiles').decode('CP866').split('\n')
    profiles = [i.split(':')[1].strip() for i in profiles_data if 'All User Profile' in i]
    print(profiles)

    for profile in profiles:
        profiles_info = subprocess.check_output(f'netsh wlan show profiles {profile} key=clear').decode('CP866').split(
            '\n')

    try:
        password = [i.split(':')[1].strip() for i in profiles_info if 'Key content' in i][0]
    except IndexError:
        password = None

    print(password)


extract_wifi_password()
