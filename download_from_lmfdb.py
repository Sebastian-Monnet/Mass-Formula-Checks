import urllib.request, json 

def get_with_offset(e,f,offset):
    str1 = "https://www.lmfdb.org/api/lf_fields/?p=i2&e=i"
    str2 = "&f=i"
    str3 = "&_format=json&_offset="
    actual_string = str1 + str(e) + str2 + str(f) + str3 + str(offset)
    with urllib.request.urlopen(actual_string) as url:
        data = json.load(url)
    return data

def get_all_fields(e,f):
    data = []
    offset = 0
    done = False
    while not done:
        contrib = get_with_offset(e,f,offset)["data"]
        offset += 100
        data += contrib
        if contrib == []: 
            done = True
    return data

def download_file(e,f): 
    data = get_all_fields(e, f)
    with open("e" + str(e) + "f" + str(f) +".txt", "w") as f:
        f.write("polys := [")
        f.write("\n")
        for dic in data[:-1]:
            f.write(str(dic['coeffs']) + ",")
            f.write("\n")
        f.write(str(data[-1]['coeffs']))
        f.write("];")

for e,f in [(4,1), (8,1), (4,2), (12,1), (4,3)]:
        download_file(e,f)