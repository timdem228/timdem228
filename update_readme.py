import random
import re

facts = [
    "no",
    "#1 femboy in world",
    "idi nahuy",
    "ilovesweatyfemboys123",
    "Firefox is your default browser. Good boy.",
    "bebebbebebebe",
    "lol",
    "nah",
    "bruh",
    "faaaaah",
    "ahhhh...",
    "my friend",
    "my husbend",
    "vtf",
    "lalalalalalala",
    "pls fuck me",
    "i love you",
    "hmmmm... nikwonder",
    "fuck u!",
    "what?",
    "piva",
    "also try shitshell!",
    "alt + f4",
    "nikike = gay",
    "google pixel 9 xl",
    "nikike na vas letit vanaya",
    "go to peak?",
    "idk",
    "uwu",
    ":3",
    "nikwonder.by",
]

random_fact = random.choice(facts)
print("Selected fact:", random_fact)

with open("README.md", "r", encoding="utf-8") as file:
    readme_content = file.read()

pattern = r'(⚡ \*\*Fun fact\*\*: \[).*?(\]\(https://nikwonder\.ru\)<br>)'

def repl(m):
    return f"{m.group(1)}{random_fact}{m.group(2)}"

new_content, count = re.subn(pattern, repl, readme_content, flags=re.S)

if count == 0:
    print("Warning: pattern not found in README.md — проверьте, совпадает ли текст (⚡ **Fun fact**: [ ... ](https://nikwonder.ru)<br>)")

with open("README.md", "w", encoding="utf-8") as file:
    file.write(new_content)
