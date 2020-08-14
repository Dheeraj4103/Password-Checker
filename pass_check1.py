import requests
import hashlib


def request(query):
    url = 'https://api.pwnedpasswords.com/range/' + query
    res = requests.get(url)
    if res.status_code == 200:
        return res
    elif res.status_code == 400:
        raise RuntimeError("Error: Try another password")


def passleak_check(hashes, hash1):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash1:
            return count
    return 0


def pass_check_api(pass_check):
    hash_sha = hashlib.sha1(pass_check.encode('utf-8')).hexdigest().upper()
    hash_sha1, tail = hash_sha[:5], hash_sha[5:]
    hash_5 = request(hash_sha1)
    return passleak_check(hash_5, tail)


def main1(pass_check):
    get_count = pass_check_api(pass_check)
    if get_count:
        print(
            f"{pass_check} was found {get_count} times... , Try with another Password")
    else:
        print(f"{pass_check} NOT found,  Carry on")


if __name__ == "__main__":
    while True:
        pass_check = input("Enter your Password: ")
        main1(pass_check)
