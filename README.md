# Planner Agent

This project aims to build a planner agent that can break down a long-term goal (multiple years) into annual plans, highlighting what to accomplish each year.

## Features
- Breaks down long-term goals into annual plans.
- Highlights key accomplishments for each year.
- Client-flexible OpenAI API integration.

## Setup

### Prerequisites
- Python 3.x
- pip

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/planner-agent.git
   cd planner-agent
   ```
2. Create a virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration
Create a `.env` file in the root directory and add your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

Run the main script:

```bash
python main.py
```

Follow the prompts to input your long-term goal.