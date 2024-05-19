from transcribe_podcasts import run_transcription
import os


os.environ["KMP_DUPLICATE_LIB_OK"] = "True"
if __name__ == "__main__":
    model_params = {
        "model_size_or_path": "large-v3",
        "device": "cpu",
        "compute_type": "int8",
    }
    podcast_file = r"C:\Users\lebru\Documents\github_folder\PodExplorer\data\podcasts\fd01a7c0f1f22487251dfed5cd803b0c.mp3"
    final_dict = run_transcription(
        podcast_file=podcast_file, model_params=model_params, beam_size=5
    )
    print(final_dict)
