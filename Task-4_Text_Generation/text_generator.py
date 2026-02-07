from transformers import pipeline

def generate_text(prompt):
    generator = pipeline("text-generation", model="gpt2")
    output = generator(prompt, max_length=150, num_return_sequences=1)
    return output[0]['generated_text']

def main():
    print("=== TEXT GENERATION TOOL ===")
    prompt = input("Enter your prompt: ")
    
    print("\nGenerating text...\n")
    result = generate_text(prompt)

    print("=== GENERATED TEXT ===")
    print(result)

if __name__ == "__main__":
    main()
