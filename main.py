from Completion import get_best_k_completions
from Initialization import init

if __name__ == '__main__':
    print("Loading the file and preparing the system...")
    d = init("C:/Users/rinat/Desktop/2021-archive/RFC/set.txt")

    text = input("The system is ready. Enter your text:\n")
    while text.find("#") == -1:
        li = get_best_k_completions(text, d)
        index = 1
        print("Here are 5 suggestion: ")
        if li:
            for i in li:
                print(str(index) + ". ", end=" ")
                i.print_suggest()
                index += 1
        print(text, end=" ")
        text += " "
        text += input()
