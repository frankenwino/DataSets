from app.scrape import Scraper


def test_init():
    # Arrange
    url = "https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/"

    # Act
    s = Scraper()

    # Assert
    assert s.url == url


def test_get_html():
    # Arrange
    s = Scraper()

    # Act
    html = s.get_html()

    # Assert
    assert isinstance(html, str) is True


def test_csv_links():
    # Arrange
    s = Scraper()

    # Act
    links = s.csv_links()
    csv_gz_links = True
    for link in links:
        if not link.endswith(".csv.gz"):
            csv_gz_links = False
            break

    # Assert
    assert csv_gz_links is True
