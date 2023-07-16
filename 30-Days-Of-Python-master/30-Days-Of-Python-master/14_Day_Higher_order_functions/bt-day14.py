            #LEVEL 1
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#bài tập 1
'''Có ba phương thức filter(), map(), và reduce() trong Python, được sử dụng cho các mục đích khác nhau:

filter():
Sử dụng để lọc ra các phần tử từ một chuỗi hoặc danh sách dựa trên một điều kiện được xác định trước.
Kết quả trả về là các phần tử mà điều kiện làm đúng (trả về giá trị True).
Đối tượng trả về là một đối tượng filter.
Sử dụng với hàm lambda hoặc hàm xử lý trả về giá trị boolean.
map():
Sử dụng để ánh xạ (map) các phần tử từ một chuỗi hoặc danh sách sang một chuỗi hoặc danh sách khác thông qua một hàm xử lý đã được xác định trước.
Kết quả trả về là kết quả của hàm xử lý được áp dụng cho từng phần tử.
Đối tượng trả về là một đối tượng map.
Sử dụng với hàm lambda hoặc hàm xử lý.
reduce():
Sử dụng để áp dụng một hàm xử lý tuần tự cho các phần tử của một chuỗi hoặc danh sách để thu gọn (reduce) chúng thành một giá trị duy nhất.
Kết quả trả về là một giá trị duy nhất.
Đối tượng trả về là kết quả sau khi áp dụng tuần tự hàm xử lý lên từng cặp phần tử.
Sử dụng với hàm lambda hoặc hàm xử lý nhận hai đối số và trả về kết quả của phép tổ hợp giữa hai đối số.
Tóm lại, filter() được sử dụng để lọc các phần tử dựa trên một điều kiện, map() được sử dụng để ánh xạ các phần tử sang một chuỗi hoặc danh sách khác, và reduce() được sử dụng để thu gọn (reduce) các phần tử thành một giá trị duy nhất.
'''

#bài tập 2
'''
Higher-order function (hàm bậc cao):
Là một hàm có khả năng nhận một hàm khác làm đối số hoặc trả về một hàm khác.
Hàm bậc cao cho phép chúng ta làm việc với hàm như một đối tượng, gán chúng vào biến, truyền chúng như đối số hoặc trả về chúng từ một hàm khác.
Ví dụ: map(), filter(), và reduce() là các hàm bậc cao trong Python.
Closure (đóng gói):
Là một hàm được tạo ra bởi một hàm khác và giữ lại môi trường (biến cục bộ) của hàm gốc, ngay cả khi hàm gốc đã kết thúc.
Closure cho phép chúng ta gắn kết dữ liệu cục bộ với một hàm và lưu trữ trạng thái của hàm đó.
Closure thường sử dụng khi chúng ta muốn tạo ra các hàm có khả năng ghi nhớ trạng thái hoặc giữ lại thông tin từ lần gọi trước.
Decorator (bộ trang trí):
Là một cú pháp ngắn gọn để bao bọc một hàm bằng một hàm khác, mở rộng hoặc thay đổi hành vi của hàm gốc mà không cần sửa đổi mã nguồn của hàm đó.
Decorator cho phép chúng ta thay đổi hành vi của một hàm mà không làm thay đổi mã nguồn của hàm đó.
'''

#bài tập 4
print([country for country in countries])

#bài tập 5
print([name for name in names])

#bài tập 6
print([number for number in numbers])

                #LEVEL 2
#bài tập 1
new_list = list(map(lambda x: x.upper(), countries))
print(new_list)

#bài tập 2
new_number_square = list(map(lambda x : x * x, numbers))
print(new_number_square)

#bài tập 3
new_upper_name = list(map(lambda name: name.upper(), names))
print(new_upper_name)

#bài tập 4
countries_land = list(filter(lambda country: 'land' in country, countries))
print(countries_land)

#bài tập 5
country6_letters = list(filter(lambda country: len(country) == 6, countries))
print(country6_letters)

#bài tập 6
country6_more_letters = list(filter(lambda country: len(country) >= 6, countries))
print(country6_more_letters)

#bài tập 7
countriesF_start = list(filter(lambda country: country.startswith('F'), countries))
print(countriesF_start)

#bài tập 8
from functools import reduce

from pytz import country_names
chain = (map(lambda num: num * num, numbers) and filter(lambda num: num >= 5, numbers) and reduce(lambda x, y: x + y, numbers))
print(chain)

#bài tập 9
def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))
my_list = [1, 'apple', 2, 'banana', 'orange']
result = get_string_lists(my_list)
print(result)

#bài tập 10
print(reduce(lambda x, y: x + y, numbers))

#bài tập 11
print(reduce(lambda x, y: x + ', ' + y, countries[:-1]) + ', and ' + countries[-1] + ' are north European countries.')

#bài tập 12
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
def categorize_countries(lst):
    return list(filter(lambda country: any(pattern in country for pattern in ['island', 'land', 'ia', 'stan']), countries))
print(categorize_countries(countries))

#bài tập 13
def countries_dict(lst):
    return dict((country, country[0]) for country in countries)
print(countries_dict(countries))

#bài tập 14
def get_first_ten_countries(lst):
    return lst[:11]

def get_last_ten_countries(lst):
    return lst[-10: len(lst)-1]




    