import os
from pydub import AudioSegment

def split_audio(input_file, output_dir, segment_length=20000):
    ## カレントディレクトリのinput_fileを読み込む
    audio = AudioSegment.from_wav(input_file)

    # 出力ディレクトリが存在しなければ作成する
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    i = 1
    start_time = 0

    while start_time < len(audio):
        end_time = start_time + segment_length
        segment = audio[start_time:end_time]
        output_file = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(input_file))[0]}_{i}.wav")
        segment.export(output_file, format="wav")

        start_time = end_time
        i += 1

if __name__ == "__main__":
    for i in range(1, 5):
        input_file = f"input{i}.wav"
        output_dir = "split"
        split_audio(input_file, output_dir)