import random
from django.template import engine


# This is just a mock/simulation of an engine
# that we feed params to and returns the reommendations and risks

RISK = [
    'Heredity With a family history of breast cancer, the risk of developing breast cancer increases 2-3 times.',
    'Reproductive factors Reproductive factors include early onset of menses, late menopause, and late birth of the first child.',
    'Other factors that increase the risk of developing breast cancer include alcohol consumption, being overweight and obese, and physical inactivity.'
]

RECOMMENDATION = [
    'To prevent breast cancer, you should regularly take',
    'At the age of 20-40, examinations in the examination room once a year;',
    'Ultrasound examination of the mammary glands after 40 years 1 time per year;',
    'X-ray prophylactic examination of the mammary glands (mammography) after 40 years 1 every 2 years;',
    'Breast self-examination.',
]

class RecommendationEngine:
    """
    In a real world scenario this would be
    a controller to AI engine that 
    1. cleans up the data 
    2. passes it to AI engine
    3. return the response from AI engine
    """
    def get_recommendation(self):
        data = {
            'risk' : RISK[random.randint(0, 2)],
            'recommendation': RECOMMENDATION[random.randint(0, 4)]
        }
        return data