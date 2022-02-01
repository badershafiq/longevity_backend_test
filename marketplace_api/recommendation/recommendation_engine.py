import random
from django.template import engine


# This is just a mock/simulation of an engine
# that we feed params to and returns the reommendations and risks

RISK = [
    'Heredity With a family history of breast cancer, the risk of developing breast cancer increases 2-3 times.',
    'Reproductive factors Reproductive factors include early onset of menses, late menopause, and late birth of the first child.',
    'Other factors that increase the risk of developing breast cancer include alcohol consumption, being overweight and obese, and physical inactivity.'
]

RECOMMENDATION1 = [
    'Divide your meals into 3 main meals at regular intervals.',
    'Drink softened water only.',
    'Include vegetables in every meal. Prefer seasonal vegetables and fruits. Consume at least 400g of fresh vegetables and fruits.',
    'Include vegetables at every meal. Prefer seasonal vegetables and fruits. Consume at least 400 grams of fresh vegetables and fruits.',
    '1-2 nuts a day (walnuts/almonds/pistachios).',
    'Keep dairy products to a minimum. Give preference to products based on goat milk.',
    'Limit intake of baked and fried foods, junk food, soda, and energy drinks.',
    'Keep red meat intake to a minimum.',
    'Eat 60-100g of meat a day (preferably white meat or fish). Do not eat meat 2 days a week.',
    'Go to the gym 3 times a week. Alternate strength and cardio workouts.',
    'Observe a daily routine. Sleep at least 8 hours a day.',
    'Eat 3 or maximum 4 times a day, drink water in between meals instead of snacks.',
    'Exclude flour and fatty foods from the diet.',
    'Reduce your consumption of white bread.',
    'Limit vegetable and animal fats to 30 of daily calorie intake.',
    'Eat 60-100g of meat a day (preferably white meat or fish). Do not eat meat 2 days a week.',
    'Get at least 150 minutes of physical activity per week to improve your health.',
    'Eat small meals. Exclude flour and fatty foods from the diet. Get up from the table a little bit hungry.',
    'Exclude white bread from a diet.',
    'Eat fresh fruits, vegetables and salads instead of refined carbohydrates and processed food.',
    'Use water instead of soft drinks or juices. Exclude energy drinks.',
    'Limit alcohol consumption to a moderate level (1-2 glasses a day).',
    'Do not have dinner one day a week (or last meal before 4 pm).',
    'Eat low-fat or low-fat dairy products. Ideally, do not consume dairy products every day. Give preference to products based on goat milk.',
    'Combine aerobic and strength training.',
    'Achieve 150 minutes of physical activity per week to improve your health and 300 to 360 minutes per week to lower weight and maintain a healthy body. Take walks. The total number of steps should be 10-15 thousand per day.',
    'Desserts only in the morning until 13:00. If you want in the evening, wait until morning and drink water.'
]

RECOMMENDATION2 = [
    'Low-fat varieties of meat, fish (mostly boiled).',
    'Lactic acid products, low-fat cottage cheese, and low-fat cheeses.',
    'Loose porridge (oatmeal, buckwheat, millet).',
    'Soups: vegetable vegetarian, porridge, dairy, fruit (taking into account the total amount of liquid consumed a day). Low-fat meat soups are recommended to be consumed no more than twice a week.',
    'Fruits, vegetables (fresh cabbage, sauerkraut, fresh cucumbers, tomatoes, zucchini, pumpkin) raw, boiled, in the form of vinaigrette, salads with vegetable oil.',
    'Foods, rich in potassium and magnesium (apricots, dried apricots, apples, and others).',
    'In case hypertension is caused by damage to the kidneys, adrenal glands, pancreas, artery system of the heart or other organs, additional complex drug treatment is required.'
]

RECOMMENDATION3 = [
    'Consume cocoa daily. It contains many Nutrients, magnesium and vitamins that lead to Toning blood vessels. Similar properties are possessed by Strong black tea.',
    'Include a lot of spices in your diet. Add spices to food, it helps to constrict blood vessels and increase the activity of the endocrine glands.',
    'Consume cocoa daily. It contains many Nutrients, magnesium and vitamins that lead to Toning blood vessels. Similar properties are possessed by Strong black tea.',
    'Dishes of fatty fish and caviar are recommended - at least 4 times a week.',
    'Include starchy foods such as potatoes, corn, buckwheat, rice, oats in the menu.',
    'Recommended eating vegetables and fruits, 500g daily.',
    'You need to eat greens every day, especially parsley and cilantro.',
    'Almost all varieties of nuts are allowed especially walnuts. The recommended rate is 30g a day.',
    'Fortified wine, sweet and semi-sweet, best made from red grapes. 50 ml is enough before eating.',
    'Recommended daily walks of at least 30 minutes or swimming or jogging. This allows you to keep blood vessels in good shape.'
]

class RecommendationEngine:
    """
    In a real world scenario this would be
    a controller to AI engine that 
    1. cleans up the data 
    2. passes it to AI engine
    3. return the response from AI engine
    """
    def get_recommendation(self, keys):
        metric = self.calculateRecommendationMetric(keys)

        data = switch(metric):
        case 1:
            {
            'risk' : RISK,
            'recommendation': RECOMMENDATION1
            }
        case 2:
            {
            'risk' : RISK,
            'recommendation': RECOMMENDATION2
            }
        case 3:
            {
            'risk' : RISK,
            'recommendation': RECOMMENDATION3
            }
        case 4:
            {
            'risk' : RISK,
            'recommendation': RECOMMENDATION4
            }
        case 5:
            {
            'risk' : RISK,
            'recommendation': RECOMMENDATION5
            }
        case 6:
            {
            'risk' : RISK,
            'recommendation': RECOMMENDATION6
            }
        case 7:
            {
            'risk' : RISK,
            'recommendation': RECOMMENDATION7
            }
        case 8:
            {
            'risk' : RISK,
            'recommendation': RECOMMENDATION8
            }
        case 9:
            {
            'risk' : RISK,
            'recommendation': RECOMMENDATION9
            }
        case 10:
            {
            'risk' : RISK,
            'recommendation': RECOMMENDATION10
            }

        return data