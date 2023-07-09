import pandas
bitmap = []
bitmap_2 = []

class Bitmap():
    def __init__(self,r,g,b,row,column,my_sum):
        self.r = int(r)
        self.g = int(g)
        self.b = int(b)
        self.row = row
        self.column = column
        self.my_sum = my_sum

    def __str__(self):
        return f'R:{self.r} G: {self.g} B:{self.b} - Sor: {self.row} - Oszlop: {self.column} Szín_össz: {self.my_sum}'

    def hatar(self):
        diff_list = []
        for index,data in enumerate(bitmap_2[1:]):
            if bitmap_2[index].b - bitmap_2[index-1].b > 10:
                diff = (bitmap_2[index],True)
                diff_list.append(diff)
        return diff_list

with open('kep.txt', 'r', encoding='utf8') as read_rgb:
    full_data = read_rgb.readlines()
    lines = [i.strip().split(' ') for i in full_data]


#print(len(lines[0][0].split(' ')))
my_line = 0
lowest_dark_pixel = 999
light_pix_counter = 0

for index_1, row in enumerate(lines):
    bitmap.append([])
    #print(row)
    counter = 0
    instant_list = []
    cl_list = []    #osztályhoz a megfelelő sorrendekbe begyűjtöm az adatot
    for i in range(640):
        for j in row[counter:counter+3]:
            instant_list.append(int(j))
            cl_list.append(j)
        cl_list.append(index_1+1)
        cl_list.append(i+1)
        cl_list.append(sum(instant_list))

        if sum(instant_list) < lowest_dark_pixel:
            lowest_dark_pixel = sum(instant_list)
        if sum(instant_list) > 600:
            light_pix_counter += 1

        bitmap_2.append(Bitmap(*cl_list)) # osztályba rendezés
        cl_list = []
        #bitmap[my_line].append(instant_list)
        instant_list = []
        counter += 3
    my_line += 1


print('2. feladat:\nKérem egy képpont adatait!')
sor_beker = int(input('Sor:'))
oszlop_beker = int(input('Oszlop:'))
for i in bitmap_2:
    if int(sor_beker)+1 == i.row and int(oszlop_beker+1) == i.column:
        print(f'A képpont színe: RGB('
              f'{i.r},'
              f'{i.g},'
              f'{i.b}'
              f')')

print(f'3. feladat:\nA világos képpontok száma: {light_pix_counter}')

dark_pixels_list = []
for i in bitmap_2:
    if i.my_sum == lowest_dark_pixel:
        dark_pixels_list.append(i)

print(f'4. feladat:\nAlegsötétebb pont RGB összege: {lowest_dark_pixel}'
      f'\nA legsötétebb pixelek színe:')
for i in dark_pixels_list:
    print(f'RGB ({i.r},{i.g},{i.b})')

my_hatar = Bitmap.hatar(self=bitmap_2)
print(f'6. feladat\nA felhő legfelső sora: {my_hatar[0][0].row}\nA felhő legalsó sora: {my_hatar[-1][0].row}')
