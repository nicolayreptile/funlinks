import re


def clear_link(link: str) -> str:
    cleaned_link = re.sub(r'^https?://w{0,3}\.?', '', link)
    cleaned_link = re.sub(r'\?\S*$', '', cleaned_link)
    cleaned_link = cleaned_link.split('/')[0]
    if not re.match(r'^\S*\.\S*$', cleaned_link):
        raise ValueError('Not valid domain')
    return cleaned_link
