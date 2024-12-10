from year_2024.day_09 import checksum, parse_and_defragment_files

text_1 = "12345"
text_2 = "2333133121414131402"


def test_checksum():
    assert checksum(parse_and_defragment_files(text_1)) == 60
    assert checksum(parse_and_defragment_files(text_2)) == 1928