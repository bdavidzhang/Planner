import os
from dotenv import load_dotenv
from planner_agent import PlannerAgent

load_dotenv()

def main():
    deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
    openai_api_key = os.getenv("OPENAI_API_KEY")

    #default to deepseek
    if not deepseek_api_key:
        print("Error: DEEPSEEK_API_KEY not found in .env file.")
        return

    api_choice = 'deepseek'

    if api_choice == "openai":
        if not deepseek_api_key:
            print("Error: OPENAI_API_KEY not found in .env file. Falling back to DS.")
            agent = PlannerAgent(api_key=openai_api_key)
        else:
            agent = PlannerAgent(api_key=deepseek_api_key, api_base="https://api.deepseek.com")
    else: # Default to deepseek
        if not deepseek_api_key:
            print("Error: DEEPSEEK_API_KEY not found in .env file. Falling back to Chat.")
            agent = PlannerAgent(api_key=openai_api_key)
        else:
            agent = PlannerAgent(api_key=deepseek_api_key, api_base="https://api.deepseek.com")

    print("Welcome to the Planner Agent!")
    long_term_goal = input("Please enter your long-term goal (e.g., 'Become a successful entrepreneur in 5 years'): ")

    print(f"\nBreaking down your goal: '{long_term_goal}'")
    annual_plans = agent.generate_annual_plans(long_term_goal)
    habits = agent.build_habits(long_term_goal)

    if annual_plans:
        print("\nHere's your annual plan:")
        print(annual_plans)
    else:
        print("Could not generate annual plans. Please try again.")

    if habits:
        print("\n---")
        print("\nHere's a system of habits to help you achieve your goal:")
        print(habits)
    else:
        print("Could not generate habits. Please try again.")

if __name__ == "__main__":
    main()