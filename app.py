from ai.generator import generate_structure_and_content
from builder.structure_builder import create_project_structure
from utils.printer import print_banner

def main():
    print_banner()
    idea = input("💡 Enter your million dollar idea: ")
    
    print("\n🧠 Thinking...\n")
    structure = generate_structure_and_content(idea)
    
    print("📁 Generating project...\n")
    create_project_structure(structure)
    
    print("\n✅ Done! Check your generated project folder.\n")

if __name__ == "__main__":
    main()
