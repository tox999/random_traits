# for name generator api you may use: https://github.com/skeeto/fantasyname/blob/master/js/namegen.js
from flask import Flask
from random import Random
import traits
import os

app = Flask(__name__)


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class HTMLColors:
    HEADER = '<span style="color: #5e81ac;">'
    OKBLUE = '<span style="color: #3e6ea5;">'
    OKGREEN = '<span style="color: #2e7d32;">'
    WARNING = '<span style="color: #f57f17;">'
    FAIL = '<span style="color: #d32f2f;">'
    ENDC = '</span>'
    BOLD = '<span style="font-weight: bold;">'
    UNDERLINE = '<span style="text-decoration: underline;">'


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def traits_string(generator,
                  trait_list,
                  number_of_traits=3,
                  color=Colors.FAIL,
                  sep=", ",
                  color_end_tag=Colors.ENDC):
    trait_list_copy = trait_list.copy()
    selected_traits = set()
    for _ in range(0, number_of_traits):
        trait = generator.choice(trait_list_copy)
        selected_traits.add(trait)
        trait_list_copy.remove(trait)

    result = sep.join(selected_traits)
    return f"{color}{result}{color_end_tag}"


def trait_generator_console(generator, seed, number_of_traits):
    iteration = 0
    while True:
        print("\n")
        print("Negative traits:")
        print(
            traits_string(generator, traits.negative, number_of_traits,
                          Colors.FAIL))
        print("Neutral traits:")
        print(
            traits_string(generator, traits.neutral, number_of_traits,
                          Colors.OKBLUE))
        print("Positive traits:")
        print(
            traits_string(generator, traits.positive, number_of_traits,
                          Colors.OKGREEN))
        print("\n")
        iteration += 1
        print("Generate another? (y/n)")
        answer = input("Answer: ")
        if answer.lower() in ["y", "yes", "ye", "", " ", None]:
            cls()
            print(f"Seed: {seed} \nIteration: {iteration}")
        else:
            break


def trait_generator_html(generator, seed, number_of_traits):
    iteration = 0
    separator = ", "
    while True:
        html = ""
        negative = traits_string(generator,
                                 traits.negative,
                                 number_of_traits,
                                 HTMLColors.FAIL,
                                 sep=separator,
                                 color_end_tag=HTMLColors.ENDC)
        neutral = traits_string(generator,
                                traits.neutral,
                                number_of_traits,
                                HTMLColors.OKBLUE,
                                sep=separator,
                                color_end_tag=HTMLColors.ENDC)
        positive = traits_string(generator,
                                 traits.positive,
                                 number_of_traits,
                                 HTMLColors.OKGREEN,
                                 sep=separator,
                                 color_end_tag=HTMLColors.ENDC)

        html += f"<p><strong>Negative traits:</strong><br />&nbsp;{negative}<br /></p>"
        html += f"<p><strong>Neutral traits:</strong><br />&nbsp;{neutral}<br /><p/>"
        html += f"<p><strong>Positive traits:</strong><br />&nbsp;{positive}<br /><p/>"

        iteration += 1
        html += f"<br />Refresh page to generate another traits.<br />Iteration: {iteration}, seed: {seed}"

        yield html


def main_console(*args, **kwargs):
    cls()
    while True:
        print("Welcome to random traits generator.")
        print(
            "Pick used for generation of random traits or press enter for generate it too."
        )
        seed = input("Seed: ")
        if seed == "":
            generator = Random()
        else:
            generator = Random(seed)

        print(
            "Choose number (int) of traits to generate, 3 is used if left blank."
        )
        number_of_traits = input("Number: ")
        try:
            number_of_traits = int(number_of_traits)
        except:
            number_of_traits = 3

        trait_generator(generator, seed, number_of_traits)


def main(*args, **kwargs):
    seed = kwargs.get("seed", None)
    number_of_traits = kwargs.get("number_of_traits", 3)
    generator = Random() if seed is None else Random(seed)

    trait_generator = trait_generator_html(generator, seed, number_of_traits)
    style = f"<html style='background-color:black; color:White; font: Noto-sans;'>"
    return f"{style}<h1>Random character traits:</h1>{next(trait_generator)}</html>"


@app.route('/')
def index():
    return main()


# if __name__ == "__main__":
# try:
#     main_console()
# except KeyboardInterrupt:
#     print("Goodbye!")

app.run(host='0.0.0.0', port=81)
