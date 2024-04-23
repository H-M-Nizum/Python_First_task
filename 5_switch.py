def switch_statement(option):
    match option:
        case "Javascript" | "Python" | "Go" | "Java" | "Kotlin" | "PHP" | "Swift" | "R" | "Ruby" | "C" | "Rust" | "Perl" | "C++" | "C#":
            print(f"{option} is a Programming language.")
        case "React" | "Angular" | "Vue" | "Svelte" | "Foundation" | "Preact":
            print(f"{option} is a Frontend Framework.")
        case "Django" | "Spring" | "Express.js" | "Laravel" | "Nest.js" | "Flask" | "Phoenix":
            print(f"{option} is a Backend Framework.")
        case _:
            print("That's not a valid option of the stack.")

if __name__ == "__main__":
    option = input("Enter the programming language or framework name : ")
    switch_statement(option.capitalize())
