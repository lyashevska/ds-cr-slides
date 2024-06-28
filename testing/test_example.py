def fahrenheit_to_celsius(temp_list, converted_temps=[]):
    for temp in temp_list:
        temp_c = (temp - 32.0) * (5.0/9.0)
        converted_temps.append(temp_c)
    return converted_temps

def test_convert():  # Special name!
    assert fahrenheit_to_celsius([32.0, 77.0]) == [0.0, 25.0]
    assert (fahrenheit_to_celsius([100], converted_temps = [0.0, 25.0])
            == [0.0, 25.0, 37.77777777777778])
    assert fahrenheit_to_celsius([32.0, 77.0]) == [0.0, 25.0]
