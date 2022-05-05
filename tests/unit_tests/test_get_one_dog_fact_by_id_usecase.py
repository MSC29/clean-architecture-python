from unittest.mock import MagicMock
import unittest

from src.adapter.spi.db.dog_fact_repository import DogFactRepository
from src.application.usecases.get_one_dog_fact_by_id_usecase import GetOneDogFactByIdUseCase
from src.domain.api_exception import ApiException
from src.domain.dog_fact import DogFactEntity


class GetOneDogFactByIdUseCaseTest(unittest.TestCase):
    def test_should_raise_exception_when_unexpected_repo_exception(self):
        # given the "one dog fact by id" usecase repo raising with an unexpected random exception
        dog_fact_repository = DogFactRepository(None)
        dog_fact_repository.get_dog_fact_by_id_by_id = MagicMock(side_effect=Exception("random exception"))

        # when calling usecase
        get_all_dog_facts_usecase: GetOneDogFactByIdUseCase = GetOneDogFactByIdUseCase(1, dog_fact_repository)

        # then exception
        with self.assertRaises(ApiException) as context:
            get_all_dog_facts_usecase.execute()
        self.assertEqual('Cannot get single dog fact', str(context.exception.message))

    def test_should_raise_exception_when_expected_repo_exception(self):
        # given the "one dog fact by id" usecase repo raising with an expected ApiException
        dog_fact_repository = DogFactRepository(None)
        dog_fact_repository.get_dog_fact_by_id = MagicMock(side_effect=ApiException("exception in repo"))

        # when calling usecase
        get_all_dog_facts_usecase: GetOneDogFactByIdUseCase = GetOneDogFactByIdUseCase(1, dog_fact_repository)

        # then exception
        with self.assertRaises(ApiException) as context:
            get_all_dog_facts_usecase.execute()
        self.assertEqual('exception in repo', str(context.exception.message))

    def test_should_return_one_result(self):
        # given the "one dog fact by id" usecase repo returning one result
        dog_fact_repository = DogFactRepository(None)
        dog_fact_repository.get_dog_fact_by_id = MagicMock(return_value=DogFactEntity(1, "fact1"))

        # when calling usecase
        get_all_dog_facts_usecase: GetOneDogFactByIdUseCase = GetOneDogFactByIdUseCase(1, dog_fact_repository)
        data = get_all_dog_facts_usecase.execute()

        # then assert the result is the expected entity
        self.assertEqual(data.fact_id, 1)
        self.assertEqual(data.fact_txt, "fact1")
