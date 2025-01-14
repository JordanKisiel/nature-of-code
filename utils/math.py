def map_to_range(num, in_min, in_max, out_min, out_max):
    return (out_min + 
            (num - in_min) / 
            (in_max - in_min) * 
            (out_max - out_min))