import requests
import re

def Start(name):
    """
    Check if a TikTok username exists.
    
    Args:
        name: The username to check
        
    Returns:
        A list with platform name, validity status, and URL
    """

    url = f"https://www.tiktok.com/@{name}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.tiktok.com/",
    }
    
    try:
        response = requests.get(url, headers=headers)
        status_code = response.status_code
        
        # Check if redirected to error page or 404
        if status_code == 404:
            print_result(name, False)
            return ["TikTok", False, url]
            
        html_content = response.text

        # Used for checking if account exists.
        account_exists_indicators = [
            f'<h2 class="tiktok-arkop9-H2ShareTitle ekmpd5l5">@{name}</h2>',
            f'"uniqueId":"{name}"',
            f'"userInfo":',
            f'"shareDesc":'
        ]
        
        # Ditto.
        account_missing_indicators = [
            '<title>This page isn&#x27;t available</title>',
            "Couldn't find this account",
            'The page you were looking for couldn',
            '<h2 class="error-page">User not found</h2>'
        ]
        
        # Check for existence indicators
        for indicator in account_exists_indicators:
            if indicator.lower() in html_content.lower():
                return ["TikTok", True, url]
                
        # Then check for non-existence indicators
        for indicator in account_missing_indicators:
            if indicator.lower() in html_content.lower():
                return ["TikTok", False, url]
        
        # Check if username appears in content with follower info
        if f"@{name.lower()}" in html_content.lower() and "followers" in html_content.lower():
            return ["TikTok", True, url]
        
        # Fallback, look for common profile page elements
        if "follower" in html_content.lower() and "following" in html_content.lower() and "likes" in html_content.lower():
            return ["TikTok", True, url]
            
        # Check for patterns in meta tags
        meta_tags = re.findall(r'<meta property="og:title" content="(.*?)"', html_content)
        if meta_tags and name.lower() in meta_tags[0].lower():
            return ["TikTok", True, url]
            
        # Finally, default to considering it doesn't exist
        return ["TikTok", False, url]
        
    except Exception as e:
        # Handle any exceptions
        print(f"[ERROR] Error '{e}' occurred whilst checking platform 'TikTok'")
        return ["TikTok", False, url]
