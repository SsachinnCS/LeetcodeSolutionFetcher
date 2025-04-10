import requests

# Base raw GitHub URL
BASE_URL = "https://raw.githubusercontent.com/kamyu104/LeetCode-Solutions/master/C++/"

def fetch_github_code(question_slug):
    """
    Fetch the C++ solution code for a given LeetCode question slug.
    Example input: '132-pattern'
    """
    formatted_slug = question_slug.strip() + ".cpp"
    full_url = BASE_URL + formatted_slug

    try:
        response = requests.get(full_url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"\n❌ File not found or not available for '{question_slug}'.")
            print(f"URL tried: {full_url}")
            return None
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        return None

def main():
    print("🔍 Enter the LeetCode question name in kebab-case format (lowercase words separated by dashes).")
    print("   For example:")
    print("   ➤ 'Add Two Numbers' → 'add-two-numbers'")
    print("   ➤ '3Sum Closest' → '3sum-closest'\n")

    question_name = input("Enter the formatted question name: ").strip()
    code = fetch_github_code(question_name)
    
    if code:
        print("\n✅ Code fetched successfully:\n")
        print(code)

if __name__ == "__main__":
    main()
