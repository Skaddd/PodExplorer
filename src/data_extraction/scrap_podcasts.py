import pytube
from pytube.exceptions import VideoUnavailable
import logging
import hashlib

logger = logging.getLogger(__name__)


def extract_podcast(
    youtube_video_link: str, saving_path: str = "./data/podcasts"
) -> None:
    """Extract Youtube podcast audio only.

    Args:
        youtube_video_link (str): url linking to a youtube video.
        saving_path (str, optional): saving path.
        Defaults to "./data/podcast".
    """
    pod = pytube.YouTube(youtube_video_link)
    logger.info("Downloading video...")
    try:
        # several reflexions needs when selecting the youtube stream
        # multiple language videos cannot be handled
        filename_md5 = (
            hashlib.md5(youtube_video_link.encode("utf-8")).hexdigest()
            + ".mp3"
        )
        pod.streams.filter(only_audio=True)[0].download(
            output_path=saving_path, filename=filename_md5
        )

    except VideoUnavailable:
        logger.info(f"{youtube_video_link} is not video, check the link given")


def scrap_podcast_channel(
    youtube_channel_link: str, saving_path: str = "./data/podcasts"
) -> None:
    """Extract All audios from a youtube channel.

    Args:
        youtube_video_link (str): url linking to a youtube video.
        saving_path (str, optional): saving path.
        Defaults to "./data/podcast".
    """

    pod_channel = pytube.Channel(youtube_channel_link)
    for podcast_video in pod_channel.videos:
        extract_podcast(
            youtube_video_link=podcast_video, saving_path=saving_path
        )


def scrap_podcast_playlist(
    youtube_playlist_link: str, saving_path: str = "./data/podcasts"
) -> None:
    """Extract all audios from a playlist.

    Args:
        youtube_video_link (str): url linking to a youtube video.
        saving_path (str, optional): saving path.
        Defaults to "./data/podcast".
    """
    pod_playlist = pytube.Playlist(youtube_playlist_link)
    for podcast_video in pod_playlist.videos:
        extract_podcast(
            youtube_video_link=podcast_video, saving_path=saving_path
        )
