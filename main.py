import wave

from flask import Flask, request

app = Flask(__name__)

@app.route('/order', methods=['POST'])
def get_order():
    if request.headers['Content-Type'] == 'audio/wav':
        audio_data = request.data

        with wave.open('audio.wav', 'wb') as wav_file:
            wav_file.setnchannels(1)  # 单声道
            wav_file.setsampwidth(2)  # 16-bit 样本宽度
            wav_file.setframerate(16000)  # 采样率为 44100 Hz
            wav_file.writeframes(audio_data)
            print("wav file saved")

    else:
        print("Content-Type is not audio/wav")

@app.route('/test', methods=['GET'])
def test():
    print("test")

    return "www.google.com"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)