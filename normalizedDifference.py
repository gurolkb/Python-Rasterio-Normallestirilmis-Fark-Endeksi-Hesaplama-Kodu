import rasterio
from rasterio.plot import show

# Endeks hesabı yapacağımız görüntünün açılma işlemi
path = '..\Images\example.tif'
image = rasterio.open(path)

# normalleştirilmiş fark hesabı = (firstBand-secondBand)/(firstBand+secondBand) #

# İlk bant numarasının kullanıcı tarafından girilmesi
firstInt = int(input('İlk bant numarasını seçiniz:'))
firstBand = image.read(firstInt)

# İkinci bant numarasının kullanıcı tarafından girilmesi
secondInt = int(input('İkinci bant numarasını seçiniz:'))
secondBand = image.read(secondInt)

# Normalleştirilmiş fark endeksi hesabı
normalizedDifference = ((firstBand - secondBand) / (firstBand + secondBand))

# Hesaplanan Endeks görüntüsünün belirtilen konuma kaydedilmesi
profile = image.profile
profile.update(nodata=0, count=1, dtype=rasterio.float64)
with rasterio.open('../Images/normalizedDifference.tif', 'w', **profile) as dst:
    dst.write(normalizedDifference.astype(rasterio.float64), 1)

# Endeks görüntüsünün görselleştirilmesi
show(normalizedDifference, cmap="Spectral")
