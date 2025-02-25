# Subdomain Finder (Non-Threaded)

This Python script implements a simple subdomain finder using a wordlist. It's a beginner-friendly project for those learning about basic network programming and file handling in Python.  This version *does not* use multithreading.

## Features:

* Checks for subdomains using a provided wordlist.
* Provides clear output of found subdomains.
* Includes basic error handling for missing wordlist files.

## Requirements:

* Python 3.x
* `requests` library (install using `pip install requests`)

## How to Run on Your Local Machine:

1. **Clone (Optional):** If the project is in a Git repository: `git clone https://github.com/kissssu/Subdomain-Finder.git`
2. **Install `requests`:** `pip install requests`
3. **Wordlist:** Create `subdomains.txt` (one subdomain per line).
4. **Permissions (If needed):** `chmod +x subdomain_finder.py` (Linux/macOS).
5. **Run:** `python subdomain_finder.py` (or `./subdomain_finder.py`).

## Example:
```
Enter target domain: google.com
Enter path to subdomains wordlist: /path/to/wordlist.txt    
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

## Contributing:

Contributions are welcome! Please submit pull requests for bug fixes, new features, or improvements.  Be professional and respectful in your contributions.  All contributions should adhere to the project's code style and be well-documented.  Thank you!
