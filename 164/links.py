import sys

INTERNAL_LINKS = ('pybit.es', 'codechalleng.es')


def make_html_links():
    for line in sys.stdin:
        if line.startswith("http"):
            url, name = line.strip().split(",")
            url = url.strip()
            if not any( [ domain in url 
                          for domain in ["pybit.es", "codechalleng.es"] ]):
                url = f'"{url}" target="_blank"'
            else:
                url = f'"{url}"'
            print(f'<a href={url}>{name.strip()}</a>')


if __name__ == '__main__':
    make_html_links()