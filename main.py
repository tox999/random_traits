# for name generator api you may use: https://github.com/skeeto/fantasyname/blob/master/js/namegen.js

from random import Random
import traits
import os

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def traits_string(generator, trait_list, number_of_traits=3, color=Colors.FAIL, sep=", "):
  trait_list_copy = trait_list.copy()
  selected_traits = set()
  for _ in range(0, number_of_traits):
    trait = generator.choice(trait_list_copy)
    selected_traits.add(trait)
    trait_list_copy.remove(trait)

  result = ", ".join(selected_traits)
  return f"{color}{result}{Colors.ENDC}"

def trait_generator(generator, seed, number_of_traits):
  iteration = 0
  while True:
    print("\n")
    print("Negative traits:")
    print(traits_string(generator,traits.negative, number_of_traits, Colors.FAIL))
    print("Neutral traits:")
    print(traits_string(generator,traits.neutral, number_of_traits, Colors.OKBLUE))
    print("Positive traits:")
    print(traits_string(generator,traits.positive, number_of_traits, Colors.OKGREEN))    
    print("\n")
    iteration += 1
    print("Generate another? (y/n)")    
    answer = input("Answer: ")
    if answer.lower() in ["y", "yes", "ye", "", " ", None]:
      cls()
      print(f"Seed: {seed} \nIteration: {iteration}")
    else:
      break

def main(*args, **kwargs):
  cls()
  while True:
    print("Welcome to random traits generator.")
    print("Pick used for generation of random traits or press enter for generate it too.")
    seed = input("Seed: ")
    if seed == "":
      generator = Random()
    else:
      generator = Random(seed)
    
    print("Choose number (int) of traits to generate, 3 is used if left blank.")
    number_of_traits = input("Number: ")
    try:
      number_of_traits = int(number_of_traits)
    except:
      number_of_traits = 3
    
    trait_generator(generator, seed, number_of_traits)



if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    print("Goodbye!")