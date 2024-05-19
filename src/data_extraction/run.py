from scrap_podcasts import extract_podcast

if __name__ == "__main__":
    url_podcast = "https://www.youtube.com/watch?v=wjZofJX0v4M"
    saving_path = "./data/podcast"

    extract_podcast(youtube_link=url_podcast, saving_path=saving_path)
