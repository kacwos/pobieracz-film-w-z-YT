from pytube import YouTube

def download_highest_resolution_video(url, output_directory):
    try:
        video = YouTube(url)

        stream = video.streams.get_highest_resolution()

        stream.download(output_path=output_directory)

        print(f"Pobrano film w najwyższej rozdzielczości: {stream.title}")

    except Exception as e:
        print(f"Wystąpił błąd: {e}")


if __name__ == "__main__":
    url = input("podaj url: ")
    output_directory = "C:\\ściezka\\do\\miejsca\\zapisu"

    download_highest_resolution_video(url, output_directory)
