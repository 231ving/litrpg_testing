"""
Characters have various body parts and organs.
Damage to 'higher' categories cascades down to varying degrees.
Each body part has their own health, defenses, and effectiveness.
    Head
        Eyes
        Ears
        Nose
        Brain
    Arms
        Hands
            Fingers
        Shoulders
        Upper Arm
        Lower Arm
    Torso
        Heart
        Lungs
        Stomach
    Legs
        Feet
            Toes
        Thighs
        Calves
        Ankles

Body Parts
    Attributes:
          Max Health
          Health
          Effectiveness = Health / Max Health
          Parent Parts = []
          Child Parts = []
          Connected Parts = []
          Organs = []
          Associated Actions = []
          Action Percentages = []
    Features
        Damage to Parent Part cascades down to Child Parts (But only 0.1x the Damage)
        As Parts take Damage, Character's overall Action Percentages get low (Action Percent * Effectiveness)
        If Effectiveness is 0, Associated Actions can't be performed with said Body Part anymore


Equipment belongs to various categories.
Effects of 'higher' categories cascades down to varying degrees.
Each category has their own characteristics.
    Weapon
        Swords
            Longswords
            Bastard Swords
            Greatswords
            Shortswords
            Scimitars
            Katanas
        Axes
        Polearms
            Spears
            Lances
            Halberds
            Poleaxes
            Pikes
        Bows
            Longbows
            Shortbows
            Hunting Bows
    Armor
        Head Armor
            Helmets
            Circlets
            Hoods
        Torso Armor
        Arm Armor
        Leg Armor
    Accessories
        Jewelry
            Necklaces
            Rings
            Earrings
        Belts
Skills have multiple Effects. Skills have certain characteristics.
    Base Magnitude
    Base Multiplier
    Modified Magnitude
    Modified Multiplier
    Other Skill Variables
    Title
    Description
    Level
Effects can have multiple Mechanisms. Effects have certain characteristics.
    Base Magnitude
    Base Multiplier
    Modified Magnitude
    Modified Multiplier
    Other Effect Variables
    Title
    Description
Mechanisms are the actual mechanical effects.
"""
