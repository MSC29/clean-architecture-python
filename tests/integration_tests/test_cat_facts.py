import vcr

from src.adapter.api.cat_facts.cat_facts_presenters import CatFactPresenter
from tests.integration_tests.request_utils import RequestsUtils
from tests.integration_tests.response_utils import ResponseUtils


class TestCatFacts:

    CAT_URL = 'http://localhost:8080/api/v1/cats/'

    @vcr.use_cassette('tests/integration_tests/fixtures/vcr_cassettes/cat_facts_facts.yaml')
    def test_should_return_multiple_results(self):
        # given the "all cat facts" route
        url = TestCatFacts.CAT_URL

        # when getting
        response = RequestsUtils.client().get(url)

        # then expect entire list, as per vcr cassette
        data: list[CatFactPresenter] = ResponseUtils.ok_and_parse(response)

        assert len(data) == 10
        assert data[0].fact == "The first true cats came into existence about 12 million years ago and were the Proailurus."
        assert data[0].nb_chars == 91

    @vcr.use_cassette('tests/integration_tests/fixtures/vcr_cassettes/cat_facts_fact.yaml')
    def test_should_return_one_result_only(self):
        # given the "random cat fact" route
        url = "{}random".format(TestCatFacts.CAT_URL)

        # when getting
        response = RequestsUtils.client().get(url)

        # then expect 1 only, as per vcr cassette
        data: CatFactPresenter = ResponseUtils.ok_and_parse(response)
        assert data.fact == "In the 1930s, two Russian biologists discovered that color change in Siamese kittens depend on their body temperature. Siamese cats carry albino genes that work only when the body temperature is above 98° F. If these kittens are left in a very warm room, their points won’t darken and they will stay a creamy white."
        assert data.nb_chars == 315
