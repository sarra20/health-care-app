def apply_safety_rules(response):

    disclaimer = """
    
    Avertissement :
Cette analyse est générée par une IA et ne remplace pas un avis médical professionnel.
Consultez un médecin en cas de doute.
"""

    return response.strip() + disclaimer