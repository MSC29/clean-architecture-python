from unittest.mock import MagicMock
import unittest

from src.adapter.spi.http.cat_fact_repository import CatFactsRepository
from src.application.usecases.get_all_cat_facts_usecase import GetAllCatFactsUseCase
from src.domain.api_exception import ApiException
from src.domain.cat_fact import CatFactEntity


class GetAllCatFactsUseCaseTest(unittest.TestCase):
    def test_should_return_generic_message_when_unexpected_repo_exception(self):
        # given the "all cat facts" usecase repo with an unexpected exception
        cat_fact_repository = CatFactsRepository(None, "")
        cat_fact_repository.get_all_cat_facts = MagicMock(side_effect=Exception("random exception"))

        # when calling usecase
        get_all_cat_facts_usecase: GetAllCatFactsUseCase = GetAllCatFactsUseCase(cat_fact_repository)

        # then exception
        with self.assertRaises(ApiException) as context:
            get_all_cat_facts_usecase.execute()
        self.assertEqual('Cannot get all cat facts', str(context.exception.message))

    def test_should_return_custom_message_when_expected_repo_exception(self):
        # given the "all cat facts" usecase repo raising with an expected ApiException
        cat_fact_repository = CatFactsRepository(None, "")
        cat_fact_repository.get_all_cat_facts = MagicMock(side_effect=ApiException("exception in repo"))

        # when calling usecase
        get_all_cat_facts_usecase: GetAllCatFactsUseCase = GetAllCatFactsUseCase(cat_fact_repository)

        # then exception
        with self.assertRaises(ApiException) as context:
            get_all_cat_facts_usecase.execute()
        self.assertEqual('exception in repo', str(context.exception.message))

    def test_should_return_empty_list(self):
        # given the "all cat facts" usecase repo returning an empty list
        cat_fact_repository = CatFactsRepository(None, "")
        cat_fact_repository.get_all_cat_facts = MagicMock(return_value=[])

        # when calling usecase
        get_all_cat_facts_usecase: GetAllCatFactsUseCase = GetAllCatFactsUseCase(cat_fact_repository)
        data = get_all_cat_facts_usecase.execute()

        # then assert the result is an empty list
        self.assertEqual(len(data), 0)

    def test_should_return_list(self):
        # given the "all cat facts" usecase repo returning a list of 2 entities
        cat_fact_repository = CatFactsRepository(None, "")
        cat_fact_repository.get_all_cat_facts = MagicMock(return_value=[CatFactEntity("fact1", 1), CatFactEntity("fact2", 2)])

        # when calling usecase
        get_all_cat_facts_usecase: GetAllCatFactsUseCase = GetAllCatFactsUseCase(cat_fact_repository)
        data = get_all_cat_facts_usecase.execute()

        # then assert the result is an empty list
        self.assertEqual(len(data), 2)
