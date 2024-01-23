# def exercise_d():
#     data = [['Student', 'Grade'],
#             ['Ali', 'A*']]

#     for row in data:
#         print('\t'.join(row))

#     with open('output.txt', 'w') as file:
#         for row in data:
#             file.write('\t'.join(row) + '\n')

#     print('saving...')
#     print('Data Saved Successfully!')

# exercise_d()

def exercise_d():
    data = [['Student', 'Grade'],
            ['Ali', 'A*']]

    data = list(map(list, zip(*data)))

    for row in data:
        print('\t'.join(row))

    with open('output.txt', 'w') as file:
        for row in data:
            file.write('\t'.join(row) + '\n')

    print('saving...')
    print('Data Saved Successfully!')

exercise_d()