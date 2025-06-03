from pytube import YouTube
from pytube.exceptions import (
    AgeRestrictedError, LiveStreamError, MaxRetriesExceeded, MembersOnly,
    PytubeError, RecordingUnavailable, RegexMatchError, VideoPrivate,
    VideoRegionBlocked, VideoUnavailable
)

def download_video():
    print("--- YouTube Video Downloader ---")
    print("Welcome! Please follow the prompts to download a video.")
    video_url = input("Enter the YouTube video URL (e.g., https://www.youtube.com/watch?v=dQw4w9WgXcQ): ")

    try:
        yt = YouTube(video_url, on_progress_callback=on_progress)
    except RegexMatchError:
        print("Invalid YouTube URL format. Please enter a valid URL (e.g., https://www.youtube.com/watch?v=...).")
        return
    except VideoUnavailable:
        print(f"The video at {video_url} is unavailable. This could be due to deletion, privacy settings, or regional restrictions.")
        return
    except AgeRestrictedError:
        print(f"The video at {video_url} is age-restricted and cannot be accessed without logging in or age verification.")
        return
    except LiveStreamError:
        print(f"The video at {video_url} is a live stream and cannot be downloaded directly with this script.")
        return
    except VideoPrivate:
        print(f"The video at {video_url} is private.")
        return
    except MembersOnly:
        print(f"The video at {video_url} is for members only.")
        return
    except RecordingUnavailable:
         print(f"The video at {video_url} is a recording that is not yet available.")
         return
    except VideoRegionBlocked:
        print(f"The video at {video_url} is blocked in your region.")
        return
    except MaxRetriesExceeded:
        print(f"Maximum retries exceeded while trying to fetch video data for {video_url}. Check your connection or try again later.")
        return
    except PytubeError as e: # Catch other generic Pytube errors
        print(f"A Pytube library error occurred: {e}")
        return
    except Exception as e: # Catch any other unexpected error
        print(f"An unexpected error occurred while accessing the video: {e}")
        return

    print(f"Title: {yt.title}")
    print(f"Views: {yt.views}")

    print("\nAvailable Streams:")
    streams = yt.streams.filter(progressive=True).order_by('resolution').desc()
    for i, stream in enumerate(streams):
        print(f"{i+1}. Resolution: {stream.resolution}, Type: {stream.mime_type}, FPS: {stream.fps}")

    selected_stream = None
    if not streams:
        print("No suitable downloadable streams found for this video.")
        return

    while True:
        try:
            stream_choice_input = input(f"Enter the number of the stream you want to download (1-{len(streams)}): ")
            if not stream_choice_input: # Handle empty input
                print("No input detected. Please enter a number.")
                continue
            stream_choice = int(stream_choice_input)
            if 1 <= stream_choice <= len(streams):
                selected_stream = streams[stream_choice-1]
                break
            else:
                print(f"Invalid choice. Please enter a number between 1 and {len(streams)}.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")
        except Exception as e: # Catch any other unexpected error during selection
            print(f"An unexpected error occurred during stream selection: {e}")
            return # Exit if unexpected error occurs


    print(f"Downloading: {yt.title} in {selected_stream.resolution}...")
    try:
        selected_stream.download()
        print("\nDownload complete!") # Added newline for better formatting after progress indicator
    except FileExistsError:
        print("\nError: A file with the same name already exists in the download location.")
    except ConnectionError:
        print("\nError: A network connection error occurred. Please check your internet connection.")
    except TimeoutError:
        print("\nError: The download timed out. Please try again.")
    except Exception as e:
        print(f"\nAn unexpected error occurred during download: {e}")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(f"{percentage_of_completion:.2f}% downloaded", end='\r')

if __name__ == "__main__":
    while True:
        download_video()
        another = input("\nDo you want to download another video? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Exiting downloader. Goodbye!")
            break
        print("\n") # Add a newline for spacing if they continue
