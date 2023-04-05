# Python Rasterio Normalleştirilmiş Fark Endeksi Hesaplama Kodu
 
Bu kod dosya yoluna yüklenen .tif uzantılı uydu görüntüleri ve hava fotoğraflarının kullanıcı tarafından seçilen bantları arasında Normalleştirilmiş Fark Endeksleri hesaplamasını sağlar. Kod **Rasterio** kütüphanesi ile çalıştığından, çalıştırmak için **Rasterio** kütüphanesinin yüklü olması gerekmektedir.

Örnek bir çalışma olarak Images\example.tif dosyasının 4 numaralı yakın kızılötesi (NIR) ve 3 numaralı kırmızı (RED) bantları arasında yapılan işlem sonucu **NDVI** (Normalleştirilmiş Fark Vejetasyon Endeksi) elde edilmiştir.

Görüntünün işlemden önceki RGB görselleştirilmesi ve işlemden sonraki renkli görselleştirilmesi:
![Figure_1](https://user-images.githubusercontent.com/129385033/229290921-44780211-d289-414e-901d-9ca762e4b5f6.png)

![Figure_2](https://user-images.githubusercontent.com/129385033/229291054-1121fdc1-d330-493b-ab59-4d630ca9e44b.png)
