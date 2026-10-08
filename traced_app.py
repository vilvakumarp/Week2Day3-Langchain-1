import os
import time

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


# Load variables from .env
load_dotenv()


def main():

    # ---------------------------------------------------------
    # Check required environment variables
    # ---------------------------------------------------------
    required_vars = [
        "OPENAI_API_KEY",
        "LANGSMITH_API_KEY",
        "LANGSMITH_TRACING",
        "LANGSMITH_PROJECT",
    ]

    missing = [var for var in required_vars if not os.getenv(var)]

    if missing:
        print("ERROR: Missing environment variables:")
        for var in missing:
            print(f"  - {var}")
        print("\nPlease check your .env file.")
        return

    # ---------------------------------------------------------
    # Create LangChain ChatOpenAI model
    # ---------------------------------------------------------
    llm = ChatOpenAI(
        model="gpt-4o-mini"
    )

    # ---------------------------------------------------------
    # Three different prompts
    # ---------------------------------------------------------
    prompts = [
        "Explain Newton's first law in simple terms for a 12-year-old.",

        "Write a short Python function that checks whether a number is prime.",

        "what is capital of Russia?",
    ]

    print("=" * 70)
    print("LANGCHAIN + OPENAI + LANGSMITH TRACING")
    print("=" * 70)
    print(f"Project : {os.getenv('LANGSMITH_PROJECT')}")
    print(f"Model   : gpt-4o-mini")
    print(f"Tracing : {os.getenv('LANGSMITH_TRACING')}")
    print("=" * 70)

    # ---------------------------------------------------------
    # Run each prompt
    # ---------------------------------------------------------
    for i, prompt in enumerate(prompts, start=1):

        print(f"\n{'=' * 70}")
        print(f"RUN {i}")
        print(f"{'=' * 70}")

        print("\nPROMPT:")
        print(prompt)

        # Start latency timer
        start_time = time.perf_counter()

        # Send request to OpenAI through LangChain
        response = llm.invoke(prompt)

        # Stop latency timer
        end_time = time.perf_counter()

        latency = end_time - start_time

        # -----------------------------------------------------
        # Extract token usage
        # -----------------------------------------------------
        usage = response.usage_metadata

        input_tokens = usage.get("input_tokens", 0)
        output_tokens = usage.get("output_tokens", 0)
        total_tokens = usage.get("total_tokens", 0)

        # -----------------------------------------------------
        # Print answer
        # -----------------------------------------------------
        print("\nANSWER:")
        print(response.content)

        # -----------------------------------------------------
        # Print performance information
        # -----------------------------------------------------
        print("\n" + "-" * 70)
        print("RUN INFORMATION")
        print("-" * 70)

        print(f"Latency       : {latency:.2f} seconds")
        print(f"Input tokens  : {input_tokens}")
        print(f"Output tokens : {output_tokens}")
        print(f"Total tokens  : {total_tokens}")

        print("-" * 70)

    print("\nAll runs completed.")
    print(f"View traces in LangSmith project: {os.getenv('LANGSMITH_PROJECT')}")


if __name__ == "__main__":
    main()