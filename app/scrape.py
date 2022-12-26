import requests
from requests_html import HTMLSession


class Scraper:
    def __init__(
        self,
        url: str = "https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/",
    ):
        self.url = url

    def get_html(self) -> str:
        """get_html downloads HTML from self.url

        Returns:
            str: HTML
        """
        r = requests.get(self.url)
        return r.text

    def csv_gz_links(self) -> list[str]:
        """csv_gz_links acquires csv links from self.url

        Returns:
            list[str]: a list of csv.gz file URLs
        """
        links = []
        session = HTMLSession()
        r = session.get(self.url)
        absolute_links = r.html.absolute_links
        for link in absolute_links:
            if link.endswith(".csv.gz"):
                links.append(link)

        return links
