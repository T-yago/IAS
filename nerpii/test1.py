import sys
sys.path.append('/opt/homebrew/lib/python3.11/site-packages')
from nerpii.named_entity_recognizer import NamedEntityRecognizer
from nerpii.faker_generator import FakerGenerator
import pandas as pd


df = pd.read_csv("random_data.csv")

recognizer = NamedEntityRecognizer(df)
                                   

recognizer.assign_entities_with_presidio()
recognizer.assign_entities_manually()
recognizer.assign_organization_entity_with_model()

recognizer.dict_global_entities


generator = FakerGenerator(df, recognizer.dict_global_entities)
generator.get_faker_generation()

