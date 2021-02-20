#!/usr/bin/python3
import requests
from argparse import ArgumentParser

def fetch_latest_release_without_asset(owner, repo, assetname):
    # fetch releases & find latest release id
    response = requests.get(f'https://api.github.com/repos/{owner}/{repo}/releases')
    releases = {int(r['id']):r for r in response.json()}
    release_id = max(releases.keys()) if releases else None
    if release_id:
        # find asset in release with name == assetname
        release = releases[release_id]
        asset = next((a for a in release['assets'] if a['name'] == assetname), None)
        # return release if asset was not found, otherwise return None
        return release if not asset else None
    return None

def main(owner, repo, assetname):
    release = fetch_latest_release_without_asset(owner, repo, assetname)
    if release:
        release_id = release['id']
        print(f'release_id:{release_id}')

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-o', '--owner', required=True)
    parser.add_argument('-r', '--repo', required=True)
    parser.add_argument('-a', '--assetname', required=True)
    args = parser.parse_args()
    main(args.owner, args.repo, args.assetname)
