import json

with open("data.json", "r") as file:
    programs = json.load(file)

def show_intro():
    print("\n University Admissions Assistant")
    print("Ask about a program, like 'Computer Science' or 'Business Administration'.\n")

def get_program_info(query):
    key = query.title().strip()
    if key in programs:
        info = programs[key]
        print(f"\n Program: {key}")
        print(f" University: {info['university']}")
        print(f" Eligibility: {info['eligibility']}")
        print(f" Required Documents:")
        for doc in info["documents"]:
            print(f"  - {doc}")
        print(f" Deadline: {info['deadline']}\n")
    else:
        print("\n Sorry! Program not found in our database.\n")

def main():
    show_intro()
    while True:
        query = input(" Enter Program or type 'exit' to quit: ")
        if query.lower() == "exit":
            print("\n Thank you for using the Admissions Bot. Good luck! \n")
            break
        get_program_info(query)

if __name__ == "__main__":
    main()
