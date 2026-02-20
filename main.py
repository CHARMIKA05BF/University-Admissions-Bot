import json
import os


class UniversityAdmissionsBot:
    def __init__(self, data_file="data.json"):
        self.data_file = data_file
        self.programs = self.load_data()

    def load_data(self):
        """Load program data from JSON file"""
        if not os.path.exists(self.data_file):
            print(" Data file not found. Please ensure data.json exists.")
            return {}

        with open(self.data_file, "r", encoding="utf-8") as file:
            return json.load(file)

    def show_welcome(self):
        """Display welcome message"""
        print("=" * 50)
        print(" Welcome to University Admissions Bot")
        print("=" * 50)
        print("I can help you with:")
        print("• Program requirements")
        print("• Eligibility criteria")
        print("• Required documents")
        print("• Application deadlines")
        print("\nType a program name to get details.")
        print("Type 'list' to see available programs.")
        print("Type 'exit' to quit the bot.\n")

    def list_programs(self):
        """Show available programs"""
        if not self.programs:
            print("No programs available in the database.\n")
            return

        print("\n📚 Available Programs:")
        for program in self.programs.keys():
            print(f"• {program}")
        print()

    def get_program_info(self, program_name):
        """Fetch and display program information"""
        program_key = program_name.strip().title()

        if program_key in self.programs:
            info = self.programs[program_key]

            print("\n" + "=" * 50)
            print(f" Program: {program_key}")
            print("=" * 50)
            print(f" University: {info.get('university', 'N/A')}")
            print(f" Eligibility: {info.get('eligibility', 'N/A')}")
            print(f" Application Deadline: {info.get('deadline', 'N/A')}")

            print("\n🗂 Required Documents:")
            documents = info.get("documents", [])
            if documents:
                for doc in documents:
                    print(f"  - {doc}")
            else:
                print("  No document details available.")
            print()
        else:
            print("\n Sorry, the program was not found in our database.")
            print("Try typing 'list' to see available programs.\n")

    def run(self):
        """Main chatbot loop"""
        self.show_welcome()

        while True:
            user_input = input("💬 Enter your query: ").strip().lower()

            if user_input == "exit":
                print("\n Thank you for using the University Admissions Bot!")
                print("Good luck with your admissions journey! ")
                break

            elif user_input == "list":
                self.list_programs()

            elif user_input == "":
                print("⚠️ Please enter a valid program name.\n")

            else:
                self.get_program_info(user_input)


if __name__ == "__main__":
    bot = UniversityAdmissionsBot()
    bot.run()
