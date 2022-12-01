with open('./data/day_16.txt') as fd:
    raw = fd.read().strip()

class color:
    # https://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python
    GREEN = '\033[92m'
    RED = '\033[91m'
    DARKCYAN = '\033[36m'
    END = '\033[0m'


def bits(s: str) -> str:
    return ''.join([bin(int(c, 16))[2:].zfill(4) for c in s])


assert bits('D2FE28') == '110100101111111000101000'
assert bits('38006F45291200') == '00111000000000000110111101000101001010010001001000000000'
assert bits('EE00D40C823060') == '11101110000000001101010000001100100000100011000001100000'

def get_label(s: str) -> int:
    print(f"version: {s[:3]}->{int(s[:3], 2)}")
    # print(f"{int(s[:3], 2)}+", end='')
    return int(s[:3], 2)


def get_type(s: str) -> int:
    print(f"type ID: {s[3:6]}->{int(s[3:6], 2)}")
    return int(s[3:6], 2)


def literal(s: str, debug=True) -> (str, int):
    keep_on, i = int(s[0]), 1
    res = ''
    while keep_on:
        res += s[i:i + 4]
        i += 5
        keep_on = int(s[i - 1])
    res += s[i:i + 4]
    i += 4
    if debug:
        print(f"parsed literal ({i}):", end='')
        for j in range(i):
            if j % 5 == 0:
                print(color.GREEN + s[j] + color.END, end='')
            else:
                print(s[j], end='')
        print()
    return res, i


def parse(s: str, rec=None, DEBUG=True):
    if DEBUG:
        print(f"(len:{len(s)}), {color.RED + s[:3] + color.DARKCYAN + s[3:6] + color.END + s[6:]}")
    version = get_label(s)
    type_id = get_type(s)
    value = ''
    i = 6
    if type_id == 4:    # "literal value"
        value, parsed = literal(s[6:])
        i += parsed
    else:               # "operator"
        l_type_id = s[6]
        if l_type_id == '0':    # next 15 bits are the length of the subpackage
            l_sub_packets = int(s[7:22], 2)
            i, parsed = 22, 0
            print(f"Length of subpacket: {l_sub_packets}: {s[22:i + l_sub_packets]}")
            while i < 22 + l_sub_packets:
                ver, parsed, value = parse(s[22 + parsed:i+l_sub_packets])
                i += parsed
                version += ver
        else:           # next 11 bits are the number of subpackets
            i = 18
            num_sub_packets = int(s[7:i], 2)
            print(f"Number of subpackets: {num_sub_packets}")
            for n in range(num_sub_packets):
                ver, parsed, value = parse(s[i:])
                i += parsed
                version += ver

    return version, i, value


# print(parse(bits('D2FE28')))    # (6, 4, year_2021)

# assert parse(bits('D2FE28')) == (6, 4, year_2021)
# assert parse(bits('D2FE28')) == (6, 21, '011111100101')

## Two subpackets in 27 bits:
# print(parse(bits('38006F45291200')))    # at least it doesn't fail

## Three subpackets 11 bits each
# print(parse(bits('EE00D40C823060')))

# print(parse(bits('8A004A801A8002F478')))
# assert parse(bits('8A004A801A8002F478'))[0] == 16

# print(parse(bits('620080001611562C8802118E34')))
# assert parse(bits('620080001611562C8802118E34'))[0] == 12

# print(parse(bits('C0015000016115A2E0802F182340')))
# assert parse(bits('C0015000016115A2E0802F182340'))[0] == 23

# assert parse(bits('A0016C880162017C3686B18A3D4780'))[0] == 31

print(parse(bits(raw)))