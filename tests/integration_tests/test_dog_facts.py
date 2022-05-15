import pytest

from src.adapter.api.dog_facts.dog_facts_presenters import DogFactPresenter
from tests.integration_tests.request_utils import RequestsUtils
from tests.integration_tests.response_utils import ResponseUtils


class TestDogFacts:

    DOG_URL = 'http://localhost:8080/api/v1/dogs/'

    @pytest.mark.usefixtures("setup_db")
    def test_should_return_multiple_results(self):
        # given the "all dog facts" route
        url = TestDogFacts.DOG_URL

        # when getting
        response = RequestsUtils.client().get(url)

        # then expect 3 results (inserted in db)
        data: list[DogFactPresenter] = ResponseUtils.ok_and_parse(response)

        assert len(data) == 3
        assert data[0].txt == "Forty-five percent of U.S. dogs sleep in their owner's bed"
        assert data[0].fact_id == 1

    @pytest.mark.usefixtures("setup_db")
    def test_should_return_one_result_only(self):
        # given the "single dog facts" route
        url = "{}2".format(TestDogFacts.DOG_URL)

        # when getting
        response = RequestsUtils.client().get(url)

        # then expect 1 result (id 2 inserted in db)
        data: DogFactPresenter = ResponseUtils.ok_and_parse(response)
        assert data.txt == "Seventy percent of people sign their dog's name on their holiday cards"
        assert data.fact_id == 2
