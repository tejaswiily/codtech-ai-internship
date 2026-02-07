from transformers import pipeline

def summarize_text(text, max_len, min_len):
    """
    Summarizes the given text using a pre-trained NLP model.
    text      : The input text to summarize
    max_len   : Maximum words/sentences in summary
    min_len   : Minimum length of summary
    """
    summarizer = pipeline("summarization")
    # Load pre-trained summarization model

    summary = summarizer(
        text,
        max_length=max_len,
        min_length=min_len,
        do_sample=False
    )

    return summary[0]['summary_text']


def main():
    print("===========================================")
    print("        TEXT SUMMARIZATION TOOL")
    print("===========================================")
    print("Paste your text below.")
    print("When you finish, type END on a NEW LINE and press Enter.\n")

    # --- Multi-Line Input Handling ---
    lines = []
    while True:
        line = input()
        if line.strip() == "END":     # Stop when user types END
            break
        lines.append(line)

    text = "\n".join(lines)           # Combine lines into one string

    # --- User chooses summary length ---
    print("\nEnter summary length preferences:")
    max_len = int(input("Maximum summary length (e.g., 80): "))
    min_len = int(input("Minimum summary length (e.g., 30): "))

    # --- Generate Summary ---
    print("\nGenerating summary... Please wait...\n")
    summary = summarize_text(text, max_len, min_len)

    # --- Final Output ---
    print("============= SUMMARY =============")
    print(summary)
    print("===================================")


# Run program
if __name__ == "__main__":
    main()
