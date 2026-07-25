"""
41: Markdown to HTML Converter
Parse and format text structures into HTML.
"""
import re

def md_to_html(md_text):
    html = re.sub(r'^# (.*)$', r'<h1></h1>', md_text, flags=re.M)
    html = re.sub(r'^## (.*)$', r'<h2></h2>', html, flags=re.M)
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong></strong>', html)
    return html

if __name__ == "__main__":
    md = "# Hello World
**Bold text**"
    print(md_to_html(md))
