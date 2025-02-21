from pydub import AudioSegment

def convert_m4a_to_mp3(m4a_file_path, mp3_file_path):
    m4a_file = AudioSegment.from_file(m4a_file_path, format="m4a")
    # Export as MP3
    m4a_file.export(mp3_file_path, format="mp3")