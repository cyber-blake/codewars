# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.
import re


def domain_name(url):
    domain_regex = r"^(?:https?://)?(?:www\.)?([^/\.]+)\.[^/]+"
    match = re.search(domain_regex, url)
    return match.group(1) if match else None
