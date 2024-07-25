import requests
from bs4 import BeautifulSoup

def extract_text_from_html(html_markup):
    """
    Extracts text from HTML markup.

    Args:
    html_markup (str): A string containing HTML markup.

    Returns:
    full_text (str): A string containing HTML markup. full text of the document
    """
    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_markup, 'html.parser')

    # Extract the text from the entire document
    full_text = soup.get_text()

   
    return full_text
        
