import sounddevice as sd
from scipy.io.wavfile import write


def record_audio(duration, output_file):
    """
    Mikrofon girişini kaydeder ve bir .wav dosyasına kaydeder.

    Args:
        duration (int): Kaydedilecek sürenin uzunluğu (saniye).
        output_file (str): Kaydedilecek dosyanın adı.
    """
    try:
        print(f"{duration} saniye boyunca ses kaydediliyor...")
        fs = 44100  # Ses örnekleme frekansı (44.1 kHz)
        audio = sd.rec(int(duration * fs), samplerate=fs, channels=2)
        sd.wait()  # Kaydın tamamlanmasını bekle
        write(output_file, fs, audio)  # .wav dosyasına kaydet
        print(f"Ses kaydedildi: {output_file}")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")


def main():
    print("Ses Kaydedici Uygulaması")
    try:
        # Kullanıcıdan süre bilgisi al
        duration = int(input("Kaç saniye boyunca ses kaydedilsin? "))
        output_file = input("Kaydedilecek dosyanın adı (ör. kayit.wav): ").strip()

        # Ses kaydet
        record_audio(duration, output_file)
    except ValueError:
        print("Geçerli bir süre giriniz.")
    except Exception as e:
        print(f"Beklenmeyen bir hata oluştu: {e}")


if __name__ == "__main__":
    main()
