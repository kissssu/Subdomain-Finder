#!/usr/bin/python3

import requests

def subdomain_finder(subdomain, domain):
    """Checks if a given subdomain exists for a target domain."""
    url = f"http://{subdomain}.{domain}"
    try:
        response = requests.get(url, timeout=5)  # Timeout to prevent hanging
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

def main():
    """Main function to initiate the subdomain finder."""
    domain = input("Enter target domain: ")
    subdomains_file = input("Enter path to subdomains wordlist: ")

    try:
        with open(subdomains_file, 'r') as f:
            subdomains = f.read().splitlines()
    except FileNotFoundError:
        print(f"Error: Subdomains file '{subdomains_file}' not found.")
        return

    results = []

    for subdomain in subdomains:
        if subdomain_finder(subdomain, domain):
            results.append(subdomain)
            print(f"[+] Found: {subdomain}.{domain}")

    print("\nFound Subdomains:")
    for subdomain in results:
        print(f"{subdomain}.{domain}")

if __name__ == "__main__":
    main()
