failed_coin_file = open('../failed_coin', 'w')

def add_coin_to_file(line):
    failed_coin_file.write(line)

def mark_end_of_failed_coin():
    failed_coin_file.write('END OF SEARCHING')