#!/usr/bin/python3

import threading
import requests
import time

def subdomain_finder(subdomain, domain):
    """
    Checks if a given subdomain exists for a target domain.

    Args:
        subdomain (str): The subdomain to check (e.g., "mail", "www").
        domain (str): The target domain (e.g., "example.com").

    Returns:
        bool: True if the subdomain exists, False otherwise.
    """
    url = f"http://{subdomain}.{domain}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

def worker(subdomains, domain, results):
    """
    Worker function for threaded subdomain checking.

    Args:
        subdomains (list): List of subdomains to check.
        domain (str): The target domain.
        results (list): List to store found subdomains.
    """
    for subdomain in subdomains:
        if subdomain_finder(subdomain, domain):
            results.append(subdomain)
            print(f"[+] Found: {subdomain}.{domain}")

def main():
    """
    Main function to initiate the subdomain finder.
    """
    domain = input("Enter target domain: ")
    subdomains_file = input("Enter path to subdomains wordlist: ")

    with open(subdomains_file, 'r') as f:
        subdomains = f.read().splitlines()

    threads = []
    results = []
    chunk_size = 100  # Adjust chunk size for optimal performance

    for i in range(0, len(subdomains), chunk_size):
        chunk = subdomains[i:i+chunk_size]
        thread = threading.Thread(target=worker, args=(chunk, domain, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("\nFound Subdomains:")
    for subdomain in results:
        print(f"{subdomain}.{domain}")

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2f} seconds")