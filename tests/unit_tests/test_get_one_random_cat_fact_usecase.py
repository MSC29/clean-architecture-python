from unittest.mock import MagicMock
import unittest

from src.adapter.spi.http.cat_fact_repository import CatFactsRepository
from src.application.usecases.get_one_random_cat_fact_usecase import GetOneRandomCatFactUseCase
from src.domain.api_exception import ApiException
from src.domain.cat_fact import CatFactEntity


class GetOneRandomCatFactUseCaseTest(unittest.TestCase):
    def test_should_return_generic_message_when_unexpected_repo_exception(self):
        # given the "one random cat fact" usecase repo with an unexpected exception
        cat_fact_repository = CatFactsRepository(None, "")
        cat_fact_repository.get_random_cat_fact = MagicMock(side_effect=Exception("random exception"))

        # when calling usecase
        get_one_random_cat_fact_usecase: GetOneRandomCatFactUseCase = GetOneRandomCatFactUseCase(cat_fact_repository)

        # then exception
        with self.assertRaises(ApiException) as context:
            get_one_random_cat_fact_usecase.execute()
        self.assertEqual('Cannot get random cat fact', str(context.exception.message))

    def test_should_return_custom_message_when_expected_repo_exception(self):
        # given the "one random cat fact" usecase repo raising with an expected ApiException
        cat_fact_repository = CatFactsRepository(None, "")
        cat_fact_repository.get_random_cat_fact = MagicMock(side_effect=ApiException("exception in repo"))

        # when calling usecase
        get_one_random_cat_fact_usecase: GetOneRandomCatFactUseCase = GetOneRandomCatFactUseCase(cat_fact_repository)

        # then exception
        with self.assertRaises(ApiException) as context:
            get_one_random_cat_fact_usecase.execute()
        self.assertEqual('exception in repo', str(context.exception.message))

    def test_should_return_one_result(self):
        # given the "one random cat fact" usecase repo returning one result
        cat_fact_repository = CatFactsRepository(None, "")
        cat_fact_repository.get_random_cat_fact = MagicMock(return_value=CatFactEntity("fact1", 1))

        # when calling usecase
        get_one_random_cat_fact_usecase: GetOneRandomCatFactUseCase = GetOneRandomCatFactUseCase(cat_fact_repository)
        data = get_one_random_cat_fact_usecase.execute()

        # then assert the result is the expected entity
        self.assertEqual(data.fact_txt, "fact1")
        self.assertEqual(data.fact_length, 1)
