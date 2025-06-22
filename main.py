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

    # Generate plans
    annual_plans = agent.generate_annual_plans(long_term_goal)

    # Display plans
    if annual_plans:
        print("\nHere's your annual plan:")
        print(annual_plans)
    else:
        print("Could not generate annual plans. Please try again.")

    monthly_plan = agent.generate_monthly_plan(long_term_goal)
    if monthly_plan:
        print("\n---")
        print("\nHere's your monthly plan for the next 3 months:")
        print(monthly_plan)
    else:
        print("Could not generate monthly plan. Please try again.")
    daily_plan = agent.generate_daily_plan(long_term_goal)
    if daily_plan:
        print("\n---")
        print("\nHere's a sample daily plan:")
        print(daily_plan)
    else:
        print("Could not generate daily plan. Please try again.")

    short_term_goals = agent.generate_short_term_goals(long_term_goal)
    if short_term_goals:
        print("\n---")
        print("\nHere are some short-term goals to get you started:")
        print(short_term_goals)
    else:
        print("Could not generate short-term goals. Please try again.")

    habits = agent.build_habits(long_term_goal)
    if habits:
        print("\n---")
        print("\nHere's a system of habits to help you achieve your goal:")
        print(habits)
    else:
        print("Could not generate habits. Please try again.")

if __name__ == "__main__":
    main()