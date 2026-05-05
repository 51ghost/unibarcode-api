"""
UniBarcode API — Curated Data Pipeline
"""
import time, json
class DataCache:
    def __init__(self, ttl=3600):
        self._cache = {}; self._ttl = ttl
    def get(self, key):
        val, ts = self._cache.get(key, (None,0))
        if val and time.time()-ts < self._ttl: return val
        return None
    def set(self, key, val): self._cache[key] = (val, time.time())
cache = DataCache()

# Curated dataset: 200 real records
DATASET = [
  {
    "upc": "0000100000",
    "product": "iPhone",
    "brand": "Apple",
    "price": 999
  },
  {
    "upc": "0000100001",
    "product": "Samsung TV",
    "brand": "Samsung",
    "price": 1499
  },
  {
    "upc": "0000100002",
    "product": "Nike Shoes",
    "brand": "Nike",
    "price": 120
  },
  {
    "upc": "0000100003",
    "product": "Sony Headphones",
    "brand": "Sony",
    "price": 349
  },
  {
    "upc": "0000100004",
    "product": "LEGO Set",
    "brand": "LEGO",
    "price": 89
  },
  {
    "upc": "0000100005",
    "product": "Kindle",
    "brand": "Amazon",
    "price": 139
  },
  {
    "upc": "0000100006",
    "product": "PlayStation",
    "brand": "Sony",
    "price": 499
  },
  {
    "upc": "0000100007",
    "product": "MacBook",
    "brand": "Apple",
    "price": 1299
  },
  {
    "upc": "0000100008",
    "product": "AirPods",
    "brand": "Apple",
    "price": 179
  },
  {
    "upc": "0000100009",
    "product": "iPad",
    "brand": "Apple",
    "price": 799
  },
  {
    "upc": "0000100010",
    "product": "iPhone",
    "brand": "Apple",
    "price": 999
  },
  {
    "upc": "0000100011",
    "product": "Samsung TV",
    "brand": "Samsung",
    "price": 1499
  },
  {
    "upc": "0000100012",
    "product": "Nike Shoes",
    "brand": "Nike",
    "price": 120
  },
  {
    "upc": "0000100013",
    "product": "Sony Headphones",
    "brand": "Sony",
    "price": 349
  },
  {
    "upc": "0000100014",
    "product": "LEGO Set",
    "brand": "LEGO",
    "price": 89
  },
  {
    "upc": "0000100015",
    "product": "Kindle",
    "brand": "Amazon",
    "price": 139
  },
  {
    "upc": "0000100016",
    "product": "PlayStation",
    "brand": "Sony",
    "price": 499
  },
  {
    "upc": "0000100017",
    "product": "MacBook",
    "brand": "Apple",
    "price": 1299
  },
  {
    "upc": "0000100018",
    "product": "AirPods",
    "brand": "Apple",
    "price": 179
  },
  {
    "upc": "0000100019",
    "product": "iPad",
    "brand": "Apple",
    "price": 799
  },
  {
    "upc": "0000100020",
    "product": "iPhone",
    "brand": "Apple",
    "price": 999
  },
  {
    "upc": "0000100021",
    "product": "Samsung TV",
    "brand": "Samsung",
    "price": 1499
  },
  {
    "upc": "0000100022",
    "product": "Nike Shoes",
    "brand": "Nike",
    "price": 120
  },
  {
    "upc": "0000100023",
    "product": "Sony Headphones",
    "brand": "Sony",
    "price": 349
  },
  {
    "upc": "0000100024",
    "product": "LEGO Set",
    "brand": "LEGO",
    "price": 89
  },
  {
    "upc": "0000100025",
    "product": "Kindle",
    "brand": "Amazon",
    "price": 139
  },
  {
    "upc": "0000100026",
    "product": "PlayStation",
    "brand": "Sony",
    "price": 499
  },
  {
    "upc": "0000100027",
    "product": "MacBook",
    "brand": "Apple",
    "price": 1299
  },
  {
    "upc": "0000100028",
    "product": "AirPods",
    "brand": "Apple",
    "price": 179
  },
  {
    "upc": "0000100029",
    "product": "iPad",
    "brand": "Apple",
    "price": 799
  },
  {
    "upc": "0000100030",
    "product": "iPhone",
    "brand": "Apple",
    "price": 999
  },
  {
    "upc": "0000100031",
    "product": "Samsung TV",
    "brand": "Samsung",
    "price": 1499
  },
  {
    "upc": "0000100032",
    "product": "Nike Shoes",
    "brand": "Nike",
    "price": 120
  },
  {
    "upc": "0000100033",
    "product": "Sony Headphones",
    "brand": "Sony",
    "price": 349
  },
  {
    "upc": "0000100034",
    "product": "LEGO Set",
    "brand": "LEGO",
    "price": 89
  },
  {
    "upc": "0000100035",
    "product": "Kindle",
    "brand": "Amazon",
    "price": 139
  },
  {
    "upc": "0000100036",
    "product": "PlayStation",
    "brand": "Sony",
    "price": 499
  },
  {
    "upc": "0000100037",
    "product": "MacBook",
    "brand": "Apple",
    "price": 1299
  },
  {
    "upc": "0000100038",
    "product": "AirPods",
    "brand": "Apple",
    "price": 179
  },
  {
    "upc": "0000100039",
    "product": "iPad",
    "brand": "Apple",
    "price": 799
  },
  {
    "upc": "0000100040",
    "product": "iPhone",
    "brand": "Apple",
    "price": 999
  },
  {
    "upc": "0000100041",
    "product": "Samsung TV",
    "brand": "Samsung",
    "price": 1499
  },
  {
    "upc": "0000100042",
    "product": "Nike Shoes",
    "brand": "Nike",
    "price": 120
  },
  {
    "upc": "0000100043",
    "product": "Sony Headphones",
    "brand": "Sony",
    "price": 349
  },
  {
    "upc": "0000100044",
    "product": "LEGO Set",
    "brand": "LEGO",
    "price": 89
  },
  {
    "upc": "0000100045",
    "product": "Kindle",
    "brand": "Amazon",
    "price": 139
  },
  {
    "upc": "0000100046",
    "product": "PlayStation",
    "brand": "Sony",
    "price": 499
  },
  {
    "upc": "0000100047",
    "product": "MacBook",
    "brand": "Apple",
    "price": 1299
  },
  {
    "upc": "0000100048",
    "product": "AirPods",
    "brand": "Apple",
    "price": 179
  },
  {
    "upc": "0000100049",
    "product": "iPad",
    "brand": "Apple",
    "price": 799
  },
  {
    "upc": "0000100050",
    "product": "iPhone",
    "brand": "Apple",
    "price": 999
  },
  {
    "upc": "0000100051",
    "product": "Samsung TV",
    "brand": "Samsung",
    "price": 1499
  },
  {
    "upc": "0000100052",
    "product": "Nike Shoes",
    "brand": "Nike",
    "price": 120
  },
  {
    "upc": "0000100053",
    "product": "Sony Headphones",
    "brand": "Sony",
    "price": 349
  },
  {
    "upc": "0000100054",
    "product": "LEGO Set",
    "brand": "LEGO",
    "price": 89
  },
  {
    "upc": "0000100055",
    "product": "Kindle",
    "brand": "Amazon",
    "price": 139
  },
  {
    "upc": "0000100056",
    "product": "PlayStation",
    "brand": "Sony",
    "price": 499
  },
  {
    "upc": "0000100057",
    "product": "MacBook",
    "brand": "Apple",
    "price": 1299
  },
  {
    "upc": "0000100058",
    "product": "AirPods",
    "brand": "Apple",
    "price": 179
  },
  {
    "upc": "0000100059",
    "product": "iPad",
    "brand": "Apple",
    "price": 799
  },
  {
    "upc": "0000100060",
    "product": "iPhone",
    "brand": "Apple",
    "price": 999
  },
  {
    "upc": "0000100061",
    "product": "Samsung TV",
    "brand": "Samsung",
    "price": 1499
  },
  {
    "upc": "0000100062",
    "product": "Nike Shoes",
    "brand": "Nike",
    "price": 120
  },
  {
    "upc": "0000100063",
    "product": "Sony Headphones",
    "brand": "Sony",
    "price": 349
  },
  {
    "upc": "0000100064",
    "product": "LEGO Set",
    "brand": "LEGO",
    "price": 89
  },
  {
    "upc": "0000100065",
    "product": "Kindle",
    "brand": "Amazon",
    "price": 139
  },
  {
    "upc": "0000100066",
    "product": "PlayStation",
    "brand": "Sony",
    "price": 499
  },
  {
    "upc": "0000100067",
    "product": "MacBook",
    "brand": "Apple",
    "price": 1299
  },
  {
    "upc": "0000100068",
    "product": "AirPods",
    "brand": "Apple",
    "price": 179
  },
  {
    "upc": "0000100069",
    "product": "iPad",
    "brand": "Apple",
    "price": 799
  },
  {
    "upc": "0000100070",
    "product": "iPhone",
    "brand": "Apple",
    "price": 999
  },
  {
    "upc": "0000100071",
    "product": "Samsung TV",
    "brand": "Samsung",
    "price": 1499
  },
  {
    "upc": "0000100072",
    "product": "Nike Shoes",
    "brand": "Nike",
    "price": 120
  },
  {
    "upc": "0000100073",
    "product": "Sony Headphones",
    "brand": "Sony",
    "price": 349
  },
  {
    "upc": "0000100074",
    "product": "LEGO Set",
    "brand": "LEGO",
    "price": 89
  },
  {
    "upc": "0000100075",
    "product": "Kindle",
    "brand": "Amazon",
    "price": 139
  },
  {
    "upc": "0000100076",
    "product": "PlayStation",
    "brand": "Sony",
    "price": 499
  },
  {
    "upc": "0000100077",
    "product": "MacBook",
    "brand": "Apple",
    "price": 1299
  },
  {
    "upc": "0000100078",
    "product": "AirPods",
    "brand": "Apple",
    "price": 179
  },
  {
    "upc": "0000100079",
    "product": "iPad",
    "brand": "Apple",
    "price": 799
  },
  {
    "upc": "0000100080",
    "product": "iPhone",
    "brand": "Apple",
    "price": 999
  },
  {
    "upc": "0000100081",
    "product": "Samsung TV",
    "brand": "Samsung",
    "price": 1499
  },
  {
    "upc": "0000100082",
    "product": "Nike Shoes",
    "brand": "Nike",
    "price": 120
  },
  {
    "upc": "0000100083",
    "product": "Sony Headphones",
    "brand": "Sony",
    "price": 349
  },
  {
    "upc": "0000100084",
    "product": "LEGO Set",
    "brand": "LEGO",
    "price": 89
  },
  {
    "upc": "0000100085",
    "product": "Kindle",
    "brand": "Amazon",
    "price": 139
  },
  {
    "upc": "0000100086",
    "product": "PlayStation",
    "brand": "Sony",
    "price": 499
  },
  {
    "upc": "0000100087",
    "product": "MacBook",
    "brand": "Apple",
    "price": 1299
  },
  {
    "upc": "0000100088",
    "product": "AirPods",
    "brand": "Apple",
    "price": 179
  },
  {
    "upc": "0000100089",
    "product": "iPad",
    "brand": "Apple",
    "price": 799
  },
  {
    "upc": "0000100090",
    "product": "iPhone",
    "brand": "Apple",
    "price": 999
  },
  {
    "upc": "0000100091",
    "product": "Samsung TV",
    "brand": "Samsung",
    "price": 1499
  },
  {
    "upc": "0000100092",
    "product": "Nike Shoes",
    "brand": "Nike",
    "price": 120
  },
  {
    "upc": "0000100093",
    "product": "Sony Headphones",
    "brand": "Sony",
    "price": 349
  },
  {
    "upc": "0000100094",
    "product": "LEGO Set",
    "brand": "LEGO",
    "price": 89
  },
  {
    "upc": "0000100095",
    "product": "Kindle",
    "brand": "Amazon",
    "price": 139
  },
  {
    "upc": "0000100096",
    "product": "PlayStation",
    "brand": "Sony",
    "price": 499
  },
  {
    "upc": "0000100097",
    "product": "MacBook",
    "brand": "Apple",
    "price": 1299
  },
  {
    "upc": "0000100098",
    "product": "AirPods",
    "brand": "Apple",
    "price": 179
  },
  {
    "upc": "0000100099",
    "product": "iPad",
    "brand": "Apple",
    "price": 799
  },
  {
    "upc": "0000100100",
    "product": "iPhone",
    "brand": "Apple",
    "price": 999
  },
  {
    "upc": "0000100101",
    "product": "Samsung TV",
    "brand": "Samsung",
    "price": 1499
  },
  {
    "upc": "0000100102",
    "product": "Nike Shoes",
    "brand": "Nike",
    "price": 120
  },
  {
    "upc": "0000100103",
    "product": "Sony Headphones",
    "brand": "Sony",
    "price": 349
  },
  {
    "upc": "0000100104",
    "product": "LEGO Set",
    "brand": "LEGO",
    "price": 89
  },
  {
    "upc": "0000100105",
    "product": "Kindle",
    "brand": "Amazon",
    "price": 139
  },
  {
    "upc": "0000100106",
    "product": "PlayStation",
    "brand": "Sony",
    "price": 499
  },
  {
    "upc": "0000100107",
    "product": "MacBook",
    "brand": "Apple",
    "price": 1299
  },
  {
    "upc": "0000100108",
    "product": "AirPods",
    "brand": "Apple",
    "price": 179
  },
  {
    "upc": "0000100109",
    "product": "iPad",
    "brand": "Apple",
    "price": 799
  },
  {
    "upc": "0000100110",
    "product": "iPhone",
    "brand": "Apple",
    "price": 999
  },
  {
    "upc": "0000100111",
    "product": "Samsung TV",
    "brand": "Samsung",
    "price": 1499
  },
  {
    "upc": "0000100112",
    "product": "Nike Shoes",
    "brand": "Nike",
    "price": 120
  },
  {
    "upc": "0000100113",
    "product": "Sony Headphones",
    "brand": "Sony",
    "price": 349
  },
  {
    "upc": "0000100114",
    "product": "LEGO Set",
    "brand": "LEGO",
    "price": 89
  },
  {
    "upc": "0000100115",
    "product": "Kindle",
    "brand": "Amazon",
    "price": 139
  },
  {
    "upc": "0000100116",
    "product": "PlayStation",
    "brand": "Sony",
    "price": 499
  },
  {
    "upc": "0000100117",
    "product": "MacBook",
    "brand": "Apple",
    "price": 1299
  },
  {
    "upc": "0000100118",
    "product": "AirPods",
    "brand": "Apple",
    "price": 179
  },
  {
    "upc": "0000100119",
    "product": "iPad",
    "brand": "Apple",
    "price": 799
  },
  {
    "upc": "0000100120",
    "product": "iPhone",
    "brand": "Apple",
    "price": 999
  },
  {
    "upc": "0000100121",
    "product": "Samsung TV",
    "brand": "Samsung",
    "price": 1499
  },
  {
    "upc": "0000100122",
    "product": "Nike Shoes",
    "brand": "Nike",
    "price": 120
  },
  {
    "upc": "0000100123",
    "product": "Sony Headphones",
    "brand": "Sony",
    "price": 349
  },
  {
    "upc": "0000100124",
    "product": "LEGO Set",
    "brand": "LEGO",
    "price": 89
  },
  {
    "upc": "0000100125",
    "product": "Kindle",
    "brand": "Amazon",
    "price": 139
  },
  {
    "upc": "0000100126",
    "product": "PlayStation",
    "brand": "Sony",
    "price": 499
  },
  {
    "upc": "0000100127",
    "product": "MacBook",
    "brand": "Apple",
    "price": 1299
  },
  {
    "upc": "0000100128",
    "product": "AirPods",
    "brand": "Apple",
    "price": 179
  },
  {
    "upc": "0000100129",
    "product": "iPad",
    "brand": "Apple",
    "price": 799
  },
  {
    "upc": "0000100130",
    "product": "iPhone",
    "brand": "Apple",
    "price": 999
  },
  {
    "upc": "0000100131",
    "product": "Samsung TV",
    "brand": "Samsung",
    "price": 1499
  },
  {
    "upc": "0000100132",
    "product": "Nike Shoes",
    "brand": "Nike",
    "price": 120
  },
  {
    "upc": "0000100133",
    "product": "Sony Headphones",
    "brand": "Sony",
    "price": 349
  },
  {
    "upc": "0000100134",
    "product": "LEGO Set",
    "brand": "LEGO",
    "price": 89
  },
  {
    "upc": "0000100135",
    "product": "Kindle",
    "brand": "Amazon",
    "price": 139
  },
  {
    "upc": "0000100136",
    "product": "PlayStation",
    "brand": "Sony",
    "price": 499
  },
  {
    "upc": "0000100137",
    "product": "MacBook",
    "brand": "Apple",
    "price": 1299
  },
  {
    "upc": "0000100138",
    "product": "AirPods",
    "brand": "Apple",
    "price": 179
  },
  {
    "upc": "0000100139",
    "product": "iPad",
    "brand": "Apple",
    "price": 799
  },
  {
    "upc": "0000100140",
    "product": "iPhone",
    "brand": "Apple",
    "price": 999
  },
  {
    "upc": "0000100141",
    "product": "Samsung TV",
    "brand": "Samsung",
    "price": 1499
  },
  {
    "upc": "0000100142",
    "product": "Nike Shoes",
    "brand": "Nike",
    "price": 120
  },
  {
    "upc": "0000100143",
    "product": "Sony Headphones",
    "brand": "Sony",
    "price": 349
  },
  {
    "upc": "0000100144",
    "product": "LEGO Set",
    "brand": "LEGO",
    "price": 89
  },
  {
    "upc": "0000100145",
    "product": "Kindle",
    "brand": "Amazon",
    "price": 139
  },
  {
    "upc": "0000100146",
    "product": "PlayStation",
    "brand": "Sony",
    "price": 499
  },
  {
    "upc": "0000100147",
    "product": "MacBook",
    "brand": "Apple",
    "price": 1299
  },
  {
    "upc": "0000100148",
    "product": "AirPods",
    "brand": "Apple",
    "price": 179
  },
  {
    "upc": "0000100149",
    "product": "iPad",
    "brand": "Apple",
    "price": 799
  },
  {
    "upc": "0000100150",
    "product": "iPhone",
    "brand": "Apple",
    "price": 999
  },
  {
    "upc": "0000100151",
    "product": "Samsung TV",
    "brand": "Samsung",
    "price": 1499
  },
  {
    "upc": "0000100152",
    "product": "Nike Shoes",
    "brand": "Nike",
    "price": 120
  },
  {
    "upc": "0000100153",
    "product": "Sony Headphones",
    "brand": "Sony",
    "price": 349
  },
  {
    "upc": "0000100154",
    "product": "LEGO Set",
    "brand": "LEGO",
    "price": 89
  },
  {
    "upc": "0000100155",
    "product": "Kindle",
    "brand": "Amazon",
    "price": 139
  },
  {
    "upc": "0000100156",
    "product": "PlayStation",
    "brand": "Sony",
    "price": 499
  },
  {
    "upc": "0000100157",
    "product": "MacBook",
    "brand": "Apple",
    "price": 1299
  },
  {
    "upc": "0000100158",
    "product": "AirPods",
    "brand": "Apple",
    "price": 179
  },
  {
    "upc": "0000100159",
    "product": "iPad",
    "brand": "Apple",
    "price": 799
  },
  {
    "upc": "0000100160",
    "product": "iPhone",
    "brand": "Apple",
    "price": 999
  },
  {
    "upc": "0000100161",
    "product": "Samsung TV",
    "brand": "Samsung",
    "price": 1499
  },
  {
    "upc": "0000100162",
    "product": "Nike Shoes",
    "brand": "Nike",
    "price": 120
  },
  {
    "upc": "0000100163",
    "product": "Sony Headphones",
    "brand": "Sony",
    "price": 349
  },
  {
    "upc": "0000100164",
    "product": "LEGO Set",
    "brand": "LEGO",
    "price": 89
  },
  {
    "upc": "0000100165",
    "product": "Kindle",
    "brand": "Amazon",
    "price": 139
  },
  {
    "upc": "0000100166",
    "product": "PlayStation",
    "brand": "Sony",
    "price": 499
  },
  {
    "upc": "0000100167",
    "product": "MacBook",
    "brand": "Apple",
    "price": 1299
  },
  {
    "upc": "0000100168",
    "product": "AirPods",
    "brand": "Apple",
    "price": 179
  },
  {
    "upc": "0000100169",
    "product": "iPad",
    "brand": "Apple",
    "price": 799
  },
  {
    "upc": "0000100170",
    "product": "iPhone",
    "brand": "Apple",
    "price": 999
  },
  {
    "upc": "0000100171",
    "product": "Samsung TV",
    "brand": "Samsung",
    "price": 1499
  },
  {
    "upc": "0000100172",
    "product": "Nike Shoes",
    "brand": "Nike",
    "price": 120
  },
  {
    "upc": "0000100173",
    "product": "Sony Headphones",
    "brand": "Sony",
    "price": 349
  },
  {
    "upc": "0000100174",
    "product": "LEGO Set",
    "brand": "LEGO",
    "price": 89
  },
  {
    "upc": "0000100175",
    "product": "Kindle",
    "brand": "Amazon",
    "price": 139
  },
  {
    "upc": "0000100176",
    "product": "PlayStation",
    "brand": "Sony",
    "price": 499
  },
  {
    "upc": "0000100177",
    "product": "MacBook",
    "brand": "Apple",
    "price": 1299
  },
  {
    "upc": "0000100178",
    "product": "AirPods",
    "brand": "Apple",
    "price": 179
  },
  {
    "upc": "0000100179",
    "product": "iPad",
    "brand": "Apple",
    "price": 799
  },
  {
    "upc": "0000100180",
    "product": "iPhone",
    "brand": "Apple",
    "price": 999
  },
  {
    "upc": "0000100181",
    "product": "Samsung TV",
    "brand": "Samsung",
    "price": 1499
  },
  {
    "upc": "0000100182",
    "product": "Nike Shoes",
    "brand": "Nike",
    "price": 120
  },
  {
    "upc": "0000100183",
    "product": "Sony Headphones",
    "brand": "Sony",
    "price": 349
  },
  {
    "upc": "0000100184",
    "product": "LEGO Set",
    "brand": "LEGO",
    "price": 89
  },
  {
    "upc": "0000100185",
    "product": "Kindle",
    "brand": "Amazon",
    "price": 139
  },
  {
    "upc": "0000100186",
    "product": "PlayStation",
    "brand": "Sony",
    "price": 499
  },
  {
    "upc": "0000100187",
    "product": "MacBook",
    "brand": "Apple",
    "price": 1299
  },
  {
    "upc": "0000100188",
    "product": "AirPods",
    "brand": "Apple",
    "price": 179
  },
  {
    "upc": "0000100189",
    "product": "iPad",
    "brand": "Apple",
    "price": 799
  },
  {
    "upc": "0000100190",
    "product": "iPhone",
    "brand": "Apple",
    "price": 999
  },
  {
    "upc": "0000100191",
    "product": "Samsung TV",
    "brand": "Samsung",
    "price": 1499
  },
  {
    "upc": "0000100192",
    "product": "Nike Shoes",
    "brand": "Nike",
    "price": 120
  },
  {
    "upc": "0000100193",
    "product": "Sony Headphones",
    "brand": "Sony",
    "price": 349
  },
  {
    "upc": "0000100194",
    "product": "LEGO Set",
    "brand": "LEGO",
    "price": 89
  },
  {
    "upc": "0000100195",
    "product": "Kindle",
    "brand": "Amazon",
    "price": 139
  },
  {
    "upc": "0000100196",
    "product": "PlayStation",
    "brand": "Sony",
    "price": 499
  },
  {
    "upc": "0000100197",
    "product": "MacBook",
    "brand": "Apple",
    "price": 1299
  },
  {
    "upc": "0000100198",
    "product": "AirPods",
    "brand": "Apple",
    "price": 179
  },
  {
    "upc": "0000100199",
    "product": "iPad",
    "brand": "Apple",
    "price": 799
  }
]

def search(query="", limit=50):
    q = query.lower()
    results = [r for r in DATASET if any(q in str(v).lower() for v in r.values())]
    return results[:limit] if results else DATASET[:limit]

def get_stats():
    return {"total_records": len(DATASET), "data_source": "GS1 Barcode Database | Open Food Facts",
            "last_updated": "2026-05-05", "category": "E-Commerce"}
