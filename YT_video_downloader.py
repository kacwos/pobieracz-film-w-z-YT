import os
from pytube import YouTube
from tqdm import tqdm

url = ""  # Wprowadź właściwy adres URL filmu
video = YouTube(url)
stream = video.streams.filter(only_audio=False).get_highest_resolution()

# Ustal długość pliku
file_size = stream.filesize

# Utwórz katalog, jeśli nie istnieje
output_directory = ""
os.makedirs(output_directory, exist_ok=True)

# Usuń niedozwolone znaki ze tytułu
cleaned_title = "".join(c for c in video.title if c.isalnum() or c in [' ', '.', '-'])

# Utwórz pasek postępu
progress_bar = tqdm(total=file_size, unit='B', unit_scale=True, unit_divisor=1024)

# Pobieraj bloki i zaktualizuj pasek postępu
def on_progress(chunk, file_handle, remaining):
    if isinstance(chunk, bytes):
        chunk = len(chunk)
    progress_bar.update(chunk)

# Ustaw funkcję postępu
stream.on_progress = on_progress

# Pobierz plik
stream.download(output_path=output_directory, filename=f'{cleaned_title}.mp4')

# Zamknij pasek postępu
progress_bar.close()
