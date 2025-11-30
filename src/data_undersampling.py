import pandas as pd
import argparse
import sys

HUMAN_LABEL = "Human"

def balance_dataset(input_path, output_path="train_undersampling.parquet"):
    # Load dataset
    try:
        df = pd.read_parquet(input_path)
    except Exception as e:
        print(f"Error loading parquet: {e}")
        sys.exit(1)

    # Split Human vs LLM
    df_human = df[df["generator"] == HUMAN_LABEL]
    df_llm   = df[df["generator"] != HUMAN_LABEL]

    num_llm = len(df_llm)

    print("LLM total samples:", num_llm)
    print("Human total samples:", len(df_human))

    if len(df_human) < num_llm:
        print("Warning: Not enough Human samples to undersample!")
        print("Human:", len(df_human), "LLM:", num_llm)
        print("No undersampling performed.")
        df_balanced = df.copy()
    else:
        # Undersample Human to match LLM count
        df_human_sampled = df_human.sample(n=num_llm, random_state=42)

        # Combine & shuffle
        df_balanced = pd.concat([df_human_sampled, df_llm]) \
            .sample(frac=1, random_state=42) \
            .reset_index(drop=True)

    print("Balanced Human samples:", len(df_balanced[df_balanced["generator"] == HUMAN_LABEL]))
    print("Balanced LLM samples:", len(df_balanced[df_balanced["generator"] != HUMAN_LABEL]))
    print("Total balanced samples:", len(df_balanced))

    # Save
    df_balanced.to_parquet(output_path)
    print(f"Balanced dataset saved to: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Undersample Human class to match LLM samples")
    parser.add_argument("--input", default="data/train.parquet", required=True, help="Path to input parquet file")
    parser.add_argument("--output", default="data/train_undersampling.parquet", help="Output parquet path")

    args = parser.parse_args()

    balance_dataset(args.input, args.output)
