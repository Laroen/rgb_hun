import pandas
import numpy


def hatar(array):
    differents = []
    for i_1,d_1 in enumerate(array):
        for i_2,d_2 in enumerate(d_1[1:]):
            diff = d_2[2] - d_1[i_2-1][2]
            if diff > 10:
                my_tup = (i_1,diff,True)
                differents.append(my_tup)
    return differents

my_data = pandas.read_csv('kep.txt', header=None, sep=' ')

np_tomb = numpy.array(my_data)
rgb_data = []
ossz = []
for i in np_tomb:
    my_array = numpy.split(i,640)
    new = []
    for i in my_array:
        new.append(sum(i))
    rgb_data.append(my_array)
    ossz.append(new)

my_data_2 = pandas.DataFrame(rgb_data)
ossz_df = pandas.DataFrame(ossz)

legkisebb = min(ossz_df.min())
#print(legkisebb)
#no_nans = ossz_df.loc[legkisebb[1]]

blue = my_data_2.where(ossz_df == legkisebb) # az RGB-s kódokból kinyeri a legsötétebbet, és a nullás értékeket feltölti
#for i in blue:
print(blue[blue.notnull()].axes)

'''
#feladat 2
print('2. feladat:\nKérem egy képpont adatait!')
sor_beker = int(input('Sor:'))
oszlop_beker = int(input('Oszlop:'))
print(f'A képpont színe: RGB('
      f'{rgb_data[sor_beker - 1][oszlop_beker - 1][0]},'
      f'{rgb_data[sor_beker - 1][oszlop_beker - 1][1]},'
      f'{rgb_data[sor_beker - 1][oszlop_beker - 1][2]}'
      f')')

#feladat 3
light_pixels_number = 0
lowest_dark_pixel = 600
for index_1, data_1 in enumerate(rgb_data):
    for index_2, data_2 in enumerate(data_1):
        if sum(data_2) > 600:
            light_pixels_number += 1
        if sum(data_2) < lowest_dark_pixel:
            lowest_dark_pixel = sum(data_2)

print(f'3. feladat:\nA világos képpontok száma: {light_pixels_number}')

# feladat 4
dark_pixels_list = []
for index_1, data_1 in enumerate(rgb_data):
    for index_2, data_2 in enumerate(data_1):
        if sum(data_2) == lowest_dark_pixel:
            dark_pixels_list.append(data_2)

print(f'4. feladat:\nAlegsötétebb pont RGB összege: {lowest_dark_pixel}'
      f'\nA legstötétebb pixelek színe:')
for i in dark_pixels_list:
    print(f'RGB ({i[0]},{i[1]},{i[2]})')

#6. feladat
my_diff_lines = hatar(rgb_data)
print(f'6. feladat\nA felhő legfelső sora: {my_diff_lines[0][0]}\nA felhő legalsó sora: {my_diff_lines[-1][0]}')
'''
