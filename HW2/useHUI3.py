import HUI3 as eq

print("Score for 'perfect' health: [1,1,1,1,1,1,1,1]")
print(eq.scoreHUI3(vision=1, hearing=1, speech=1, ambulation=1, dexterity=1, emotion=1, cognition=1, pain=1))

print("Score for potential patient: [5,4,3,2,1,2,3,4]")
print(eq.scoreHUI3(vision=5, hearing=4, speech=3, ambulation=2, dexterity=1, emotion=2, cognition=3, pain=4))
