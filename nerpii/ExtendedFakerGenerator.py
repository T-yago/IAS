from nerpii.faker_generator import FakerGenerator
from faker import Faker
from costum_providers import course_provider, industry_provider, organization_provider

class ExtendedFakerGenerator(FakerGenerator):
    def __init__(self, df, entity_dict):
        super().__init__(df, entity_dict)
        self.faker = Faker()
        self.faker.add_provider(course_provider)
        self.faker.add_provider(industry_provider)
        self.faker.add_provider(organization_provider)
        self.custom_generators = {
            "AGE": lambda: self.faker.random_int(min=18, max=80),
            "COURSE": lambda: self.faker.course(),
            "INDUSTRY": lambda: self.faker.industry(),
            "ORGANIZATION": lambda: self.faker.organization(),
        }

    def get_faker_generation(self):
        super().get_faker_generation()

        for column, entity_info in self.dict_global_entities.items():
            if not entity_info:
                continue

            entity = entity_info["entity"]

            # Check if the entity has a custom generator
            if entity in self.custom_generators:
                self.dataset[column] = self.dataset[column].apply(lambda _: self.custom_generators[entity]())