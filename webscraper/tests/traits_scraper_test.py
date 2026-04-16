
from unittest import TestCase
from unittest.mock import Mock
from bs4 import BeautifulSoup
from fetchers.base_fetcher import BaseFetcher
from orm.trait import Trait
from scrapers.traits_scraper import TraitsScraper


class TestTraitsScraper(TestCase):
    def test_parse_success(self) -> None:
        main_html = """
        <div id="main">
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span>
                <h2 class="title">Affliction Traits</h2>
                <span class="trait" title="Curse">
                    <a href="Traits.aspx?ID=566">Curse</a>
                </span>
                <span class="trait" title="Disease">
                    <a href="Traits.aspx?ID=578">Disease</a>
                </span>
                <br>
                <h2 class="title">Alignment Traits</h2>
                <span class="trait" title="Chaotic">
                    <a href="Traits.aspx?ID=25">Chaotic</a>
                </span>
                <br>
            </span>
        </div>
        """

        description_html_1 = """
        <div>
            <a class="external-link"></a>
            descrição <a>curse</a>
            <br>
        </div>
        """

        description_html_2 = """
        <div>
            <a class="external-link"></a>
            <br>
        </div>
        """

        description_html_3 = """
        <div>
            <a class="external-link"></a>
            descrição chaotic
            <br>
        </div>
        """

        fetcher_mock: Mock = Mock(spec=BaseFetcher)
        fetcher_mock.fetch.side_effect = [
            description_html_1,
            description_html_2,
            description_html_3,
        ]

        scraper: TraitsScraper = TraitsScraper(baseFetcher=fetcher_mock)
        soup: BeautifulSoup = BeautifulSoup(main_html, "html.parser")

        result: list[Trait] = scraper.parse(soup)

        self.assertEqual(len(result), 3)

        self.assertEqual(result[0].name, "Curse")
        self.assertEqual(result[0].trait_type, "Affliction Traits")
        self.assertEqual(result[0].description, "descrição curse")

        self.assertEqual(result[1].name, "Disease")
        self.assertEqual(result[1].trait_type, "Affliction Traits")
        self.assertEqual(result[1].description, "")

        self.assertEqual(result[2].name, "Chaotic")
        self.assertEqual(result[2].trait_type, "Alignment Traits")
        self.assertEqual(result[2].description, "descrição chaotic")

    def test_main_not_found(self) -> None:
        main_html = "<div></div>"

        fetcher_mock: Mock = Mock(spec=BaseFetcher)

        scraper: TraitsScraper = TraitsScraper(baseFetcher=fetcher_mock)
        soup: BeautifulSoup = BeautifulSoup(main_html, "html.parser")

        with self.assertRaises(ValueError) as context:
            _ = scraper.parse(soup)

        self.assertEqual(str(context.exception), "Element 'main' not found")

    def test_traits_block_not_found(self) -> None:
        main_html = "<div id='main'></div>"

        fetcher_mock: Mock = Mock(spec=BaseFetcher)

        scraper: TraitsScraper = TraitsScraper(baseFetcher=fetcher_mock)
        soup: BeautifulSoup = BeautifulSoup(main_html, "html.parser")

        with self.assertRaises(IndexError) as context:
            _ = scraper.parse(soup)

        self.assertEqual(str(context.exception), "Number of contents is less then 10")
