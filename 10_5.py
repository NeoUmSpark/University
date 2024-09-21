import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        line = file.readline()
        while True:
            all_data.append(line)
            if not line:
                break


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start_time_line = datetime.datetime.now()
    for filename in filenames:
        read_info(filename)
    end_time_line = datetime.datetime.now()
    print(f"Время выполнения линейного вызова: {end_time_line - start_time_line}")

    start_time_multi = datetime.datetime.now()
    with Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end_time_multi = datetime.datetime.now()
    print(f"Время выполнения многопроцессного вызова: {end_time_multi - start_time_multi}")
