from youtube_comments import get_youtube_comments

# Replace with a real YouTube video URL
video_url = "https://youtu.be/qHF0bsT5SZw?si=ISqei_bnyDyz1U4R"

comments = get_youtube_comments(video_url, max_comments=20)

if comments:
    print(f"✅ Successfully fetched {len(comments)} comments!")
    print("\nSample Comments:")
    for c in comments[:5]:
        print("-", c)
else:
    print("❌ No comments found or the link is invalid!")

