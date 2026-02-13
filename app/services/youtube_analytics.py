import requests
from app.core.config import settings

class YouTubeService:
    def __init__(self):
        self.api_key = settings.YOUTUBE_API_KEY
        self.base_url = "https://www.googleapis.com/youtube/v3"

    def get_video_stats(self, video_id: str) -> dict | None:
        if not self.api_key:
            return None
        url = f"{self.base_url}/videos"
        params = {"part": "statistics,snippet", "id": video_id, "key": self.api_key}
        try:
            resp = requests.get(url, params=params, timeout=10)
            resp.raise_for_status()
            data = resp.json()
            items = data.get("items", [])
            if items:
                stats = items[0].get("statistics", {})
                snippet = items[0].get("snippet", {})
                return {
                    "title": snippet.get("title"),
                    "published_at": snippet.get("publishedAt"),
                    "views": int(stats.get("viewCount", 0)),
                    "likes": int(stats.get("likeCount", 0)),
                    "comments": int(stats.get("commentCount", 0))
                }
        except Exception as e:
            print(f"YouTube API error: {e}")
        return None