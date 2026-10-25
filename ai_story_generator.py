import random

def generate_story(name, animal, place):
stories = [
f"Once upon a time, {name} found a magical {animal} in {place}. "
f"They became best friends and went on an exciting adventure. "
f"Together, they helped everyone in the village and lived happily ever after.",

    f"One beautiful morning, {name} visited {place} and met a friendly {animal}. "
    f"The {animal} showed {name} a secret garden full of magical flowers. "
    f"They learned that kindness makes the world a better place."
]

return random.choice(stories)

print("================================")
print(" AI CHILDREN'S STORY GENERATOR ")
print("================================")

name = input("Enter the child's name: ")
animal = input("Enter an animal: ")
place = input("Enter a place: ")

print("\nYour Magical Story")
print("------------------")
print(generate_story(name, animal, place))

print("\nMoral: Always be kind and help others!")
