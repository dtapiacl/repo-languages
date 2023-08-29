import requests

def fetch_languages(repo_url):
    # Replace {owner} and {repo} with the repository's owner and name
    api_url = f"https://api.github.com/repos/{repo_url}/languages"

    # Fetching the language data using GitHub API
    response = requests.get(api_url)
    if response.status_code != 200:
        print(f"Failed to get data: {response.status_code}")
        return None
    
    language_data = response.json()
    
    # Converting bytes to megabytes
    for lang, bytes_count in language_data.items():
        language_data[lang] = bytes_count / (1024 * 1024)
    
    return language_data

# Replace 'lsst-it/lsst-control' with the target repository
language_data = fetch_languages("lsst-it/lsst-control")

if language_data:
    total_megabytes = sum(language_data.values())
    total_gigabytes = total_megabytes / 1024
    print("Decoded Conversations:")
    for lang, megabytes in language_data.items():
        print(f"{lang} with {megabytes:.2f} megabytes of code.")
    print(f"Total gigabytes of code: {total_gigabytes:.2f}")