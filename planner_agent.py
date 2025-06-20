from openai import OpenAI

class PlannerAgent:
    def __init__(self, api_key: str, api_base: str = None):
        self.client = OpenAI(api_key=api_key, base_url=api_base)
        self.default_model = "gpt-3.5-turbo" if api_base is None else "deepseek-chat"

    def generate_annual_plans(self, long_term_goal: str) -> dict:
        prompt = f"""You are a highly intelligent and strategic planner. Your task is to take a long-term goal and break it down into annual plans, highlighting what needs to be accomplished each year to achieve the overall goal. Provide a detailed, actionable plan for each year.

Long-term Goal: {long_term_goal}

Provide the output in a structured format, indicating each year and its corresponding plan. For example:

Year 1:
- [Actionable item 1]
- [Actionable item 2]

Year 2:
- [Actionable item 1]
- [Actionable item 2]

...and so on.

Ensure the plan is realistic, progressive, and clearly outlines milestones for each year. The plan should span a reasonable number of years to achieve the goal, typically between 3 to 10 years, unless the goal explicitly suggests a different timeframe.
"""

       
        response = self.client.chat.completions.create(
            model=self.default_model,  # Use the default model based on API choice
            messages=[
                {"role": "system", "content": "You are a helpful assistant that creates annual plans."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1500
        )
        
        plan_text = response.choices[0].message.content
        return  plan_text

    def build_habits(self, goal: str) -> str:

        prompt = f"""You are an expert in habit formation, inspired by principles from 'Atomic Habits'. Given a specific goal, your task is to outline a system of habits that, if consistently followed, will lead the user to achieve that goal. Focus on actionable, small, and consistent habits.

Goal: {goal}

Provide a clear, concise list of habits, categorized if necessary, and explain briefly how each habit contributes to the goal. Consider the four laws of behavior change: Make it obvious, Make it attractive, Make it easy, Make it satisfying.
"""

        try:
            response = self.client.chat.completions.create(
                model=self.default_model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that creates habit systems."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1000
            )
            return response.choices[0].message.content

        except Exception as e:
            print(f"An error occurred while building habits: {e}")
            return "Could not generate habits."

        
            return {}
