from unittest.mock import MagicMock
import unittest

from src.adapter.spi.db.dog_fact_repository import DogFactRepository
from src.application.usecases.get_all_dog_facts_usecase import GetAllDogFactsUseCase
from src.domain.api_exception import ApiException
from src.domain.dog_fact import DogFactEntity


class GetAllDogFactsUseCaseTest(unittest.TestCase):
    def test_should_return_generic_message_when_unexpected_repo_exception(self):
        # given the "all dog facts" usecase repo with an unexpected exception
        dog_fact_repository = DogFactRepository(None)
        dog_fact_repository.get_all_dog_facts = MagicMock(side_effect=Exception("random exception"))

        # when calling usecase
        get_all_dog_facts_usecase: GetAllDogFactsUseCase = GetAllDogFactsUseCase(dog_fact_repository)

        # then exception
        with self.assertRaises(ApiException) as context:
            get_all_dog_facts_usecase.execute()
        self.assertEqual('Cannot get all dog facts', str(context.exception.message))

    def test_should_return_custom_message_when_expected_repo_exception(self):
        # given the "all dog facts" usecase repo raising with an expected ApiException
        dog_fact_repository = DogFactRepository(None)
        dog_fact_repository.get_all_dog_facts = MagicMock(side_effect=ApiException("exception in repo"))

        # when calling usecase
        get_all_dog_facts_usecase: GetAllDogFactsUseCase = GetAllDogFactsUseCase(dog_fact_repository)

        # then exception
        with self.assertRaises(ApiException) as context:
            get_all_dog_facts_usecase.execute()
        self.assertEqual('exception in repo', str(context.exception.message))

    def test_should_return_empty_list(self):
        # given the "all dog facts" usecase repo returning an empty list
        dog_fact_repository = DogFactRepository(None)
        dog_fact_repository.get_all_dog_facts = MagicMock(return_value=[])

        # when calling usecase
        get_all_dog_facts_usecase: GetAllDogFactsUseCase = GetAllDogFactsUseCase(dog_fact_repository)
        data = get_all_dog_facts_usecase.execute()

        # then assert the result is an empty list
        self.assertEqual(len(data), 0)

    def test_should_return_list(self):
        # given the "all dog facts" usecase repo returning a list of 2 entities
        dog_fact_repository = DogFactRepository(None)
        dog_fact_repository.get_all_dog_facts = MagicMock(return_value=[DogFactEntity(1, "fact1"), DogFactEntity(2,"fact2")])

        # when calling usecase
        get_all_dog_facts_usecase: GetAllDogFactsUseCase = GetAllDogFactsUseCase(dog_fact_repository)
        data = get_all_dog_facts_usecase.execute()

        # then assert the result is an empty list
        self.assertEqual(len(data), 2)
