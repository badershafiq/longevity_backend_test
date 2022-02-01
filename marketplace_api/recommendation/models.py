from django.db import models

# Create your models here.
class Recommendation(models.Model):
    fields = models.ListField()

def getRecommendation(self, data):
    keys = data.keys()
    required_keys = []
    for field in self.fields:
        if field in keys:
            required_keys.append(field)

    engine = RecommendationEngine()
    engine.get_recommendation(required_keys)
