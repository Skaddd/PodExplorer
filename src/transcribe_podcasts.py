from faster_whisper import WhisperModel
from pathlib import Path

import logging

logger = logging.getLogger(__name__)


# must add a dict
def loading_model(model_params):
    transcription_model = WhisperModel(**model_params)

    return transcription_model


def run_transcription(
    podcast_file: str, model_params: dict, beam_size: int = 5
):
    transcript_dict = {}
    try:
        whipser_model = loading_model(model_params)
        # could add a dict also
        segments, _ = whipser_model.transcribe(
            podcast_file,
            beam_size=beam_size,
            task="transcribe",
            language="en",
            without_timestamps=True,
            vad_filter=True,
            vad_parameters=dict(min_silence_duration_ms=400),
        )
        transcript_dict[Path(podcast_file).stem] = [
            segment.text for segment in segments
        ]
    except Exception:
        print("oui")
        logger.info(
            "--- The given file couldn't be transcribed"
            + "Check the file and its extension ---"
        )

    return transcript_dict
