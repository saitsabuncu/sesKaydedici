# Ses Kaydedici Uygulaması

Bu Python uygulaması, kullanıcıların belirlenen süre boyunca mikrofon girişini kaydetmelerine olanak tanır. Kayıtlar, yüksek kaliteli stereo formatında `.wav` dosyası olarak saklanır.

## Özellikler

- Ses kaydını mikrofon aracılığıyla yapma
- Kayıtları `.wav` formatında kaydetme
- Kullanıcı tarafından belirlenen süre boyunca ses kaydı

## Kurulum

Projeyi yerel makinenizde çalıştırmak için:
1. Bu repoyu klonlayın veya indirin.
2. Gerekli kütüphaneleri yüklemek için terminalden aşağıdaki komutu çalıştırın:
   ```
   pip install sounddevice scipy
   ```

## Kullanım

Uygulamayı çalıştırmak için:
```
python main.py
```
Çalıştırdığınızda, kayıt süresini (saniye cinsinden) ve kaydedilecek dosya adını girmeniz istenir.

## Katkıda Bulunma

Projeye katkıda bulunmak isteyenler için pull request'ler kabul edilir. Büyük değişiklikler için, lütfen önce neyi değiştirmek istediğinizi tartışmak üzere bir konu açınız.

## Lisans

[MIT](https://choosealicense.com/licenses/mit/)
