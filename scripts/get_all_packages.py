from scripts.create_provider_stubs import _create_stubs

import requests
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
import os
from subprocess import CalledProcessError, check_output
if __name__ == "__main__":
    providers = requests.get('https://releases.hashicorp.com/')
    provider_set= set()
    parsed_html = BeautifulSoup(providers.text)
    for match in parsed_html.body.find_all('a'):
        if match.text.startswith('terraform-provider'):
            provider_set.add(match.text.replace('terraform-provider-',''))
    for provider in provider_set:
        version_set = set()
        if provider != 'google':
            continue
        versions = requests.get(f'https://releases.hashicorp.com/terraform-provider-{provider}/')
        versions_html = BeautifulSoup(versions.text)
        for match in versions_html.body.find_all('a'):
            if '_' in match.text:
                version = match.text.rsplit('_')[1]
                version_set.add(version)

        for version in version_set:
            try:
                check_output(['create_provider_stubs', f'hashicorp/{provider}', version, os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                                    'providers', ), r'c:/tech/terraform.exe'
                              ])
            except CalledProcessError as e:
                print(e.stderr)
                if 'is not compatible with Terraform' in str(e.stderr):
                    continue
                else:
                    raise e