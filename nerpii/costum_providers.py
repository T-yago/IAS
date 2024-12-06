from faker import Faker
from faker.providers import DynamicProvider
from faker.providers import BaseProvider

# The `course_provider` can be added to a Faker instance to generate random course names.
course_provider = DynamicProvider(
     provider_name="course",
     elements=["MIA", "LEIC", "LIACD", "LCC"]
)

# The `MyProvider` class can be used to generate random ages between 18 and 80.
class AgeProvider(BaseProvider):
     def age(self):
         return self.random_int(min=18, max=80)

# The `my_word_list` can be used as a source of random words related to sweets and desserts.
my_word_list = [
'danish','cheesecake','sugar',
'Lollipop','wafer','Gummies',
'sesame','Jelly','beans',
'pie','bar','Ice','oat' ]





# Top Richest People Dataset

industry_provider = DynamicProvider(
    provider_name="industry",
    elements = [
            "Technology", "Healthcare", "Finance", "Manufacturing", "Retail",
            "Education", "Energy", "Transportation", "Construction", "Telecommunications"
        ]
)

organization_provider = DynamicProvider(
    provider_name="organization",
    elements = [
        "Apple",
        "Microsoft",
        "Amazon",
        "Google (Alphabet)",
        "Meta (Facebook)",
        "Tesla",
        "Berkshire Hathaway",
        "NVIDIA",
        "Samsung",
        "Tencent",
        "Visa",
        "JPMorgan Chase",
        "Johnson & Johnson",
        "Procter & Gamble",
        "ExxonMobil",
        "Toyota",
        "ICBC (Industrial and Commercial Bank of China)",
        "Walmart",
        "Chevron",
        "Roche",
        "Pfizer",
        "Coca-Cola",
        "PepsiCo",
    ]
)