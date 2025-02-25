# Subdomain Finder (Non-Threaded)

This Python script implements a simple subdomain finder using a wordlist. It's a beginner-friendly project for those learning about basic network programming and file handling in Python.  This version *does not* use multithreading.

## Features:

* Checks for subdomains using a provided wordlist.
* Provides clear output of found subdomains.
* Includes basic error handling for missing wordlist files.

## Requirements:

* Python 3.x
* `requests` library (install using `pip install requests`)

## Usage:

1. Save the script as `subdomain_finder.py`.
2. Prepare a text file containing subdomains to check (e.g., "subdomains.txt"), one subdomain per line.
3. Run the script from your terminal: `python subdomain_finder.py`
4. The script will prompt you for the target domain and the path to the subdomains wordlist. It will then scan for subdomains and print the found ones.

## Example:
```
Enter target domain: google.com
Enter path to subdomains wordlist: /home/kissu/Kissu/Cyber-Things/wordlists/directory-medium-2-3.txt    
[+] Found: images.google.com
[+] Found: news.google.com
[+] Found: about.google.com
...
```

## Disclaimer:

This script is for educational purposes only. Always use it responsibly and ethically. Do not scan targets without proper authorization.

## Further Enhancements:

* Use a more comprehensive subdomains wordlist.
* Implement multithreading for faster scanning (see the threaded version of this script).
* Add options for output formatting (e.g., saving results to a file).
* Integrate with other tools and services for a more robust scanning solution.
* Add more robust error handling (e.g., handling different HTTP status codes).
